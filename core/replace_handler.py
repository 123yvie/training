# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 3:32 PM
# @Author  : chenxu
# @File    : replace_handler.py
# **************************

# 替换param参数中对应字符
import json


def replace_json_param(dict_params):
    re_json = json.loads(str(dict_params).replace("|", "','").replace('None', "''").replace('\"', "\\'").replace('\'', '\"').replace('True', 'true').replace('False', 'false'))
    # re_json = json.loads(
    #     str(dict_params).replace("|", "','").replace('None', "''").replace('\'', '\"'))
    return re_json
    #  old:return json.loads(str(dict_params).replace("|", "','").replace('None', "''").replace('"', '\"'))
    #  jiaqi update: transform " to \' in yaml by [replace('\"', "\\'")]
    #  and then  transform ' to " in yaml by [replace('\'', '\"')]
    #  and then  transform \" to ' in yaml by [replace('\\"', '\')]
    #  .replace('\\"', '\'')

