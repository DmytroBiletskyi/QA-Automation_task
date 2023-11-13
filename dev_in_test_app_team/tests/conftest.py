import subprocess
import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from dev_in_test_app_team.utils.android_utils import android_get_desired_capabilities

capabilities_options = UiAutomator2Options().load_capabilities(android_get_desired_capabilities())

@pytest.fixture(scope='session')
def run_appium_server(android_udid):
    appium_path = 'C:\\Users\\Администратор\\AppData\\Roaming\\npm\\appium'
    subprocess.Popen(
        [appium_path, '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server):
    app_driver = webdriver.Remote('http://localhost:4723', options=capabilities_options)
    yield app_driver
    if app_driver:
        app_driver.quit()


@pytest.fixture(scope="session")
def android_udid():
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()

    # Extract the UDID from the result.
    devices = [line.split('\t')[0] for line in lines[1:] if line and "device" in line]

    if devices:
        return devices[0]  # Return the UDID of the first found device
    else:
        pytest.fail("No device found")
