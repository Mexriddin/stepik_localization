import time


def test_is_have_add_button(browser):
    add_button = ('css selector', '.btn-add-to-basket')

    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    is_visible = browser.find_element(*add_button).is_displayed()
    time.sleep(30)
    assert is_visible, "Button add was not"
