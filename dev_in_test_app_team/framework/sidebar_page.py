from .login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy

class SidebarPage(LoginPage):
    HELP_BUTTON_ID = 'com.ajaxsystems:id/help'
    REPORT_A_PROBLEM_BUTTON_ID = 'com.ajaxsystems:id/logs'
    VIDEO_SURVEILLANCE_BUTTON_ID = 'com.ajaxsystems:id/camera'
    ADD_HUB_BUTTON_CLASS_NAME = 'android.widget.Button'

    def verify_sidebar_elements(self):
        elements = [
            (AppiumBy.ID, self.APP_SETTINGS_BUTTON_ID),
            (AppiumBy.ID, self.HELP_BUTTON_ID),
            (AppiumBy.ID, self.REPORT_A_PROBLEM_BUTTON_ID),
            (AppiumBy.ID, self.VIDEO_SURVEILLANCE_BUTTON_ID),
            (AppiumBy.CLASS_NAME, self.ADD_HUB_BUTTON_CLASS_NAME)
        ]

        for by, value in elements:
            try:
                self.find_element(by, value)
            except NoSuchElementException:
                # You can log in here
                print(f"Item not found: {value}")
                return False
        return True
