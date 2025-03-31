from selenium import webdriver

def init_driver():
    driver = webdriver.Chrome()
    return driver