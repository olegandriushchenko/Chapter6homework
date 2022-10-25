from selenium.webdriver.support.color import Color

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

from BrainBucketTest.drivers.browser import Browser
from BrainBucketTest.drivers.UIElement import UIElement as Element
from BrainBucketTest.drivers.dropdown import Dropdown

from BrainBucketTest.components.header import Header
from BrainBucketTest.components.right_menu import RightMenu
from BrainBucketTest.components.footer import Footer
from BrainBucketTest.pages.login_page import LoginPage
from BrainBucketTest.pages.registration_page import RegistrationPage

URL = "https://cleveronly.com/brainbucket/index.php?route=common/home"


def test_header_1():
    browser = Browser(URL)

    logo = Header(browser)
    logo.verify_logo_is_visible()

    currency = Header(browser)
    currency.change_currency()

    call = Header(browser)
    call.contact_us()


def test_login_through_dropdown():
    browser = Browser(URL)
    driver = browser.get_driver()

    login1 = LoginPage(browser)

    login = Header(browser)
    login.open_login_page()
    login_option = Element(browser, "xpath", "//div[@id='content']/div/div/div/h2")
    assert "New Customer" == login_option.get_text()

    login1.email_input_click("olegandriushchenko95@gmail.com")

    login1.password_input_click("12345678")

    login1.login_button_click()

    continue_btn = driver.find_element("xpath", "//div[@id='content']/div/div/div/a")
    background_color = continue_btn.value_of_css_property('background-color')
    converted_background_color = Color.from_string(background_color)
    assert converted_background_color.rgb == 'rgb(34, 154, 200)'
    continue_btn.click()


def test_registration_through_dropdown():
    browser = Browser(URL)
    driver = browser.get_driver()

    registration = LoginPage(browser)
    registration.open_registration_from_account_dropdown()

    registration1 = RegistrationPage(browser)

    firstname_field = Element(browser, "xpath", "//fieldset/div[2]")
    firstname_field_class = firstname_field.get_attribute("class")
    assert "required" in firstname_field_class
    registration1.enter_first_name("Oleg")

    lastname_field = Element(browser, "xpath", "//fieldset[@id='account']/div[3]")
    lastname_field_class = lastname_field.get_attribute("class")
    assert "required" in lastname_field_class
    registration1.enter_last_name("Andriushchenko")

    email_field = Element(browser, "xpath", "//fieldset[@id='account']/div[4]")
    email_field_class = email_field.get_attribute("class")
    assert "required" in email_field_class
    registration1.enter_email("olegandriushchenko95@gmail.com")

    telephone_field = Element(browser, "xpath", "//fieldset[@id='account']/div[5]")
    telephone_field_class = telephone_field.get_attribute("class")
    assert "required" in telephone_field_class
    registration1.enter_telephone("1234567890")

    registration1.enter_fax("1234567890")

    registration1.enter_company("BBC")

    address_field = Element(browser, "xpath", "//fieldset[@id='address']/div[2]")
    address_field_class = address_field.get_attribute("class")
    assert "required" in address_field_class
    registration1.enter_first_line_address("123 Michigan Ave")

    city_field = Element(browser, "xpath", "//fieldset[@id='address']/div[4]")
    city_field_class = city_field.get_attribute("class")
    assert "required" in city_field_class
    registration1.enter_city("Chicago")

    registration1.enter_postcode("12345")

    registration1.select_state("Illinois")

    registration1.enter_password("12345678")
    registration1.confirm_password("12345678")

    continue_btn = driver.find_element("xpath", "//input[@value='Continue']")
    background_color2 = continue_btn.value_of_css_property("background-color")
    converted_background_color2 = Color.from_string(background_color2)
    assert converted_background_color2.rgb == 'rgb(34, 154, 200)'
    continue_btn.click()

    registration1.subscribe_to_newsletters()
    registration1.agree_to_privacy_policy()

    # right menu check
    right_menu1 = RightMenu(browser)
    right_menu1.click_login()

    right_menu2 = RightMenu(browser)
    right_menu2.click_registration()

    right_menu3 = RightMenu(browser)
    right_menu3.click_forgotten_btn()

    right_menu4 = RightMenu(browser)
    right_menu4.click_my_account()

    right_menu5 = RightMenu(browser)
    right_menu5.click_my_address()

    right_menu6 = RightMenu(browser)
    right_menu6.click_wish_list()

    right_menu7 = RightMenu(browser)
    right_menu7.click_order_history()

    right_menu8 = RightMenu(browser)
    right_menu8.click_downloads()

    right_menu9 = RightMenu(browser)
    right_menu9.click_recurring_payments()

    right_menu10 = RightMenu(browser)
    right_menu10.click_reward_points()

    right_menu11 = RightMenu(browser)
    right_menu11.click_returns()

    right_menu12 = RightMenu(browser)
    right_menu12.click_transactions()

    right_menu13 = RightMenu(browser)
    right_menu13.click_newsletter()


def test_header_2():
    browser = Browser(URL)

    wishlist = Header(browser)
    wishlist.open_wishlist()

    shopping = Header(browser)
    shopping.shopping_list()

    search = Header(browser)
    search.search_for()


def test_footer1():
    browser = Browser(URL)

    about_us = Footer(browser)
    about_us.about_us_click()

    delivery_information = Footer(browser)
    delivery_information.delivery_information_click()

    privacy_policy = Footer(browser)
    privacy_policy.privacy_policy_click()

    terms_and_conditions = Footer(browser)
    terms_and_conditions.delivery_information_click()

    contact_us = Footer(browser)
    contact_us.contact_us_click()

    returns = Footer(browser)
    returns.returns_click()

    site_map = Footer(browser)
    site_map.site_map_click()

    brands = Footer(browser)
    brands.brands_click()

    gift_certification = Footer(browser)
    gift_certification.gift_certification_click()

    affiliates = Footer(browser)
    affiliates.affiliates_click()

    specials = Footer(browser)
    specials.specials_click()

    my_account = Footer(browser)
    my_account.my_account_click()

    order_history = Footer(browser)
    order_history.order_history_click()

    wish_list = Footer(browser)
    wish_list.wish_list_click()

    newsletter = Footer(browser)
    newsletter.newsletter_click()


if __name__ == "__main__":
    test_header_1()
    test_login_through_dropdown()
    test_registration_through_dropdown()
    test_header_2()
    test_footer1()

# browser.shutdown()


