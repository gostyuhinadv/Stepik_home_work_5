link = "http://selenium1py.pythonanywhere.com/"


def test_register(browser):
    browser.get(link)
    browser.find_element_by_css_selector('#login_link').click()
    browser.find_element_by_css_selector('[name="registration-email"]').send_keys("ae1piinnkxjg@ya.ru")
    browser.find_element_by_css_selector('[name="registration-password1"]').send_keys("sjuekju1432l")
    browser.find_element_by_css_selector('[name="registration-password2"]').send_keys("sjuekju1432l")
    browser.find_element_by_css_selector('[name="registration_submit"]').click()
    greeting = browser.find_element_by_css_selector(".alertinner.wicon")
    assert greeting.text == "Thanks for registering!" , "greeting not found!"