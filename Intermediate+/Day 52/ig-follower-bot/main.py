from selenium import webdriver
import os
from dotenv import load_dotenv
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()

URL = "https://www.instagram.com"
SIMILAR_ACCOUNT = "barackobama"
username = os.environ.get("IG_USERNAME")
password = os.environ.get("IG_PASSWORD")
chrome_driver_path = "/Users/Daniel/Desktop/chromedriver"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.followed = 0

    def login(self):
        self.driver.get(URL)
        sleep(5)
        username_input = self.driver.find_element("name", "username")
        username_input.send_keys(username)
        sleep(1)
        password_input = self.driver.find_element("name", "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        sleep(5)
        self.driver.find_element("class name", "cmbtv").click()
        sleep(2)

    def find_followers(self):
        self.driver.get(f"{URL}/{SIMILAR_ACCOUNT}")
        followers_btn = self.driver.find_elements("class name", "-nal3")[1]
        followers_btn.click()
        sleep(3)
        followers_pop_up = self.driver.find_element("class name", "isgrP")
        while True:
            self.follow(followers_pop_up)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight',
                                       followers_pop_up)
            if self.followed > 20:
                break
            sleep(3)

    def follow(self, pop_up_window):
        follow_buttons = pop_up_window.find_elements("tag name", "button")
        for btn in follow_buttons:
            try:
                btn.click()
                self.followed += 1
            except ElementClickInterceptedException:
                self.driver.find_element("class name", "HoLwm").click()
                sleep(1)
            sleep(2)


bot = InstaFollower()
bot.login()
bot.find_followers()
