from selenium import webdriver
import os
from dotenv import load_dotenv
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()

SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com"
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")

chrome_driver_path = "/Users/Daniel/Desktop/chromedriver"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = 0
        self.up = 0
        self.result_id = None

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        sleep(3)
        go = self.driver.find_element("class name", "js-start-test")
        go.click()
        sleep(45)
        try:
            self.driver.find_element("css selector", ".notification prompt-modal .notification-dismiss").click()
            sleep(1)
        except NoSuchElementException:
            pass
        finally:
            result_id = self.driver.find_element("xpath", "/html/body/div[3]/div/div[3]/div/"
                                                          "div/div/div[2]/div[3]/div[3]/div/"
                                                          "div[3]/div/div/div[1]/div/div/div[2]/div[2]/a").text
            download_speed = self.driver.find_element("class name", "download-speed").text
            upload_speed = self.driver.find_element("class name", "upload-speed").text
            self.result_id = result_id
            self.down = download_speed
            self.up = upload_speed
            print(f"Result ID: {self.result_id}\n"
                  f"Download Speed: {self.down}\n"
                  f"Upload Speed: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        sleep(2)

        try:
            sign_in = self.driver.find_element("xpath", "/html/body/div/div/div/div/main/div/"
                                                        "div/div/div[1]/div/div[3]/div[4]/span")
        except NoSuchElementException:
            sign_in = self.driver.find_element("xpath", "/html/body/div/div/div/div/main/div/"
                                                        "div/div/div[1]/div/div[3]/a[2]")
        finally:
            sign_in.click()
            sleep(2)

        self.driver.find_element("xpath", '/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a').click()
        sleep(3)
        username = self.driver.find_element("name", "username")
        username.send_keys(TWITTER_USERNAME)
        sleep(2)
        self.driver.find_element("xpath", "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/"
                                          "div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div").click()
        sleep(2)
        try:
            password = self.driver.find_element("name", "password")
        except NoSuchElementException:
            username = self.driver.find_element("name", "username")
            username.send_keys(TWITTER_USERNAME)
            sleep(1)
            password = self.driver.find_element("name", "password")
        finally:
            password.send_keys(TWITTER_PASSWORD)
            sleep(2)

        self.driver.find_element("xpath", "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/"
                                          "div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div").click()
        sleep(5)
        actions = ActionChains(self.driver)
        self.driver.find_element("xpath", "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/"
                                          "div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/"
                                          "label/div[1]/div/div/div").click()
        message = f"Hey Internet Provider, why is my internet speed {self.down}down/" \
                  f"{self.up}up when I pay for 150down/10up?"
        actions.send_keys(message)
        actions.perform()
        sleep(3)
        self.driver.find_element("xpath", "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/"
                                          "div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]").click()
        sleep(3)
