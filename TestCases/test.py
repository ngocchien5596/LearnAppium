import time
import unittest
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.options.android import UiAutomator2Options
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestCases.conftest import setup

class TestLogin:

    appID = "com.betterwell.reset"
    email = "fevex98244@weirby.com"
    pwd = "Aa@123123"


    def test_example(self, setup):

        self.driver = setup

        # Login functions usage
        self.lp = LoginPage(self.driver)

        # Fill email
        self.lp.setEmail(self.email)

        # Fill password
        self.lp.setPW(self.pwd)

        # Check agreement terms
        self.lp.tapAgrement()

        # Tap login button
        self.lp.tapLogin()

        # Wait for reset label to be displayed
        resetLabel_xpath =  """//android.widget.TextView[@text="Reset"]"""
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, resetLabel_xpath)))

        if element:
            assert True
            self.driver.terminate_app(self.appID)
        else:
            self.driver.terminate_app(self.appID)
            assert False
