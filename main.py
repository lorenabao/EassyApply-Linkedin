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
        login_password.send_keys(Keys.RETURN)

    def job_search(self):
        """This function goes to the 'Jobs' section and looks for all the jobs that matches the keywords"""

        # Go to 'Jobs' section
        self.driver.get("https://www.linkedin.com/jobs/search/?")

        # Introduce keywords and location and hit enter
        search_keyword = self.driver.find_element_by_xpath("//input[starts-with(@id, 'jobs-search-box-keyword')]")
        search_keyword.clear()
        search_keyword.send_keys(self.keywords)

        search_location = self.driver.find_element_by_xpath("//input[starts-with(@id, 'jobs-search-box-location')]")
        search_location.clear()
        search_location.send_keys(self.location)

        search_button = self.driver.find_element_by_css_selector(".jobs-search-box__submit-button")
        search_button.click()


    def filter(self):
        """This function filters all the job results by 'Easy Apply'"""
        

         # Select all filters, click on Easy Apply and apply the filter
        all_filters_button = self.driver.find_element_by_css_selector(".artdeco-pill.artdeco-pill--slate.artdeco-pill--choice.artdeco-pill--2.search-reusables__filter-pill-button.search-reusables__filter-pill-button.search-reusables__all-filters-pill-button")
        all_filters_button.click()
        easy_apply_button = self.driver.find_element_by_xpath("//input[@class, 'input artdeco-toggle__button']")
        easy_apply_button.click()
        all_filters_button = self.driver.find_element_by_css_selector("//button[@data-test-reusables-filters-modal-show-results-button='true']")
        all_filters_button.click()
       


if __name__ == "__main__":
    with open('config.json') as config_file:
        data = json.load(config_file)

    bot = EasyApplyLinkedin(data)
    bot.login_linkedin()
    bot.job_search()
    bot.filter()