def android_get_desired_capabilities():
    return {
        'newCommandTimeout': 500,
        'noSign': True,
        'resetKeyboard': True,
        'takesScreenshot': True,
        'udid': '771b5c2f',
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'platformVersion': '13',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
        'language': 'en',
        'locale': 'US'
}
