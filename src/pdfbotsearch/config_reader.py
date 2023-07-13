import os
import configparser

class ConfigReader:
    def __init__(self):
        # Get the absolute path of the root folder
        self.root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__)))

        # Read the config file from the root folder
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(self.root_folder, "config.ini"))

    def get_value(self, section, key):
        return self.config[section][key]
