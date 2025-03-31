#coding=utf-8
#这个公用是存放page中的所有Super_find_wait_click方法
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# class BaseWaitFunctions:#定义一个父类
#     def __init__(self,driver):
#         self.driver=driver
#     def find_element_with_wait(self, element):
#         # page中的所有方法都在Super_find_wait_click中。把这个方法封装为智能等待即可。
#         return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(element[0], element[1]))



from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
class BaseWaitFunctions:
    """封装通用显式等待方法，提升代码复用性"""

    def __init__(self, driver, timeout=10):
        """
        初始化基类
        :param driver: WebDriver实例
        :param timeout: 默认超时时间（秒）
        """
        self.driver = driver
        self.timeout = timeout

    def find_element_with_wait(self, locator_type,locator_value, timeout=None):
        """
        等待元素存在并返回
        :param locator_type: 定位类型（如 'id', 'xpath'）
        :param locator_value: 定位值
        :param timeout: 可选，覆盖默认超时时间
        :return: WebElement
        """
        return self._wait_for_element(
            (locator_type,locator_value),
            EC.presence_of_element_located,
            timeout
        )

    def wait_for_element_visible(self,locator_type,locator_value, timeout=None):
        """
        等待元素可见并返回
        """
        return self._wait_for_element(
            (locator_type,locator_value),
            EC.visibility_of_element_located,
            timeout
        )

    def _wait_for_element(self, locator, condition, timeout=None):
        """
        内部通用等待方法
        """
        wait_timeout = timeout or self.timeout
        return WebDriverWait(self.driver, wait_timeout).until(condition(locator))