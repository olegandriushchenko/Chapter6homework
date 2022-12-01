from BrainBucketTest.drivers.browser import Browser
from BrainBucketTest.drivers.UIElement import UIElement as Element
import time


class Alert:
    def __init__(self, browser):
        self.driver = browser.get_driver()
        self.alert = self.driver.switch_to.alert

    def switch_to_alert(self, browser):
        return self.driver.switch_to.alert

    def accept_alert(self, browser):
        self.alert.accept()

    def cancel_alert(self, browser):
        self.alert.dismiss()

    def enter_text(self, text):
        self.alert.send_keys(text)
        



