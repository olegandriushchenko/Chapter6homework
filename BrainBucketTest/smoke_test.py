import time

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
from BrainBucketTest.drivers.actions import Actions

from selenium.webdriver.common.keys import Keys

from BrainBucketTest.pages.home_page import HomePage

URL = "https://cleveronly.com/brainbucket/index.php?route=common/home"


def test_header_1():
    browser = Browser(URL)

    logo = Header(browser)
    logo.verify_logo_is_visible()

    currency = Header(browser)
    currency.change_currency()

    call = Header(browser)
    call.contact_us()

    browser.shutdown()


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

    browser.shutdown()


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

    # right menu check
    right_menu = RightMenu(browser)
    right_menu.click_login()

    right_menu.click_registration()

    right_menu.click_forgotten_btn()

    right_menu.click_my_account()

    right_menu.click_my_address()

    right_menu.click_wish_list()

    right_menu.click_order_history()

    right_menu.click_downloads()

    right_menu.click_recurring_payments()

    right_menu.click_reward_points()

    right_menu.click_returns()

    right_menu.click_transactions()

    right_menu.click_newsletter()

    browser.shutdown()


def test_header_2():
    browser = Browser(URL)

    wishlist = Header(browser)
    wishlist.open_wishlist()

    shopping = Header(browser)
    shopping.shopping_list()

    search = Header(browser)
    search.search_for()

    browser.shutdown()


def test_opening_all_desktops():
    browser = Browser(URL)
    home_page = HomePage(browser)
    home_page.show_all_desktops()

    section_title = Element(browser, "xpath", "//*[@id='content']/h2").get_text()

    assert section_title == "Desktops"


def test_opening_all_pcs():
    browser = Browser(URL)
    home_page = HomePage(browser)
    home_page.show_all_laptops()

    section_title = Element(browser, "xpath", "//h3[text()='Refine Search']").get_text()

    assert section_title == "Refine Search"


def test_opening_macs():
    browser = Browser(URL)
    home_page = HomePage(browser)
    home_page.show_mac_desktops()


def test_footer1():
    browser = Browser(URL)

    footer = Footer(browser)

    footer.about_us_click()

    footer.delivery_information_click()

    footer.privacy_policy_click()

    footer.delivery_information_click()

    footer.contact_us_click()

    footer.returns_click()

    footer.site_map_click()

    footer.brands_click()

    footer.gift_certification_click()

    footer.affiliates_click()

    footer.specials_click()

    footer.my_account_click()

    footer.order_history_click()

    footer.wish_list_click()

    footer.newsletter_click()

    browser.shutdown()


def chapter_11():
    browser = Browser("https://cleveronly.com/practice/")

    action_chains = Actions(browser)
    element = Element(browser, "xpath", "//aside[@id='card']")
    action_chains.double_click(element)
    time.sleep(2)
    background_color = element.get_background_color()
    converted_background_color2 = Color.from_string(background_color)
    print(converted_background_color2)
    assert converted_background_color2.rgb == 'rgb(255, 179, 128)'


def chapter_11_1_2():
    browser = Browser("https://cleveronly.com/practice/")

    action_chains = Actions(browser)
    element = Element(browser, "xpath", "//input[@type='text']")
    action_chains.send_keys_to_element(element, Keys.ENTER)
    time.sleep(3)
    element1 = Element(browser, "xpath", "//p[text()='You pressed the key!']")
    assert "You pressed the key!" == element1.get_text()


def chapter_11_1_3():
    browser = Browser("https://cleveronly.com/practice/")

    action_chains = Actions(browser)
    element = Element(browser, "xpath", "//div[@id='context_menu']")
    action_chains.right_click(element)
    element1 = Element(browser, "xpath", "//li[@onclick='changeColor()']")
    element1.click()
    background_color = element.get_background_color()
    converted_background_color3 = Color.from_string(background_color)
    print(converted_background_color3)
    assert converted_background_color3.rgb == 'rgb(204, 255, 245)'

    action_chains = Actions(browser)
    action_chains.right_click(element)
    element2 = Element(browser, "xpath", "//li[@onclick='changeFont()']")
    element2.click()
    text_element = Element(browser, "xpath", "//div[@id='context_menu']/p")
    text_font = text_element.get_text_font()
    print(text_font)
    assert text_font == '"Source Sans Pro", Arial, Helvetica, sans-serif'

    action_chains = Actions(browser)
    action_chains.right_click(element)
    element3 = Element(browser, "xpath", "//li[@class='menu-option']/a")
    original_window = browser.get_driver().current_window_handle
    element3.click()
    browser.get_driver().switch_to.window(original_window)

    action_chains = Actions(browser)
    action_chains.right_click(element)
    action_chains.send_keys(Keys.ESCAPE)
    menu = Element(browser, "xpath", "//div[@class='menu']")
    menu.wait_until_invisible()


if __name__ == "__main__":
    # test_header_1()
    # test_registration_through_dropdown()
    # test_login_through_dropdown()
    # test_header_2()
    test_opening_all_desktops()
    test_opening_all_pcs()
    # test_footer1()
    # chapter_11()
    # chapter_11_1_2()
    # chapter_11_1_3()
