
import os
import allure
import pytest

from common.client_util import client_util
from common.logger import logger
from core.assert_handler import assertions
from core.render_handler import render_yaml

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


@allure.step("步骤2 ==>> 上传附件")
def step_1():
    logger.info("步骤1 ==>> 经销商上传附件")


@allure.epic("Tips_Case")
@allure.feature("Tips_Case - case-dict")
@pytest.mark.usefixtures('init_fixture')  # 获取token
class TestPaymentOverview:
    @allure.story('search-types')
    @pytest.mark.parametrize("case_data", render_yaml(os.path.join(BASE_PATH, 'tips', 'test_tips_upload_attachment.yaml'))) #把yaml文件的参数赋值给case_data
    # @allure.title(case_data)
    def test_tips_create_case(self, case_data, init_fixture):
        # 设置用例名称
        allure.dynamic.title(case_data['name'])
        step_1()
        result = client_util.send_request(case_data, token=init_fixture)
        assertions.run(result, case_data['validate'])


