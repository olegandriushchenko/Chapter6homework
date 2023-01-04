from BrainBucketTest.components.header import Header
from BrainBucketTest.components.right_menu import RightMenu
from BrainBucketTest.drivers.UIElement import UIElement as Element
from BrainBucketTest.drivers.dropdown import Dropdown


class RegistrationPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)

        self.title = Element(browser, "xpath", "//div[@id='content']/h1")
        self.first_name_input = Element(browser, "id", "input-firstname")
        self.last_name_input = Element(browser, "id", "input-lastname")
        self.email_input = Element(browser, "id", "input-email")
        self.telephone_input = Element(browser, "id", "input-telephone")
        self.fax_input = Element(browser, "id", "input-fax")
        self.company_input = Element(browser, "id", "input-company")
        self.first_address_input = Element(browser, "id", "input-address-1")
        self.city_input = Element(browser, "id", "input-city")
        self.postcode_input = Element(browser, "id", "input-postcode")
        self.password_input = Element(browser, "id", "input-password")
        self.confirm_password_input = Element(browser, "id", "input-confirm")

        self.country_dropdown = Dropdown(browser, "id", 'input-country')
        self.region_dropdown = Dropdown(browser, "id", 'input-zone')

        self.subscribe_btn = Element(browser, "xpath", "//input[@name='newsletter' and @value='1']")
        self.unsubscribe_btn = Element(browser, "xpath", "//input[@name='newsletter' and @value='0']")

        self.privacy_policy_checkbox = Element(browser, "name", "agree")

        self.continue_btn = Element(browser, "xpath", "//input[@value='Continue']")

        self.first_name_error = Element(browser, "xpath", "//fieldset[@id='account']/div[2]/div/div")
        self.last_name_error = Element(browser, "xpath", "//fieldset[@id='account']/div[3]/div/div")
        self.phonenumber_error = Element(browser, "xpath", "//fieldset[@id='account']/div[5]/div/div")
        self.password_error = Element(browser, "xpath", "//fieldset[3]/div/div/div")

    def get_form_title(self):
        return self.title.get_text(wait=True)

    def enter_first_name(self, text):
        self.first_name_input.enter_text(text)

    def enter_last_name(self, text):
        self.last_name_input.enter_text(text)

    def enter_email(self, text):
        self.email_input.enter_text(text)

    def enter_telephone(self, text):
        self.telephone_input.enter_text(text)

    def enter_fax(self, text):
        self.fax_input.enter_text(text)

    def enter_company(self, text):
        self.company_input.enter_text(text)

    def enter_first_line_address(self, text):
        self.first_address_input.enter_text(text)

    def enter_city(self, city):
        self.city_input.enter_text(city)

    def enter_postcode(self, postcode):
        self.postcode_input.enter_text(postcode)

    def enter_password(self, password):
        self.password_input.enter_text(password)

    def confirm_password(self, password):
        self.confirm_password_input.enter_text(password)

    def select_country(self, country):
        self.country_dropdown.select_by_text(country)

    def select_state(self, state):
        self.region_dropdown.select_by_text(state)

    def subscribe_to_newsletters(self):
        self.subscribe_btn.click()

    def unsubscribe_from_newsletters(self):
        self.unsubscribe_btn.click()

    def agree_to_privacy_policy(self):
        self.privacy_policy_checkbox.click()

    def submit_form(self):
        self.continue_btn.submit()

    def get_firstname_error(self):
        return self.first_name_error.get_text()

    def get_lastname_error(self):
        return self.last_name_error.get_text()

    def get_phonenumber_error(self):
        return self.phonenumber_error.get_text()

    def get_password_error(self):
        return self.password_error.get_text()


