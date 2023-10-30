# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 3:32 PM
# @Author  : chenxu
# @File    : conftest.py
# **************************
import allure
import pytest

from common.logger import logger
from core.config_handler import config


@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")


@allure.step("前置步骤 ==>> 管理员用户登录")
def step_login(username, password):
    logger.info("前置步骤 ==>> 管理员 {} 登录，返回信息 为：{}".format(username, password))


@pytest.fixture(scope="session")
def init_fixture():
    # 获取token
    yield config.get_env_token()        #return用法
    # value = data.load_yaml(BASE_PATH + '/config.yml')
    # env = value['env']
    # url = value[env]['url']
    # token = value[env]['token']
# logger.info("执行env环境 ==>> {}".format(env))
# logger.info("url ==>> {}".format(url))
# logger.info("token ==>> {}".format(token))
# yield url
# username = base_data["init_admin_user"]["username"]
# password = base_data["init_admin_user"]["password"]
# header = {
#     "Content-Type": "application/x-www-form-urlencoded"
# }
# payload = {
#     "username": username,
#     "password": password
# }
# loginInfo = user.login(data=payload, headers=header)
# step_login(username, password)
# yield loginInfo.json()
#
#
# @pytest.fixture(scope="function")
# def insert_delete_user():
#     """删除用户前，先在数据库插入一条用户数据"""
#     insert_sql = base_data["init_sql"]["insert_delete_user"][0]
#     db.execute_db(insert_sql)
#     step_first()
#     logger.info("删除用户操作：插入新用户--准备用于删除用户")
#     logger.info("执行前置SQL：{}".format(insert_sql))
#     yield
#     # 因为有些情况是不给删除管理员用户的，这种情况需要手动清理上面插入的数据
#     del_sql = base_data["init_sql"]["insert_delete_user"][1]
#     db.execute_db(del_sql)
#     step_last()
#     logger.info("删除用户操作：手工清理处理失败的数据")
#     logger.info("执行后置SQL：{}".format(del_sql))
#
#
# @pytest.fixture(scope="function")
# def delete_register_user():
#     """注册用户前，先删除数据，用例执行之后，再次删除以清理数据"""
#     del_sql = base_data["init_sql"]["delete_register_user"]
#     db.execute_db(del_sql)
#     step_first()
#     logger.info("注册用户操作：清理用户--准备注册新用户")
#     logger.info("执行前置SQL：{}".format(del_sql))
#     yield
#     db.execute_db(del_sql)
#     step_last()
#     logger.info("注册用户操作：删除注册的用户")
#     logger.info("执行后置SQL：{}".format(del_sql))
#
#
# @pytest.fixture(scope="function")
# def update_user_telephone():
#     """修改用户前，因为手机号唯一，为了使用例重复执行，每次需要先修改手机号，再执行用例"""
#     update_sql = base_data["init_sql"]["update_user_telephone"]
#     db.execute_db(update_sql)
#     step_first()
#     logger.info("修改用户操作：手工修改用户的手机号，以便用例重复执行")
#     logger.info("执行SQL：{}".format(update_sql))
