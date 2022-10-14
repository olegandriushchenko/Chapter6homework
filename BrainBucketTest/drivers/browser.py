from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


class Browser:
    def __init__(self, url, browser_name=""):
        if browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox(executable_path="drivers/geckodriver")
        else:
            s = Service(executable_path='drivers/chromedriver')
            self.driver = webdriver.Chrome(service=s)

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()

