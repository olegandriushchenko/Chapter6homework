from BrainBucketTest.drivers.actions import Actions
from BrainBucketTest.drivers.UIElement import UIElement as Element
from BrainBucketTest.drivers.browser import Browser
from selenium.webdriver.support.color import Color

URL = "https://cleveronly.com/practice/"


def chapter_11():
    browser = Browser(URL)

    action_chains = Actions(browser.get_driver())
    element = Element(browser, "xpath", "//aside[@id='card']/p")
    action_chains.double_click(element)
    background_color = element.get_background_color()
    converted_background_color2 = Color.from_string(background_color)
    assert converted_background_color2.rgb == 'rgb(154, 154, 154)'


if __name__ == "__main__":
    chapter_11()