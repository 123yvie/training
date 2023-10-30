# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 3:32 PM
# @Author  : chenxu
# @File    : test_payment_overview.py
# **************************
import os

import allure
import pytest

from common.client_util import client_util
from common.logger import logger
from core.assert_handler import assertions
from core.render_handler import render_yaml

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

@allure.step("步骤1 ==>> 获取sicco-概览信息")
def step_1():
    logger.info("步骤1 ==>> 获取sicco-概览信息")


@allure.epic("Payment")
@allure.feature("F&L Payment Management - RT 模块")
@pytest.mark.usefixtures('init_fixture')       #获取token
class TestPaymentOverview:
    @allure.story('test_overview_list接口')
    @pytest.mark.parametrize("case_data", render_yaml(os.path.join(BASE_PATH, "payment", 'test_overview_list.yaml')))     #把yaml文件的参数赋值给case_data
    # @allure.title(case_data)
    def test_overview_list(self, case_data, init_fixture):
        # 设置用例名称
        allure.dynamic.title(case_data['name'])
        step_1()
        result = client_util.send_request(case_data, token=init_fixture)
        assertions.run(result, case_data['validate'])
