from BrainBucketTest.components.header import Header
from BrainBucketTest.components.right_menu import RightMenu
from BrainBucketTest.drivers.UIElement import UIElement as Element


class LoginPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)
        self.continue_btn = Element(browser, "xpath", "//div[@id='content']/div/div/div/a")
        self.email_input = Element(browser, "id", "input-email")
        self.password_input = Element(browser, "id", "input-password")
        self.login_button = Element(browser, "xpath", "//div[@id='content']/div/div[2]/div/form/input")

    def open_registration_from_menu(self):
        self.header.open_login_page()
        self.right_menu.click_registration()

    def open_registration_from_account_dropdown(self):
        self.header.open_registration_form()

    def click_continue_btn(self):
        self.header.open_login_page()
        self.continue_btn.click()

    def email_input_click(self, text):
        self.email_input.enter_text(text)

    def password_input_click(self, text):
        self.password_input.enter_text(text)

    def login_button_click(self):
        self.login_button.click()