import json
from selenium import webdriver

class EasyApplyLinkedin:
    def __init__(self, data):
        """Parameter initialization"""
        self.email = data['email']
        self.password = data['password']
        self.keywords = data['keywords']
        self.location = data['location']
        self.driver = webdriver.Chrome(data['driver_path'])

if __name__ == "__main__":
    with open('config.json') as config_file:
        data = json.load(config_file)
    bot = EasyApplyLinkedin(data)