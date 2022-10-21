from BrainBucketTest.drivers.UIElement import UIElement as Element


class Header:
    def __init__(self, browser):
        self.my_account_btn = Element(browser, "xpath", "//div[@id='top-links']/ul/li[2]/a")
        self.my_account_dropdown = Element(browser, "xpath", "//*[@class='dropdown-menu dropdown-menu-right']")
        self.register_btn = Element(browser, "xpath", "//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
        self.login_btn = Element(browser, "xpath", "//*[@class='dropdown-menu dropdown-menu-right']/li[2]")
        self.wish_list_btn = Element(browser, "id", "wishlist-total")
        self.shopping_list_btn = Element(browser, "xpath", "//div[@id='top-links']/ul/li[4]")
        self.checkout_btn = Element(browser, "xpath", "//div[@id='top-links']/ul/li[5]")
        self.currency_btn = Element(browser, "xpath", "//form[@id='form-currency']/div/button")
        self.currency_dropdown = Element(browser, "xpath", "//*[@class='btn btn-link dropdown-toggle']")
        self.currency_change_dollars = Element(browser, "xpath", "//form[@id='form-currency']/div/ul/li[3]/button")
        self.logo = Element(browser, "id", "logo")
        self.search = Element(browser, "id", "search")
        self.call = Element(browser, "xpath", "//div[@id='top-links']/ul/li[1]")

    def verify_logo_is_visible(self):
        return self.logo.wait_until_visible()

    def open_registration_form(self):
        self.my_account_btn.click()
        self.my_account_dropdown.wait_until_visible()
        self.register_btn.click()

    def open_login_page(self):
        self.my_account_btn.click()
        self.my_account_dropdown.wait_until_visible()
        self.login_btn.click()

    def change_currency(self):
        self.currency_btn.click()
        self.currency_dropdown.wait_until_visible()
        self.currency_change_dollars.click()

    def open_wishlist(self):
        self.wish_list_btn.click()

    def search_for(self):
        self.search.click()

    def shopping_list(self):
        self.shopping_list_btn.click()

    def contact_us(self):
        self.call.click()