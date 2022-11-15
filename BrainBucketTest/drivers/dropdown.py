from BrainBucketTest.drivers.UIElement import UIElement as Element
from selenium.webdriver.support.select import Select


class Dropdown(Element):
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)

    def select_by_text(self, option):
        Select(self.get_element()).select_by_visible_text(option)

    def select_by__value(self, value):
        Select(self.get_element()).select_by_value(value)

    def select_by__index(self, index):
        Select(self.get_element()).select_by_index(index)

# homework chapter 9.2
    def deselect_by_text(self, option):
        Select(self.get_element()).deselect_by_visible_text(option)

    def select_by_option_xpath(self, option_xpath):
        self.click(self.get_locator() + option_xpath)


class Checkbox(Element):
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)

    def select_by_xpath(self, value):
        Select(self.get_element()).select_by_value(value)
