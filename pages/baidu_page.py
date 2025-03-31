from bases.base_waitfunc import *
from selenium.webdriver.common.by import By
from bases.base_data import *


class baidu_page(BaseWaitFunctions):
    locators = excel_to_locator_dict(r"F:\testbaiduui\datas\baidu.xlsx")
    butten_baiduyixia = 'By.ID','su'

    input_baiduyixia = 'By.ID','kw'

    PYTHON = 'python'

    PYTHON_PATH = By.LINK_TEXT,'Welcome to Python.org'


    def click_baiduyixia(self):
        # self.find_element_with_wait(self.butten_baiduyixia).click()
        # print(locators['butten_baiduyixia'])
        self.find_element_with_wait(self.locators['butten_baiduyixia'][0],self.locators['butten_baiduyixia'][1]).click()

    def input_python(self):
        self.find_element_with_wait(self.locators['input_baiduyixia'][0],self.locators['input_baiduyixia'][1]).send_keys(self.PYTHON)

    def python_official_website_text(self):
        msg = self.find_element_with_wait(self.locators['PYTHON_PATH'][0],self.locators['PYTHON_PATH'][1]).text
        return msg