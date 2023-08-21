import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EasyApplyLinkedin:
    def __init__(self, data):
        """Parameter initialization"""

        self.email = data['email']
        self.password = data['password']
        self.keywords = data['keywords']
        self.location = data['location']
        self.driver = webdriver.Chrome(data['driver_path'])

    def login_linkedin(self):
        """This function logs into your personal Linkedin profile"""

        # Make driver go to the Linkedin login url
        self.driver.get("https://www.linkedin.com/login")

        # Introduce email and password and hit enter
        login_email = self.driver.find_element_by_name("session_key")
        login_email.clear()
        login_email.send_keys(self.email)

        login_password = self.driver.find_element_by_name("session_password")
        login_password.clear()
        login_password.send_keys(self.password)

        login_password.send_key(Keys.RETURN)



if __name__ == "__main__":
    with open('config.json') as config_file:
        data = json.load(config_file)

    bot = EasyApplyLinkedin(data)
    bot.login_linkedin()