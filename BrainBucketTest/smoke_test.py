from selenium.webdriver.support.color import Color

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

from BrainBucketTest.drivers.browser import Browser
from BrainBucketTest.drivers.UIElement import UIElement as Element
from BrainBucketTest.drivers.dropdown import Dropdown

from BrainBucketTest.components.header import Header


URL = "https://cleveronly.com/brainbucket/index.php?route=common/home"


def test_header_1():
    browser = Browser(URL)
    driver = browser.get_driver()

    logo = Header(browser)
    logo.verify_logo_is_visible()

    currency = Header(browser)
    currency.change_currency()

    call = Header(browser)
    call.contact_us()


def test_login_through_dropdown():
    browser = Browser(URL)
    driver = browser.get_driver()
    login = Header(browser)
    login.open_login_page()
    login_option = Element(browser, "xpath", "//div[@id='content']/div/div/div/h2")
    assert "New Customer" == login_option.get_text()

    continue_btn = driver.find_element("xpath", "//div[@id='content']/div/div/div/a")
    background_color = continue_btn.value_of_css_property('background-color')
    converted_background_color = Color.from_string(background_color)
    assert converted_background_color.rgb == 'rgb(34, 154, 200)'
    continue_btn.click()


def test_registration_through_dropdown():
    browser = Browser(URL)
    driver = browser.get_driver()

    registration = Header(browser)
    registration.open_registration_form()

    firstname_field = Element(browser, "xpath", "//fieldset/div[2]")
    firstname_field_class = firstname_field.get_attribute("class")
    assert "required" in firstname_field_class
    firstname_input = driver.find_element("id", "input-firstname")
    firstname_input.clear()
    firstname_input.send_keys("Oleg")

    lastname_field = Element(browser, "xpath", "//fieldset[@id='account']/div[3]")
    lastname_field_class = lastname_field.get_attribute("class")
    assert "required" in lastname_field_class
    lastname_input = driver.find_element("id", "input-lastname")
    lastname_input.clear()
    lastname_input.send_keys("Andriushchenko")

    email_field = Element(browser, "xpath", "//fieldset[@id='account']/div[4]")
    email_field_class = email_field.get_attribute("class")
    assert "required" in email_field_class
    email_input = driver.find_element("id", "input-email")
    email_input.clear()
    email_input.send_keys("oleg@gmail.com")

    telephone_field = Element(browser, "xpath", "//fieldset[@id='account']/div[5]")
    telephone_field_class = telephone_field.get_attribute("class")
    assert "required" in telephone_field_class
    telephone_input = driver.find_element("id", "input-telephone")
    telephone_input.clear()
    telephone_input.send_keys("1234567890")

    address_field = Element(browser, "xpath", "//fieldset[@id='address']/div[2]")
    address_field_class = address_field.get_attribute("class")
    assert "required" in address_field_class
    address_input = driver.find_element("id", "input-address-1")
    address_input.clear()
    address_input.send_keys("123 Michigan Ave")

    city_field = Element(browser, "xpath", "//fieldset[@id='address']/div[4]")
    city_field_class = city_field.get_attribute("class")
    assert "required" in city_field_class
    city_input = driver.find_element("id", "input-city")
    city_input.clear()
    city_input.send_keys("Chicago")

    password_field = Element(browser, "xpath", "//input[@id='input-password']")
    password_input = driver.find_element("id", "input-password")
    password_input.clear()
    password_input.send_keys("12345678")
    password_field.click()

    continue_btn = driver.find_element("xpath", "//input[@value='Continue']")
    background_color2 = continue_btn.value_of_css_property("background-color")
    converted_background_color2 = Color.from_string(background_color2)
    assert converted_background_color2.rgb == 'rgb(34, 154, 200)'
    continue_btn.click()

    state_dropdown = driver.find_element("id", "input-zone")
    state_dropdown_select = Select(state_dropdown)
    state_dropdown_select.select_by_value("3635")

    Dropdown(browser, "id", "input-country").select_by_text("--- Please Select ---")
    Dropdown(browser, "id", "input-zone").select_by_text("--- Please Select ---")

    subscribe_btn = Element(browser, "xpath", "//div[@id='content']/form/fieldset[4]/div/div/label/input")
    subscribe_btn.click()

    privacy_policy_btn = Element(browser, "xpath", "//div[@id='content']/form/div/div/input")
    privacy_policy_btn.click()


def test_header_2():
    browser = Browser(URL)
    driver = browser.get_driver()

    wishlist = Header(browser)
    wishlist.open_wishlist()

    shopping = Header(browser)
    shopping.shopping_list()

    search = Header(browser)
    search.search_for()


if __name__ == "__main__":
    test_header_1()
    test_login_through_dropdown()
    test_registration_through_dropdown()
    test_header_2()


# browser.shutdown()


