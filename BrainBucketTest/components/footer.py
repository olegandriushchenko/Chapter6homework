from BrainBucketTest.drivers.UIElement import UIElement as Element


class Footer:
    def __init__(self, browser):
        self.about_us = Element(browser, "xpath", "//a[text()='About Us']")
        self.delivery_information = Element(browser, "xpath", "//a[text()='Delivery Information']")
        self.privacy_policy = Element(browser, "xpath", "//a[text()='Privacy Policy']")
        self.terms_and_conditions = Element(browser, "xpath", "//a[text()='Terms & Conditions']")
        self.contact_us = Element(browser, "xpath", "//a[text()='Contact Us']")
        self.returns = Element(browser, "xpath", "//div[@class='col-sm-3']/ul/li/a[text()='Returns']")
        self.site_map = Element(browser, "xpath", "//a[text()='Site Map']")
        self.brands = Element(browser, "xpath", "//a[text()='Brands']")
        self.gift_certification = Element(browser, "xpath", "//a[text()='Gift Certificates']")
        self.affiliates = Element(browser, "xpath", "//a[text()='Affiliates']")
        self.specials = Element(browser, "xpath", "//a[text()='Specials']")
        self.my_account = Element(browser, "xpath", "//div[@class='col-sm-3']/ul/li/a[text()='My Account']")
        self.order_history = Element(browser, "xpath", "//div[@class='col-sm-3']/ul/li/a[text()='Order History']")
        self.wish_list = Element(browser, "xpath", "//div[@class='col-sm-3']/ul/li/a[text()='Wish List']")
        self.newsletter = Element(browser, "xpath", "//div[@class='col-sm-3']/ul/li/a[text()='Newsletter']")

    def about_us_click(self):
        self.about_us.click()

    def delivery_information_click(self):
        self.delivery_information.click()

    def privacy_policy_click(self):
        self.privacy_policy.click()

    def terms_and_conditions_click(self):
        self.terms_and_conditions.click()

    def contact_us_click(self):
        self.contact_us.click()

    def returns_click(self):
        self.returns.click()

    def site_map_click(self):
        self.site_map.click()

    def brands_click(self):
        self.brands.click()

    def gift_certification_click(self):
        self.gift_certification.click()

    def affiliates_click(self):
        self.affiliates.click()

    def specials_click(self):
        self.specials.click()

    def my_account_click(self):
        self.my_account.click()

    def order_history_click(self):
        self.order_history.click()

    def wish_list_click(self):
        self.wish_list.click()

    def newsletter_click(self):
        self.newsletter.click()