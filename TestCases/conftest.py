import pytest
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.options.android import UiAutomator2Options
appID = "com.betterwell.reset"
@pytest.fixture
def setup() -> None:
    appium_url = 'http://localhost:4723/wd/hub'
    desired_caps = {
        'platformName': 'Android',  # or 'iOS'
        'platformVersion': '13',
        'deviceName': 'RF8R60PF4NL',
        'appPackage': 'com.betterwell.reset',
        'appActivity': 'com.betterwell.reset.MainActivity',
        'automationName': 'UiAutomator2',  # or 'XCUITest' for iOS
        'app': '/Users/ngocchien/Downloads/app-release.apk'
    }
    options = UiAutomator2Options().load_capabilities(desired_caps)

    # Initialize the Appium driver
    driver = webdriver.Remote(appium_url, options=options)
    return driver


def teardown(self) -> None:
    if self.driver:
        self.driver.terminate_app(self.appID)