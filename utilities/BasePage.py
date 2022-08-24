import inspect
import logging
import time
from imghdr import tests

import pytest
from _pytest import reports
from py import log
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup", "params")
class BasePage:
    def wait_presence(self, path):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(path))

    def wait_clickable(self, path):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(path))

    def message_logging(self, message):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logfile.log")
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.info(message)

    def waiting_until_item_enabled(self, item, time_out=30, interval_unit=0.5):
        end_time = time.time() + time_out
        self.message_logging(f"{item} : is Waiting for Enable")
        while time.time() < end_time and not item.is_enabled():
            time.sleep(interval_unit)

        if time.time() > end_time:
            log.debug(f"{item} : is not enable error")
            raise TimeoutError()
