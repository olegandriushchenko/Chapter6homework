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

    def get_user_email(self):
        if 'user_email' not in self.data.keys():
            raise Exception("User_email option is not present in the config file")
        return self.data['user_email']

    def get_user_password(self):
        if 'user_password' not in self.data.keys():
            raise Exception("User_password option is not in the config file")
        return self.data['user_password']


