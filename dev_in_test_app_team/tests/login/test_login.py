import logging
import pytest
import time

# Login settings
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Adding a file handler for writing logs
file_handler = logging.FileHandler('test_login_logs.log')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@pytest.mark.parametrize("email, password, is_successful", [
    ("email2@example.com", "password2", False),
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True)
])
def test_user_login(android_udid, user_login_fixture, email, password, is_successful):
    logger.info("Testing on devices with UDID: %s", android_udid)
    logger.info("Login test started for user: %s", email)

    login_page = user_login_fixture
    login_page.accept_notifications()
    logger.info("Notification accepted")

    login_page.click_first_login_button()
    logger.info("The first login button is pressed")

    login_page.enter_email(email)
    login_page.enter_password(password)
    logger.info("Login and password entered")

    login_page.click_second_login_button()
    time.sleep(6)  # better use WebDriverWait
    logger.info("Clicked to complete login")

    if is_successful:
        assert login_page.is_logged_in(), "Failed to log in with valid credentials"
        logger.info("Successful login for the user: %s", email)

        login_page.click_side_bar_button()
        login_page.click_app_settings_button()
        login_page.click_sign_out_button()
        logger.info("Logout successful")
    else:
        assert not login_page.is_logged_in(), "Login failed with incorrect credentials"
        logger.info("Login failed for user: %s", email)
        login_page.driver.back()
