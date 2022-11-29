class Iframe:
    def __init__(self, browser):
        self.driver = browser.get_driver()
        self.iframe = self.driver.switch_to.iframe

    def switch_to_iframe(self):
        return self.driver.switch_to.iframe
