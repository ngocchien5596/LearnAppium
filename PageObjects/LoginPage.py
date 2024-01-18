import time
import unittest
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.options.android import UiAutomator2Options

class LoginPage:

    textbox_email_xpath = "//android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText"
    textbox_pw_xpath = """//android.widget.EditText[@resource-id="RNE__Input__text-input"]"""
    checkbox_agreement_xpath = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
    checkbox_agreement_xpath1 = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
    button_login_xpath = """//android.widget.TextView[@text="Log In"]"""
    icon_reset_xpath = """//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"""
    label_email_xpath = """//android.widget.TextView[@text="Email"]"""
    label_pw_xpath = """//android.widget.TextView[@text="Password"]"""
    button_forgotPW_xpath = """//android.widget.TextView[@text="Forgot your password?"]"""
    label_agreement_xpath = """//android.widget.TextView[@text="By using Reset, you agree to our Term of Use, including the arbitration agreement and class action waiver, and acknowledge you have read our Privacy Policy and our Health Checklist."]"""
    label_emailErrorMessage_xpath = """//android.widget.TextView[@text="Please input your email"]"""
    label_pwErrorMessage_xpath = """//android.widget.TextView[@text="Please input your password"]"""
    label_invalidEmailPW_xpath = """//android.widget.TextView[@text="Invalid Email or Password"]"""
    button_skip_xpath = """//android.widget.TextView[@text="Skip"]"""
    label_loggedReset_xpath = """//android.widget.TextView[@text="Reset"]"""

    def __init__(self, driver):
            self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)
        time.sleep(0.5)
        self.driver.hide_keyboard()
        time.sleep(0.5)

    def setPW(self, pw):
        self.driver.find_element(By.XPATH, self.textbox_pw_xpath).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.textbox_pw_xpath).send_keys(pw)
        time.sleep(0.5)
        self.driver.hide_keyboard()
        time.sleep(0.5)

    def tapAgreement(self):
        self.driver.find_element(By.XPATH, self.checkbox_agreement_xpath).click()
        time.sleep(0.5)
    def tapAgreement1(self):
        self.driver.find_element(By.XPATH, self.checkbox_agreement_xpath1).click()
        time.sleep(0.5)

    def tapLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        time.sleep(5)