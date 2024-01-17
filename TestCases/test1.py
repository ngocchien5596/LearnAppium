import unittest
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.options.android import UiAutomator2Options

class AppiumTest(unittest.TestCase):
    def test_example(self):

        # desired_caps = {
        #     'platformName': 'Android',  # or 'iOS'
        #     'platformVersion': '13',
        #     'deviceName': 'RF8R60PF4NL',
        #     'appPackage': 'com.betterwell.reset',
        #     'appActivity': 'com.betterwell.reset.MainActivity',
        #     'automationName': 'UiAutomator2',  # or 'XCUITest' for iOS
        #     'app': '/Users/ngocchien/Downloads/app-release.apk'
        # }

        desired_caps = {
            'platformName': 'Android',  # or 'iOS'
            'platformVersion': '13',
            'deviceName': 'RF8R60PF4NL',
            'appPackage': 'com.google.android.calculator',
            'appActivity': 'com.android.calculator2.Calculator',
            'automationName': 'UiAutomator2',  # or 'XCUITest' for iOS
            'app': '/Users/ngocchien/Downloads/Calc.apk'
        }

        # Appium server URL
        appium_url = 'http://localhost:4723/wd/hub'
        options = UiAutomator2Options().load_capabilities(desired_caps)

        # Initialize the Appium driver
        self.driver = webdriver.Remote(appium_url, options=options)

        self.driver.find_element(By.ID, "com.google.android.calculator:id/digit_9").click()
        self.driver.find_element(By.ID, "com.google.android.calculator:id/op_add").click()
        self.driver.find_element(By.ID, "com.google.android.calculator:id/digit_9").click()
        self.driver.find_element(By.ID, "com.google.android.calculator:id/eq").click()

        result = self.driver.find_element(By.ID, "com.google.android.calculator:id/result_final").text
        print(result)

        if result == "18":
            # self.driver.close()
            assert True
            print("Pass")
        else:
            # self.driver.close()
            print("Fail")
            assert False






