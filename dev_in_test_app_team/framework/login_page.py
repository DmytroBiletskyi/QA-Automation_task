from .page import Page
from appium.webdriver.common.appiumby import AppiumBy
import time


class LoginPage(Page):
    EMAIL_XPATH = '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]'
    PASSWORD_XPATH = '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]'
    FIRST_LOGIN_BUTTON_XPATH = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button'
    SECOND_LOGIN_BUTTON_XPATH = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View/android.widget.Button'
    ALLOW_NOTIFICATIONS_BUTTON_ID = 'com.android.permissioncontroller:id/permission_allow_button'
    SIDE_BARE_ID = 'com.ajaxsystems:id/menuDrawer'
    APP_SETTINGS_BUTTON_ID = 'com.ajaxsystems:id/settings'
    SIGN_OUT_BUTTON_XPATH = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[6]/android.view.View/android.view.View[1]'

    def accept_notifications(self):
        try:
            self.click_element(AppiumBy.ID, self.ALLOW_NOTIFICATIONS_BUTTON_ID)
        except Exception:
            print('The notification has already been accepted.')

    def enter_email(self, email):
        self.enter_text(AppiumBy.XPATH, self.EMAIL_XPATH, email)

    def enter_password(self, password):
        self.enter_text(AppiumBy.XPATH, self.PASSWORD_XPATH, password)

    def click_first_login_button(self):
        self.click_element(AppiumBy.XPATH, self.FIRST_LOGIN_BUTTON_XPATH)

    def click_second_login_button(self):
        self.click_element(AppiumBy.XPATH, self.SECOND_LOGIN_BUTTON_XPATH)

    def is_logged_in(self):
        return len(self.driver.find_elements(AppiumBy.ID, self.SIDE_BARE_ID)) > 0

    def click_side_bar_button(self):
        self.click_element(AppiumBy.ID, self.SIDE_BARE_ID)

    def click_app_settings_button(self):
        self.click_element(AppiumBy.ID, self.APP_SETTINGS_BUTTON_ID)

    def click_sign_out_button(self):
        self.click_element(AppiumBy.XPATH, self.SIGN_OUT_BUTTON_XPATH)

    def login(self, email, password):
        self.click_first_login_button()
        self.enter_email(email)
        self.enter_password(password)
        self.click_second_login_button()
        time.sleep(5)  # better use WebDriverWait
