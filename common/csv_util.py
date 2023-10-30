# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 3:32 PM
# @Author  : chenxu
# @File    : csv_util.py
# **************************
import csv
import re
from contextlib import ExitStack

"""
将csv文件转换成json
"""
profileList = []


def from_csv_to_json(csv_path):
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            profileList.append(dict(row))
        return profileList


# yaml_file为YAML模板文件
# new_yaml_file为新生成的带有测试数据的YAML文件
def env_replace_yaml(yaml_file, new_yaml_file):
    try:
        with ExitStack() as stack:
            yml_file = stack.enter_context(open(yaml_file, 'r+'))
            yml_output = stack.enter_context(open(new_yaml_file, 'w'))
            # 先读取YAML模板文件，返回值为字符串列表
            yml_file_lines = yml_file.readlines()
            print(type(yml_file_lines))
            # profileList的长度即为测试用例的数量
            for i in range(0, len(profileList)):
                # 循环遍历列表
                for line in yml_file_lines:
                    new_line = line
                    # 如果找到以“$csv{”开头的字符串
                    if new_line.find('$csv{') > 0:
                        # 对字符串以“:”切割
                        env_list = new_line.split(':')
                        # 取“:”后面的部分，去掉首尾空格，再以“{”切割，再以“}”切割取出变量名称，比如“name”
                        env_name = env_list[1].strip().split('$csv{', 1)[1].split('}')[0]
                        replacement = ""
                        # 如果name在字典列表的key里
                        if env_name in profileList[i].keys():
                            # 取出name对应的值赋给replacement
                            replacement = profileList[i][env_name]
                            # 用replacement替换掉YAML模板中的“$csv{name}”
                            for j in range(0, len(profileList)):
                                new_line = new_line.replace(env_list[1].strip(), replacement)
                    # 将new_line写入到yml_output文件里
                    yml_output.write(new_line)
                yml_output.write("\n\n")
    except IOError as e:
        print("Error: " + format(str(e)))
        raise


# yaml_file为YAML模板文件
# new_yaml_file为新生成的带有测试数据的YAML文件
def env_replace_yaml_data(yml_file_lines, new_yaml_file):
    try:
        with ExitStack() as stack:
            # yml_file = stack.enter_context(open(yaml_template_path, 'r+'))
            yml_output = stack.enter_context(open(new_yaml_file, 'w', encoding='utf-8'))
            # profileList的长度即为测试用例的数量
            profile = [profileList[len(profileList)-1]]
            for i in range(0, len(profile)):
                # 循环遍历列表
                for line in yml_file_lines:
                    new_line = line
                    # 如果找到以“$csv{”开头的字符串
                    if new_line.find('$csv{') > 0:
                        # 对字符串以“:”切割
                        env_list = new_line.split(':')
                        pattern = r'\$csv{(.*?)}'
                        # 取“:”后面的部分，去掉首尾空格，再以“{”切割，再以“}”正则取出变量名称，比如“name”
                        env_name_list = re.findall(pattern, env_list[1])
                        replacement = ""
                        if len(env_name_list) > 0:
                            # 如果name在字典列表的key里
                            for env_name in env_name_list:
                                if env_name != '':
                                    if env_name in profile[i].keys():
                                        # 取出name对应的值赋给replacement
                                        replacement = profile[i][env_name]
                                        # 用replacement替换掉YAML模板中的“$csv{name}”
                                        new_line = new_line.replace('$csv{' + env_name + '}', replacement)
                    # 将new_line写入到yml_output文件里
                    yml_output.write(new_line)
                yml_output.write("\n\n")
    except IOError as e:
        print("Error: " + format(str(e)))
        raise


if __name__ == '__main__':
    new_line = 'url: /cgi-bin/token/abc/$csv{secret}/aa/ddd/$csv{grant_type}'
