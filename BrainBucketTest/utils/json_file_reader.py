import json


class JsonFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = json.load(config_file)

    def get_browser(self):
        if 'browser' not in self.data.keys():
            raise Exception("Browser option is not present in the config file")
        return self.data['browser']

    def get_wait_time(self):
        if 'wait_time' not in self.data.keys():
            raise Exception("Wait_time option is not present in the config file")
        return int(self.data['wait_time'])

    def get_user1_email(self):
        if 'user_email' not in self.data.keys():
            raise Exception("User_email option is not present in the config file")
        return self.data['user_email']

    def get_user1_password(self):
        if 'user_password' not in self.data.keys():
            raise Exception("User_password option is not in the config file")
        return self.data['user_password']

    def get_browser_height(self):
        if 'browser_height' not in self.data.keys():
            raise Exception("browser_height option is not in the config file")
        return int(self.data['browser_height'])

    def get_browser_width(self):
        if 'browser_width' not in self.data.keys():
            raise Exception("browser_width option is not in the config file")
        return int(self.data['browser_width'])

    def get_url(self):
        value = self.data.get('environment', 'url', fallback=None)
        if value is None:
            raise Exception("URL option is not found in environment section")
        return value






