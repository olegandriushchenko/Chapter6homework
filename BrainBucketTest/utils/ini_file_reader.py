from configparser import ConfigParser


class IniFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = ConfigParser()
            self.data.read_file(config_file)

    def get_browser(self):
        value = self.data.get('environment', 'browser', fallback=None)
        if value is None:
            raise Exception("Browser option is not present in the config file")
        return value

    def get_wait_time(self):
        value = self.data.get('environment', 'wait', fallback=None)
        if value is None:
            raise Exception("Wait_time option is not present in the config file")
        return int(value)

    def get_user_email(self):
        value = self.data.get('environment', 'user_email', fallback=None)
        if value is None:
            raise Exception("User_email option is not present in the config file")
        return self.data['user_email']

    def get_user_password(self):
        value = self.data.get('environment', 'user_password', fallback=None)
        if value is None:
            raise Exception("User_password option is not in the config file")
        return self.data['user_password']
