# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 3:32 PM
# @Author  : chenxu
# @File    : config_handler.py  config配置文件相关操作
# **************************
from common.get_path import get_root_path
from common.read_data import data

# 获取全局配置信息
result = data.load_yaml(get_root_path() + '/config.yml')
# 获取当前环境
env = result['env']


class ConfigHandler():

    def __init__(self):
        pass

    # 获取当前环境base_url
    def get_env_base_url(self):
        return result[env]['url']

    # 获取当前环境token
    def get_env_token(self):
        return result[env]['token']

    def get_evn(self):
        return env


config = ConfigHandler()
