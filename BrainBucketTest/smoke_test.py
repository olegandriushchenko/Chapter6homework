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

account_btn = Element(browser, "xpath", "//div[@id='top-links']/ul/li[2]/a").click()
# login btn
wd_wait.until(EC.visibility_of_element_located(("xpath", "//div[@id='top-links']/ul/li[2]/ul/li[2]/a")))
login_option = Element(browser, "xpath", "//*[@class='dropdown-menu dropdown-menu-right']/li[2]")
login_option.click()
login_option = Element(browser, "xpath", "//div[@id='content']/div/div/div/h2")
assert "New Customer" == login_option.get_text()


continue_btn = driver.find_element("xpath", "//div[@id='content']/div/div/div/a")
background_color = continue_btn.value_of_css_property('background-color')
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
continue_btn.click()

register_btn = Element(browser, "xpath", "//div[@id='top-links']/ul/li[2]/a").click()
# assert "Register Account" == register_btn.get_text()


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

# Chapter 8.2 exercises
# exercise 1


state_dropdown = driver.find_element("id", "input-zone")
state_dropdown_select = Select(state_dropdown)
state_dropdown_select.select_by_value("3635")

# chapter 9 exercise

Dropdown(browser, "id", "input-country").select_by_text("--- Please Select ---")
Dropdown(browser, "id", "input-zone").select_by_text("--- Please Select ---")


subscribe_btn = Element(browser, "xpath", "//div[@id='content']/form/fieldset[4]/div/div/label/input")
subscribe_btn.click()

privacy_policy_btn = Element(browser, "xpath", "//div[@id='content']/form/div/div/input")
privacy_policy_btn.click()

# browser.shutdown()


