import time

import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestCases.conftest import appID


class TestLogin:

    email = "fevex98244@weirby.com"
    pwd = "Aa@123123"
    emptyString = ""
    wrongEmail = "abc@gmail.com"
    wrongPw = "123123"

    # Login_01: Check all components are displayed in Login screen
    def test_Login_01(self, setup):

        self.driver = setup
        time.sleep(3)

        list_status = []

        # Check Reset icon
        if LoginPage.icon_reset_xpath:
            list_status.append("Pass")
        else:
            list_status.append("Fail")

        # Check Email label
        if LoginPage.label_email_xpath:
            list_status.append("Pass")
        else:
            list_status.append("Fail")

        # Check Email textbox input field
        if LoginPage.textbox_email_xpath:
            list_status.append("Pass")
        else:
            list_status.append("Fail")

        # Check Password label
        if LoginPage.label_pw_xpath:
            list_status.append("Pass")
        else:
            list_status.append("Fail")

        # Check Password textbox input field
        if LoginPage.textbox_pw_xpath:
            list_status.append("Pass")
        else:
            list_status.append("Fail")

        # Check Forgot Password button
        if LoginPage.button_forgotPW_xpath:
            list_status.append("Pass")
        else:
            list_status.append("Fail")

        # Check Agreement checkbox
        if LoginPage.checkbox_agreement_xpath:
            list_status.append("Pass")
        else:
            list_status.append("Fail")

        # Check Agreement content
        if LoginPage.label_agreement_xpath:
            list_status.append("Pass")
        else:
            list_status.append("Fail")

        # Check Login button
        if LoginPage.button_login_xpath:
            list_status.append("Pass")
        else:
            list_status.append("Fail")

        if "Fail" not in list_status:
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False

    # Login_02: Check if do not fill both email and password
    def test_Login_02(self, setup):

        self.driver = setup
        time.sleep(1)

        list_status = []

        self.lp = LoginPage(self.driver)

        self.lp.tapAgrement()

        self.lp.tapLogin()

        error1 = self.driver.find_element(By.XPATH, LoginPage.label_emailErrorMessage_xpath)
        error2 = self.driver.find_element(By.XPATH, LoginPage.label_pwErrorMessage_xpath)

        if error1.is_displayed() and error2.is_displayed():
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False

    # Login_03: Check if do not fill both email and password
    @pytest.mark.sanity
    def test_Login_03(self, setup):

        self.driver = setup
        time.sleep(1)

        list_status = []

        self.lp = LoginPage(self.driver)

        self.lp.setEmail(self.email)

        self.lp.tapAgrement()

        self.lp.tapLogin()

        error2 = self.driver.find_element(By.XPATH, LoginPage.label_pwErrorMessage_xpath)

        if error2.is_displayed():
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False


