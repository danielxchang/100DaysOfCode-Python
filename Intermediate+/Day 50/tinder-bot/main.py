from selenium import webdriver
import os
from dotenv import load_dotenv
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

load_dotenv()

EMAIL = os.environ.get("FB_EMAIL")
PASSWORD = os.environ.get("FB_PASSWORD")
URL = "https://tinder.com/"

chrome_driver_path = "/Users/Daniel/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


def login_to_tinder():
    driver.get(URL)
    sleep(3)

    driver.find_element("link text", "Log in").click()
    sleep(2)

    fb_login = driver.find_element("xpath", '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
    fb_login.click()
    sleep(1)

    windows = driver.window_handles
    base_window, fb_login_window = windows
    driver.switch_to.window(fb_login_window)

    email = driver.find_element(value="email")
    email.send_keys(EMAIL)
    password = driver.find_element(value="pass")
    password.send_keys(PASSWORD)
    driver.find_element(value="loginbutton").click()

    driver.switch_to.window(base_window)
    sleep(5)


def tinder_like_bot():
    login_to_tinder()
    try:
        driver.find_element("xpath", '//*[@id="u1408193709"]/div/div/div/div/div[3]/button[1]').click()
        sleep(1)
        driver.find_element("xpath", '//*[@id="u1408193709"]/div/div/div/div/div[3]/button[2]').click()
        driver.find_element("xpath", '//*[@id="u1186853273"]/div/div[2]/div/div/div[1]/button').click()
    except NoSuchElementException:
        sleep(2)
    finally:
        sleep(10)

    for _ in range(100):
        try:
            buttons = driver.find_elements("css selector", '.recsCardboard__cards button')
            like = buttons[-2]
            like.click()
        except ElementClickInterceptedException:
            try:
                pop_up_buttons = driver.find_elements("css selector", 'body div div div button')
                pop_up_buttons[-1].click()
            except ElementClickInterceptedException:
                match_screen = driver.find_elements("css selector", 'body div[2] div div div button')
                match_screen[-1].click()
            finally:
                print("MATCH!")

        finally:
            sleep(3)

    driver.quit()


if __name__ == "__main__":
    tinder_like_bot()
