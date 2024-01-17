import time
import unittest
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.options.android import UiAutomator2Options

class AppiumTest(unittest.TestCase):

    appID = "com.betterwell.reset"
    def test_example(self):

        desired_caps = {
            'platformName': 'Android',  # or 'iOS'
            'platformVersion': '13',
            'deviceName': 'RF8R60PF4NL',
            'appPackage': 'com.betterwell.reset',
            'appActivity': 'com.betterwell.reset.MainActivity',
            'automationName': 'UiAutomator2',  # or 'XCUITest' for iOS
            'app': '/Users/ngocchien/Downloads/app-release.apk'
        }


        # Appium server URL
        appium_url = 'http://localhost:4723/wd/hub'
        options = UiAutomator2Options().load_capabilities(desired_caps)

        # Initialize the Appium driver
        self.driver = webdriver.Remote(appium_url, options=options)

        self.driver.find_element(By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText").send_keys("fevex98244@weirby.com")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,"""//android.widget.EditText[@resource-id="RNE__Input__text-input"]""").send_keys("Aa@123123")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, """//android.widget.TextView[@text="Log In"]""").click()
        time.sleep(5)

        resetLabel = self.driver.find_element(By.XPATH, """//android.widget.TextView[@text="Reset"]""")
        if resetLabel:
            assert True
            self.driver.terminate_app(self.appID)
        else:
            self.driver.terminate_app(self.appID)
            assert False
