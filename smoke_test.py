from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.color import Color

s = Service(executable_path = 'drivers/chromedriver')
driver = webdriver.Chrome(service = s)
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()
logo = driver.find_element("xpath", "//img[@title='Brainbucket']")

newregisterbtn = driver.find_element("xpath", "//a[contains(text(),'Continue')]")
background_color = newregisterbtn.value_of_css_property('background-color')
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
newregisterbtn.click()

firstname_field = driver.find_element("xpath", "//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class


firstname_input = driver.find_element("id", "input-firstname")
firstname_input.clear()
firstname_input.send_keys("Oleg")


#homework,
#exercise 1
password_field = driver.find_element("xpath", "//input[@id='input-password']")
password_input = driver.find_element("id", "input-password")
password_input.clear()
password_input.send_keys("12345678")
password_field.click()

# homework exercise 2

lastname_field = driver.find_element("xpath", "//fieldset[@id='account']/div[3]/label")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element("id", "input-lastname")
lastname_input.clear()
lastname_input.send_keys("Andriushchenko")

email_field = driver.find_element("xpath", "//fieldset[@id='account']/div[4]/label")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class

email_input = driver.find_element("id", "input-email")
email_input.clear()
email_input.send_keys("oleg@gmail.com")


telephone_field = driver.find_element("xpath", "//fieldset[@id='account']/div[5]/label")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

telephone_input = driver.find_element("id", "input-telephone")
telephone_input.clear()
telephone_input.send_keys("1234567890")


address_field = driver.find_element("xpath", "//fieldset[@id='address']/div[2]/label")
address_field_class = address_field.get_attribute("class")
assert "required" in address_field_class

address_input = driver.find_element("id", "input-address-1")
address_input.clear()
address_input.send_keys("123 Michigan Ave")


city_field = driver.find_element("xpath", "//fieldset[@id='address']/div[4]/label")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class

city_input = driver.find_element("id", "input-city")
city_input.clear()
city_input.send_keys("Chicago")


continue_btn = driver.find_element("xpath", "//input[@value='Continue']")
background_color2 = continue_btn.value_of_css_property("background-color")
converted_background_color2 = Color.from_string("background-color")
assert converted_background_color2.rgb == 'rgb(34, 154, 200)'
continue_btn.click()

#driver.quit()


