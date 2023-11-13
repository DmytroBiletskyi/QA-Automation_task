import pytest

from dev_in_test_app_team.framework.sidebar_page import SidebarPage


@pytest.fixture(scope='function')
def sidebar_fixture(driver):
    yield SidebarPage(driver)