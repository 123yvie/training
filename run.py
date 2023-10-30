import os
import time

import pytest

if __name__ == '__main__':
    pytest.main()
    # 睡眠两秒 生成allure报告
    time.sleep(2)
    os.system("allure generate ./temps -o ./reports --clean")
