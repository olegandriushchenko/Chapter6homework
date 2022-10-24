from BrainBucketTest.drivers.UIElement import UIElement as Element


class RightMenu:
    def __init__(self, browser):
        self.login_btn = Element(browser, "xpath", "//*[@id='column-right']//a[1]")
        self.registration_btn = Element(browser, "xpath", "//*[@id='column-right']//a[2]")
        self.forgotten_password_btn = Element(browser, "xpath", "//*[@id='column-right']//a[3]")
        self.my_account_btn = Element(browser, "xpath", "//*[@id='column-right']//a[4]")
        self.address_book = Element(browser, "xpath", "//*[@id='column-right']//a[5]")
        self.wish_list = Element(browser, "xpath", "//*[@id='column-right']//a[6]")
        self.order_history = Element(browser, "xpath", "//*[@id='column-right']//a[7]")
        self.downloads = Element(browser, "xpath", "//*[@id='column-right']//a[8]")
        self.recurring_payments = Element(browser, "xpath", "//*[@id='column-right']//a[9]")
        self.reward_points = Element(browser, "xpath", "//*[@id='column-right']//a[10]")
        self.returns = Element(browser, "xpath", "//*[@id='column-right']//a[11]")
        self.transactions = Element(browser, "xpath", "//*[@id='column-right']//a[12]")
        self.newsletter = Element(browser, "xpath", "//*[@id='column-right']//a[13]")

    def click_login(self):
        self.login_btn.click()

    def click_registration(self):
        self.registration_btn.click()

    def click_forgotten_btn(self):
        self.forgotten_password_btn.click()

    def click_my_account(self):
        self.my_account_btn.click()

    def click_my_address(self):
        self.address_book.click()

    def click_wish_list(self):
        self.wish_list.click()

    def click_order_history(self):
        self.order_history.click()

    def click_downloads(self):
        self.downloads.click()

    def click_recurring_payments(self):
        self.recurring_payments.click()

    def click_reward_points(self):
        self.reward_points.click()

    def click_returns(self):
        self.returns.click()

    def click_transactions(self):
        self.transactions.click()

    def click_newsletter(self):
        self.newsletter.click()
