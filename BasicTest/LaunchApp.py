#
#
# import unittest
# import allure
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# class TestLogin(unittest.TestCase):
#
#     def setUp(self):
#         # Appium server details
#         url = 'http://127.0.0.1:4723/wd/hub'
#
#         # Appium capabilities
#         desired_caps = {
#             'platformName': 'Android',
#             'automationName': 'uiautomator2',
#             'appPackage': 'com.logan4509.ups',
#             'appActivity': 'com.logan4509.ups.MainActivity',
#             'language': 'en',
#             'locale': 'US'
#         }
#
#         # Create Appium driver instance using desired_caps directly
#         self.driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(desired_caps))
#         self.driver.implicitly_wait(10)
#
#     def test_login_with_valid_credentials(self):
#         driver = self.driver
#
#         # Explicit wait for the "Continue" button
#         wait = WebDriverWait(driver, 10)
#         continue_button = wait.until(
#             EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Continue"]'))
#         )
#         continue_button.click()
#
#         # Explicit wait for the "Login" button
#         wait = WebDriverWait(driver, 15)
#         login_button = wait.until(
#             EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Login"]'))
#         )
#         login_button.click()
#
#         # Explicit wait for the email textbox
#         wait = WebDriverWait(driver, 10)
#         email_textbox = wait.until(
#             EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Enter your Email Address"]'))
#         )
#         email_textbox.send_keys("Yfatunbi@gmail.com")  # Enter a valid email address
#
#         # Explicit wait for the password textbox
#         wait = WebDriverWait(driver, 10)
#         password_textbox = wait.until(
#             EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Enter password"]'))
#         )
#         password_textbox.send_keys("Fatunbi@1")  # Enter a valid password
#
#         # Explicit wait for the "Continue" button
#         wait = WebDriverWait(driver, 10)
#         continue_button = wait.until(
#             EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Continue"]'))
#         )
#         continue_button.click()
#
#         # Add additional assertions here to verify successful login (optional)
#
#     def tearDown(self):
#         self.driver.quit()
# if __name__ == '__main__':
#    unittest.main()
#
#


import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

# 1. EXACT CAPABILITIES FROM YOUR INSPECTOR (NO CHANGES)
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Pixel6Pro"
options.app_package = "com.android.camera2"
options.app_activity = "com.android.camera.CameraLauncher"
options.automation_name = "UiAutomator2"
options.no_reset = True
options.auto_grant_permissions = True
options.udid = "emulator-5554"

# 1. Set up device capabilities
#options = UiAutomator2Options()
#options.platform_name = "Android"
#options.device_name = "Pixel6Pro"
#options.app_package = "com.google.android.apps.nexuslauncher"  # Launcher package
#options.app_activity = "com.google.android.apps.nexuslauncher.NexusLauncherActivity"  # Launcher activity
#options.automation_name = "UiAutomator2"
#options.no_reset = True
#options.udid = "emulator-5554"

# 2. Initialize driver
driver = webdriver.Remote("http://localhost:4723", options=options)


def test_click_clock_icon():
    """Simple test to click clock icon"""
    try:
        # 3. Find and click clock icon
        clock_icon = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Clock")
        clock_icon.click()
        print("Successfully clicked clock icon!")

        # Optional verification
        assert "deskclock" in driver.current_package.lower()

    finally:
        # 4. Clean up
        driver.quit()
        print("Test completed")


# 5. Run the test
if __name__ == "__main__":
    test_click_clock_icon()


