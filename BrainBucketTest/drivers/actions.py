from selenium.webdriver.common.action_chains import ActionChains


class Actions:
    def __init__(self, browser):
        self.__driver = browser.get_driver()
        self._action_chains = None

    def __reset_actions(self):
        self.action_chains = ActionChains(self.__driver)

    def click(self, element=None):
        self.__reset_actions()

        if element:
            self.action_chains.click(element.get_element()).perform()
        else:
            self.action_chains.click().perform()

    def click_and_hold(self, element=None):
        self.__reset_actions()

        if element:
            self.action_chains.click_and_hold(element.get_element()).perform()
        else:
            self.action_chains.click_and_hold().perform()

    def right_click(self, element=None):
        self.__reset_actions()

        if element:
            self.action_chains.context_click(element.get_element()).perform()
        else:
            self.action_chains.context_click().perform()

    def double_click(self, element=None):
        self.__reset_actions()

        if element:
            self.action_chains.double_click(element.get_element()).perform()
        else:
            self.action_chains.double_click().perform()

    def drag_and_drop(self, source, target):
        self.__reset_actions()
        self.action_chains.drag_and_drop(source.get_element(), target.get_element()).perform()

    def drag_and_drop_by_offset(self, source, xoffset=0, yoffset=0):
        self.__reset_actions()

        self.action_chains.drag_and_drop_by_offset(source.get_element(), xoffset, yoffset).perform()

    def key_down(self, key, element=None):
        self.__reset_actions()
        if element:
            self.action_chains.key_down(key, element.get_element()).perform()
        else:
            self.action_chains.key_down(key).perform()

    def key_up(self, key, element=None):
        self.__reset_actions()

        if element:
            self.action_chains.key_up(key, element.get_element()).perform()
        else:
            self.action_chains.key_up(key).perform()

    def move_mouse(self, xoffset, yoffset):
        self.__reset_actions()

        self.action_chains.move_by_offset(xoffset, yoffset).perform()

    def move_to_element(self, to_element):
        self.__reset_actions()

        self.action_chains.move_to_element(to_element.get_element()).perform()

    def move_to_element_with_offset(self, to_element, xoffset, yoffset):
        self.__reset_actions()

        self.action_chains.move_to_element_with_offset(to_element.get_element(), xoffset, yoffset).perform()

    def send_keys(self, keys_to_send):
        self.__reset_actions()
        self.action_chains.send_keys(keys_to_send).perform()

    def send_keys_to_element(self, element, keys_to_send):
        self.__reset_actions()
        self.action_chains.send_keys_to_element(element.get_element(), keys_to_send).perform()
