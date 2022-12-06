from BrainBucketTest.utils.json_file_reader import JsonFileReader
from BrainBucketTest.utils.ini_file_reader import IniFileReader


class ConfigReader:
    def __init__(self, filename):
        self.reader = None

        if filename.endswith(".json"):
            self.reader = JsonFileReader(filename)
        elif filename.endswith(".ini"):
            self.reader = IniFileReader(filename)
        else:
            raise Exception("File format is not supported")

    def get_browser(self):
        return self.reader.get_browser()

    def get_wait_time(self):
        return self.reader.get_wait_time()

    def user_email(self):
        return self.reader.get_user_email()

    def user_password(self):
        return self.reader.get_user_password()
