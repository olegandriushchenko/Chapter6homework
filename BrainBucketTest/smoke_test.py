# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.color import Color


# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

from BrainBucketTest.drivers.browser import Browser
from BrainBucketTest.drivers.UIElement import UIElement as Element

from BrainBucketTest.drivers.dropdown import Dropdown


browser = Browser("https://cleveronly.com/brainbucket/index.php?route=common/home")
driver = browser.get_driver()


driver.maximize_window()

logo = driver.find_element("xpath", "//img[@title='Brainbucket']")

# Chapter 8 lesson 1 assignment
# Dropdown(browser, "xpath", "//div[@id='top-links']/ul/li[2]/a").select_by_text("My Account").click()
wd_wait = WebDriverWait(driver, 10)
element = wd_wait.until(EC.element_to_be_clickable(("xpath", "//div[@id='top-links']/ul/li[2]/a")))

account_btn = driver.find_element("xpath", "//div[@id='top-links']/ul/li[2]/a").click()
# login btn
wd_wait.until(EC.visibility_of_element_located(("xpath", "//div[@id='top-links']/ul/li[2]/ul/li[2]/a")))
login_option = driver.find_element("xpath", "//*[@class='dropdown-menu dropdown-menu-right']/li[2]")
login_option.click()

newregisterbtn = driver.find_element("xpath", "//div[@id='content']/div/div/div/a")
background_color = newregisterbtn.value_of_css_property('background-color')
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
newregisterbtn.click()

register_btn = Element(browser, "xpath", "//div[@id='top-links']/ul/li[2]/a").click()

firstname_field = driver.find_element("xpath", "//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class


firstname_input = driver.find_element("id", "input-firstname")
firstname_input.clear()
firstname_input.send_keys("Oleg")


# homework,
# exercise 1
password_field = driver.find_element("xpath", "//input[@id='input-password']")
password_input = driver.find_element("id", "input-password")
password_input.clear()
password_input.send_keys("12345678")
password_field.click()

# homework exercise 2

lastname_field = driver.find_element("xpath", "//fieldset[@id='account']/div[3]/label")
lastname_field_class = lastname_field.get_attribute("class")
# print(lastname_field_class)
# assert "required" in lastname_field_class

lastname_input = driver.find_element("id", "input-lastname")
lastname_input.clear()
lastname_input.send_keys("Andriushchenko")

email_field = driver.find_element("xpath", "//fieldset[@id='account']/div[4]/label")
email_field_class = email_field.get_attribute("class")
# assert "required" in email_field_class

email_input = driver.find_element("id", "input-email")
email_input.clear()
email_input.send_keys("oleg@gmail.com")


telephone_field = driver.find_element("xpath", "//fieldset[@id='account']/div[5]/label")
telephone_field_class = telephone_field.get_attribute("class")
# assert "required" in telephone_field_class

telephone_input = driver.find_element("id", "input-telephone")
telephone_input.clear()
telephone_input.send_keys("1234567890")


address_field = driver.find_element("xpath", "//fieldset[@id='address']/div[2]/label")
address_field_class = address_field.get_attribute("class")
# assert "required" in address_field_class

address_input = driver.find_element("id", "input-address-1")
address_input.clear()
address_input.send_keys("123 Michigan Ave")


city_field = driver.find_element("xpath", "//fieldset[@id='address']/div[4]/label")
city_field_class = city_field.get_attribute("class")
# assert "required" in city_field_class

city_input = driver.find_element("id", "input-city")
city_input.clear()
city_input.send_keys("Chicago")


continue_btn = driver.find_element("xpath", "//input[@value='Continue']")
background_color2 = continue_btn.value_of_css_property("background-color")
converted_background_color2 = Color.from_string("background-color")
assert converted_background_color2.rgb == 'rgb(34, 154, 200)'
continue_btn.click()

# Chapter 8.2 exercises
# exercise 1
state_dropdown = driver.find_element("id", "input-zone")
state_dropdown_select = Select(state_dropdown)
state_dropdown_select.select_by_value("3635")

# chapter 9 exercise

no_subscribe_btn = Element(browser, "xpath", "//div[@id='content']/form/fieldset[4]/div/div/label[2]")
no_subscribe_btn.click()

privacy_policy_btn = Element(browser, "xpath", "//div[@id='content']/form/div/div/input")
privacy_policy_btn.click()


# homework chapter 9.2

Dropdown(browser, "id", "input-country").deselect_by_text(None)
Dropdown(browser, "id", "input-state").deselect_by_text(None)

Dropdown(browser, "id", "newsletter").select_by__value("1")
browser.shutdown()


