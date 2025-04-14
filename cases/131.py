from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('D:/Desktop/test.html')
driver.switch_to.frame(WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath','/html/body/iframe'))))
time.sleep(2)
# WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath','/html/body/iframe')))
driver.find_element('xpath','//*[@id="csdn-toolbar"]/div/div/div[1]/div/a/img').click()
# driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div/a/img').click()
time.sleep(2)
