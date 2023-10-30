# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 3:32 PM
# @Author  : chenxu
# @File    : assert_handler.py (封装Assert方法)
# **************************
import json

from common.logger import logger


class AssertHandler:

    def __init__(self):
        self.log = logger

    # 验证response状态码
    def assert_code(self, code, expected_code):
        try:
            assert code == expected_code
            logger.info("code ==>> 预期结果：{}， 实际结果：{}".format(expected_code, code))
            return True
        except:
            self.log.error("code状态码错误, 预期结果: %s, 实际结果: %s " % (expected_code, code))
            raise

    # 验证response body中任意属性的值
    def assert_body(self, body, body_msg, expected_msg):
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except:
            self.log.error(
                "Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            raise

    # 验证response body中是否包含预期字符串
    def assert_in_text(self, body, expected_msg):
        try:
            if type(body) == dict:
                key = [key for key in body.keys()]
                assert expected_msg in key
            else:
                text = json.dumps(body, ensure_ascii=False)
                assert expected_msg in text
            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            raise

    # 验证response body中是否等于预期字符串
    def assert_msg(self, msg, expected_msg):
        try:
            assert msg == expected_msg
            logger.info("msg ==>> 预期结果: {}， 实际结果: {}".format(expected_msg, msg))
            return True
        except:
            self.log.error("msg信息错误,  预期结果: %s, 实际结果: %s" % (expected_msg, msg))
            raise

    # 验证response body响应时间小于预期最大响应时间,单位：毫秒
    def assert_time(self, time, expected_time):
        try:
            if expected_time != 0:
                assert time < expected_time
            return True

        except:
            self.log.error("time超时错误,  预期结果: %s, 实际结果: %s" % (expected_time, time))
            raise

    def run(self, result, expect):
        for key, value in expect.items():
            if key == "code":
                code = result.code
                self.assert_code(int(code), value)
            elif key == "msg":
                msg = result.msg
                self.assert_msg(msg, value)
            # elif key == "data":
            #     data = result.data
            #     for data_key, data_value in value.items():
            #         self.assert_body(data, data_key, data_value)
            elif key == "time":
                time = result.time
                self.assert_time(time, value)

    def second_to_millisecond(second):
        f = int(float(second) * 1000)
        return f


assertions = AssertHandler()
