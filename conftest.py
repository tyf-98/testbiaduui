# conftest.py
import datetime
import os


def pytest_configure(config):
    route = os.path.abspath('..')
    if config.option.htmlpath:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        # config.option.htmlpath = rf"F:/testbaiduui/reports/report_{timestamp}.html"
        config.option.htmlpath = rf"{route}\reports\report_{timestamp}.html"