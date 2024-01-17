import time
import unittest
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.options.android import UiAutomator2Options

class LoginPage:

    textbox_email_xpath = "//android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText"
    textbox_pw_xpath = """//android.widget.EditText[@resource-id="RNE__Input__text-input"]"""
    checkbox_agreement_xpath = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
    button_login_xpath = """//android.widget.TextView[@text="Log In"]"""


    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)
        time.sleep(0.5)

    def setPW(self, pw):
        self.driver.find_element(By.XPATH, self.textbox_pw_xpath).send_keys(pw)
        time.sleep(0.5)

    def tapAgrement(self):
        self.driver.find_element(By.XPATH, self.checkbox_agreement_xpath).click()
        time.sleep(0.5)

    def tapLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()