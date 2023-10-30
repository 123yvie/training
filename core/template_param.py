# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 3:32 PM
# @Author  : chenxu
# @File    : template_param.py  (yaml文件中动态参数 规则：参数名对应 -> 方法名)
# **************************


from common.logger import logger

from core.config_handler import config


# yaml模版文件 base_url
def get_base_url():
    env = config.get_evn()
    url = config.get_env_base_url()
    token = config.get_env_token()
    logger.info("执行env环境 ==>> {}".format(env))
    logger.info("url ==>> {}".format(url))
    logger.info("token ==>> {}".format(token))
    return str(url)
