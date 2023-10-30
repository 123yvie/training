# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 3:32 PM
# @Author  : chenxu
# @File    : render_handler.py  渲染yaml模版
# **************************
import importlib
import inspect
import os
import re
import sys
from contextlib import ExitStack

import jinja2
import yaml

from common.csv_util import from_csv_to_json, env_replace_yaml_data
from common.get_path import get_root_path
from common.logger import logger
from common.read_data import data

BASE_PATH = get_root_path()


def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')
                              ).get_template(filename).render(**kwargs)


# 加载模版方法
def all_functions():
    """加载template_param.py模块"""
    debug_module = importlib.import_module("core.template_param")
    all_function = inspect.getmembers(debug_module, inspect.isfunction)
    # 函数列表循环遍历替换 value = getattr(object, key)执行后出现<function>
    for i in range(len(all_function)):
        change = list(all_function[i])
        change[1] = all_function[i][1]()
        all_function[i] = tuple(change)
    return dict(all_function)


# 生成临时yaml文件地址
def generate_temps_file_path(yaml_template_path):
    file_name = os.path.basename(yaml_template_path)
    new_file_name = os.path.splitext(file_name)[0] + '_new' + os.path.splitext(file_name)[-1]
    return os.path.join(BASE_PATH, 'temps', new_file_name)


# 渲染yaml模版
def render_yaml(yaml_template_path):
    # 设置yaml模版文件路径
    # yaml_template_path = get_root_path() + '/testcase/api_test/payment/test_detail_search.yaml'
    # 渲染yaml模版动态参数
    r = render(yaml_template_path, **all_functions())
    # 加载渲染后yaml模版文件
    yaml_template_data = yaml.safe_load(r)
    # 生成临时yaml文件路径
    yaml_template_temp_path = generate_temps_file_path(yaml_template_path)
    # 设置csv数据文件路径
    csv_path = get_root_path() + yaml.safe_load(r)[0]['data_url']
    # 加赞csv数据文件
    profileList = from_csv_to_json(csv_path)
    # 切割yaml模版文件
    yaml_file_lines = (r.splitlines(True))
    # 将csv数据文件渲染yaml临时文件
    env_replace_yaml_data(yaml_file_lines, yaml_template_temp_path)
    # 渲染后yaml文件数据
    values = data.load_yaml(yaml_template_temp_path)
    logger.info("yaml模版文件路径 ==>> {}".format(yaml_template_path))
    logger.info("加载渲染后yaml模版文件 ==>> {}".format(yaml_template_data))
    logger.info("生成临时yaml文件路径 ==>> {}".format(yaml_template_data))
    logger.info("csv数据文件路径 ==>> {}".format(csv_path))
    logger.info("加载csv数据文件 ==>> {}".format(profileList[len(profileList)-1]))
    logger.info("切割yaml模版文件 ==>> {}".format(yaml_file_lines))
    logger.info("渲染后yaml文件数据 ==>> {}".format(values))
    return values

# if __name__ == '__main__':
# # 设置yaml模版文件路径
# yaml_template_path = get_root_path() + '/testcase/api_test/payment/test_detail_search.yaml'
# # 渲染yaml模版动态参数
# r = render(yaml_template_path, **all_functions())
# # 加载渲染后yaml模版文件
# yaml_template_data = yaml.safe_load(r);
# # 生成临时yaml文件路径
# yaml_template_temp_path = generate_temps_file_path(yaml_template_path)
# # 设置csv数据文件路径
# csv_path = get_root_path() + yaml.safe_load(r)[0]['data_url']
# # 加赞csv数据文件
# profileList = from_csv_to_json(csv_path)
# # 切割yaml模版文件
# yaml_file_lines = (r.splitlines(True))
# # 将csv数据文件渲染yaml临时文件
# env_replace_yaml_data(yaml_file_lines, yaml_template_temp_path)
# # 渲染后yaml文件数据
# values = data.load_yaml(yaml_template_temp_path)
# logger.info("yaml模版文件路径 ==>> {}".format(yaml_template_path))
# logger.info("加载渲染后yaml模版文件 ==>> {}".format(yaml_template_data))
# logger.info("生成临时yaml文件路径 ==>> {}".format(yaml_template_data))
# logger.info("csv数据文件路径 ==>> {}".format(csv_path))
# logger.info("加载csv数据文件 ==>> {}".format(profileList))
# logger.info("切割yaml模版文件 ==>> {}".format(yaml_file_lines))
# logger.info("切割yaml模版文件 ==>> {}".format(yaml_file_lines))
# logger.info("渲染后yaml文件数据 ==>> {}".format(values))
