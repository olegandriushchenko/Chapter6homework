from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from datetime import datetime
from selenium.common.exceptions import *


class UIElement:
    def __init__(self, browser, by, locator):
        self.driver = browser.get_driver()
        self.wait = browser.get_wd_wait()
        self._by = by
        self._locator = locator

    def save_screenshot(self):
        now = datetime.now()
        filename = "../screenshots/" + now.strftime("%d%m%Y_%H%M%S.png")
        self.driver.save_screenshot(filename)

    def get_element(self):
        try:
            return self.driver.find_element(self._by, self._locator)
        except NoSuchElementException:
            print("Wasn't able to find element by {} with locator={}".format(self._by, self._locator))
            self.save_screenshot()
            raise

    def get_locator(self):
        return self._locator

    def wait_until_visible(self):
        return self.wait.until(EC.visibility_of_element_located((self._by, self._locator)))

    def wait_until_invisible(self):
        return self.wait.until(EC.invisibility_of_element_located((self._by, self._locator)))

    def get_text(self, wait=True):
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()
        return element.text

    def get_attribute(self, attribute, wait=True):
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()
        return element.get_attribute(attribute)

    def click(self, xpath=None):
        if xpath is None:
            locator = self._locator
        else:
            locator = xpath
        self.wait.until(EC.element_to_be_clickable((self._by, locator))).click()

    def enter_text(self, text, wait=True):
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()
        element.clear()
        element.send_keys(text)

    def submit(self):
        try:
            self.wait.until(EC.element_to_be_clickable((self._by, self._locator))).submit()
        except TimeoutException:
            print("Web element with locator {} by {} is not clickable".format(self._locator, self._by))
            self.save_screenshot()
            raise

    def get_background_color(self):
        return self.get_element().value_of_css_property("background-color")

    def get_text_font(self):
        return self.get_element().value_of_css_property("font-family")

