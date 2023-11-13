import pytest


@pytest.mark.parametrize("email, password", [
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password")
])
def test_sidebar(sidebar_fixture, email, password):
    # initialize SidebarPage
    sidebar_page = sidebar_fixture
    sidebar_page.accept_notifications()
    sidebar_page.login(email, password)

    # Opening SideBar before checking elements
    sidebar_page.click_side_bar_button()

    # Performing a check
    assert sidebar_page.verify_sidebar_elements(), "Not all SideBar elements are present"
