# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 3:32 PM
# @Author  : chenxu
# @File    : get_path.py
# **************************
import os


def get_path():
    # 返回绝对路径
    current_path = os.path.abspath(__file__)
    return current_path


def get_root_path():
    # 返回项目根目录
    root_path = os.path.dirname(os.path.dirname(get_path()))
    return root_path



def get_file_path(name):
    # 获得目录
    file_path = os.path.join(os.path.dirname(os.path.dirname(get_path()) + os.path.sep + "."), name)
    return file_path


def get_xls_path(xls_name):
    xls_path = get_file_path(xls_name)
    return xls_path


def get_json_path(json_name):
    json_path = get_file_path(json_name)
    return json_path


if __name__ == '__main__':
    print(get_path())
