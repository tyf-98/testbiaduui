from bases.base_waitfunc import *
from selenium.webdriver.common.by import By
from bases.base_data import *


class test_page(BaseWaitFunctions):

    a = 'By.XPATH','/html/body/iframe'

    b = 'By.XPATH','//*[@id="csdn-toolbar"]/div/div/div[1]/div/a/img'

    c = 'python'

    PYTHON_PATH = By.LINK_TEXT,'Welcome to Python.org'


    def kuangjia(self):
        # self.find_element_with_wait(self.butten_baiduyixia).click()
        # print(locators['butten_baiduyixia'])
        # return self.find_element_with_wait(self.a[0],self.a[1])
        return self.find_element_with_wait('xpath','/html/body/iframe')

    def click_zhuye(self):
        self.find_element_with_wait('xpath','//*[@id="csdn-toolbar"]/div/div/div[1]/div/a/img').click()

    # def python_official_website_text(self):
    #     msg = self.find_element_with_wait(self.locators['PYTHON_PATH'][0],self.locators['PYTHON_PATH'][1]).text
    #     return msg