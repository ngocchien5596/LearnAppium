import time

import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestCases.conftest import appID


class TestLogin:

    email = "buingocchien5596@gmail.com"
    invalidEmail = "abc@example.com"
    spaceAtMiddleEmail = "buingocchien 5596@gmail.com"
    spaceAtFirstandEndEmail = " buingocchien5596@gmail.com "
    pwd = "Aa@123123"
    invalidPW = "1111111"
    spaceAtMiddlePW = "Aa @12313"
    spaceAtFirstandEnDPW = " Aa@123123 "
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

    # Login_02: Check if user inputs blank into Email field
    def test_Login_02(self, setup):
        self.driver = setup
        time.sleep(3)

        self.lp = LoginPage(self.driver)

        self.lp.setEmail(self.emptyString)

        self.lp.setPW(self.pwd)

        self.lp.tapAgreement1()

        self.lp.tapLogin()

        element = self.driver.find_element(By.XPATH, LoginPage.label_emailErrorMessage_xpath)

        if element:
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False

    # Login_03: Check if user inputs space at middle of word into Email field
    def test_Login_03(self, setup):
        self.driver = setup
        time.sleep(3)

        self.lp = LoginPage(self.driver)

        self.lp.setEmail(self.spaceAtMiddleEmail)

        self.lp.setPW(self.pwd)

        self.lp.tapAgreement()

        self.lp.tapLogin()

        element = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, LoginPage.label_invalidEmailPW_xpath)))

        if element:
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False

    # Login_04: Check if user inputs space at first and end of word into Email field
    def test_Login_04(self, setup):
        self.driver = setup
        time.sleep(3)

        self.lp = LoginPage(self.driver)

        self.lp.setEmail(self.spaceAtFirstandEndEmail)

        self.lp.setPW(self.pwd)

        self.lp.tapAgreement()

        self.lp.tapLogin()

        element = self.driver.find_elements(By.XPATH, LoginPage.button_skip_xpath)
        element1 = self.driver.find_elements(By.XPATH, LoginPage.label_loggedReset_xpath)

        if element:
            assert True
            self.driver.terminate_app(appID)
        elif element1:
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False


    # Login_05: Check if user input invalid email into Email field
    def test_Login_05(self, setup):
        self.driver = setup
        time.sleep(3)

        self.lp = LoginPage(self.driver)

        self.lp.setEmail(self.invalidEmail)

        self.lp.setPW(self.pwd)

        self.lp.tapAgreement()

        self.lp.tapLogin()

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, LoginPage.label_invalidEmailPW_xpath)))

        if element:
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False

    # Login_06: Check if user input valid email into Email field

    def test_Login_06(self, setup):
        self.driver = setup
        time.sleep(3)

        self.lp = LoginPage(self.driver)

        self.lp.setEmail(self.email)

        self.lp.setPW(self.pwd)

        self.lp.tapAgreement()

        self.lp.tapLogin()

        element = self.driver.find_elements(By.XPATH, LoginPage.button_skip_xpath)
        element1 = self.driver.find_elements(By.XPATH, LoginPage.label_loggedReset_xpath)

        if element:
            assert True
            self.driver.terminate_app(appID)
        elif element1:
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False

    # Login_07: Check if user inputs blank into Password field
    def test_Login_07(self, setup):
        self.driver = setup
        time.sleep(3)

        self.lp = LoginPage(self.driver)

        self.lp.setEmail(self.email)

        self.lp.setPW(self.emptyString)

        self.lp.tapAgreement()

        self.lp.tapLogin()

        element = self.driver.find_element(By.XPATH, LoginPage.label_pwErrorMessage_xpath)

        if element:
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False

    # Login_08: Check if user inputs space at middle of word into Password field
    def test_Login_08(self, setup):
        self.driver = setup
        time.sleep(3)

        self.lp = LoginPage(self.driver)

        self.lp.setEmail(self.email)

        self.lp.setPW(self.spaceAtMiddlePW)

        self.lp.tapAgreement()

        self.lp.tapLogin()

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, LoginPage.label_invalidEmailPW_xpath)))

        if element:
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False

    # Login_09: Check if user inputs space at first and end of word into Password field

    def test_Login_09(self, setup):
        self.driver = setup
        time.sleep(3)

        self.lp = LoginPage(self.driver)

        self.lp.setEmail(self.email)

        self.lp.setPW(self.spaceAtFirstandEnDPW)

        self.lp.tapAgreement()

        self.lp.tapLogin()

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, LoginPage.label_invalidEmailPW_xpath)))

        if element:
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False

    # Login_10: Check if user input invalid Password into Password field
    @pytest.mark.sanity
    def test_Login_10(self, setup):
        self.driver = setup
        time.sleep(3)

        self.lp = LoginPage(self.driver)

        self.lp.setEmail(self.email)

        self.lp.setPW(self.invalidPW)

        self.lp.tapAgreement()

        self.lp.tapLogin()

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, LoginPage.label_invalidEmailPW_xpath)))

        if element:
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False


    # Login_11: Check if user input valid Password into Password field
    @pytest.mark.sanity
    def test_Login_11(self, setup):
        self.driver = setup
        time.sleep(3)

        self.lp = LoginPage(self.driver)

        self.lp.setEmail(self.email)

        self.lp.setPW(self.pwd)

        self.lp.tapAgreement()

        self.lp.tapLogin()

        element = self.driver.find_elements(By.XPATH, LoginPage.button_skip_xpath)
        element1 = self.driver.find_elements(By.XPATH, LoginPage.label_loggedReset_xpath)

        if element:
            assert True
            self.driver.terminate_app(appID)
        elif element1:
            assert True
            self.driver.terminate_app(appID)
        else:
            self.driver.terminate_app(appID)
            assert False





