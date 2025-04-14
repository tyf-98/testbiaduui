import pytest
from bases.base_driver import init_driver
from pages.test_page import *
import time
class Test_baidu:
    def setup_class(self):
        self.driver = init_driver()
        self.test=test_page(self.driver)
        self.driver.maximize_window()
        self.driver.get('D:/Desktop/test.html')

    def teardown_class(self):
        self.driver.quit()

    def test_search_python(self):
        self.driver.switch_to.frame(self.test.kuangjia())
        # self.driver.switch_to.frame('CSDN_info')
        self.test.click_zhuye()
        print('----成功--')
        time.sleep(2)
        # msg = self.baidu.python_official_website_text()
        # assert 'Python' in msg



if __name__ == '__main__':
    pytest.main(['-s','test_test.py'])  # 调用pytest的main函数执行测试