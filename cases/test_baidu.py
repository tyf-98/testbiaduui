import pytest
from bases.base_driver import init_driver
from pages.baidu_page import *

class Test_baidu:
    def setup_class(self):
        self.driver = init_driver()
        self.baidu=baidu_page(self.driver)
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')

    def teardown_class(self):
        self.driver.quit()

    def test_search_python(self):
        self.baidu.input_python()
        self.baidu.click_baiduyixia()
        msg = self.baidu.python_official_website_text()
        assert 'Python' in msg



if __name__ == '__main__':
    pytest.main(['-s','test_baidu.py'])  # 调用pytest的main函数执行测试