

from common.logger import logger
from core.config_handler import config
from core.replace_handler import replace_json_param
from core.rest_client import RestClient
from core.result_base import ResultBase

"""
Client Util
"""
# 获取api前缀地址
api_root_url = config.get_env_base_url()


class ClientUtil(RestClient):

    def __init__(self, api_root_url):
        super(ClientUtil, self).__init__(api_root_url)

    def send_request(self, case_data, token, is_download=False, **kwargs):
        # 获取请求地址
        url = case_data['request']['url']
        # 获取请求方法转大写
        method = str(case_data['request']['method']).upper()
        # 获取json请求参数
        json_param = replace_json_param(case_data['request']['json'])
        res = self.request(url, method, json=json_param, headers={"Authorization": token}, **kwargs)
        # if 'data' in case_data['request']:  # jiaqi: data judge
        #     json_data = replace_json_param(case_data['request']['data'])
        #     files = case_data['request']['files']
        #     res = self.request(url, method, json=json_param, headers={"Authorization": token}, data=json_data,
        #                        files=files, **kwargs)
        # else:
        #     res = self.request(url, method, json=json_param, headers={"Authorization": token}, **kwargs)
        if is_download:
            return res
        else:
            result = ResultBase(res)
            logger.info("{} ==>> 返回结果 ==>> {}".format(case_data['name'], result.response.text))
            return result


client_util = ClientUtil(api_root_url)
