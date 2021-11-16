from selenium import webdriver
import os
from dotenv import load_dotenv
from time import sleep
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

linkedin_email = os.environ.get("LINKEDIN_EMAIL")
linkedin_password = os.environ.get("LINKEDIN_PW")

URL = "https://www.linkedin.com/jobs/search/" \
      "?f_AL=true&geoId=103644278&keywords=web%20developer&location=United%20States"

chrome_driver_path = "/Users/Daniel/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)


def sign_in_to_linkedin():
    sign_in = driver.find_element("class name", "nav__button-secondary")
    sign_in.click()

    username = driver.find_element(value="username")
    username.send_keys(linkedin_email)
    password = driver.find_element(value="password")
    password.send_keys(linkedin_password)

    submit = driver.find_element("css selector", ".login__form_action_container button")
    submit.click()


def close_application():
    driver.find_element("class name", "artdeco-modal__dismiss").click()
    driver.find_element("css selector", ".artdeco-modal__actionbar button").click()


def save_job():
    try:
        easy_apply = driver.find_element("css selector", ".jobs-apply-button--top-card .jobs-apply-button")
    except NoSuchElementException:
        return

    easy_apply.click()
    sleep(2)

    buttons = driver.find_elements("css selector", "footer button")
    if len(buttons) > 1 or buttons[0].get_attribute('aria-label') != "Submit application":
        close_application()
        return
    else:
        close_application()
        save = driver.find_element("class name", "jobs-save-button")
        save.click()


def linkedin_application_automation():
    sign_in_to_linkedin()
    sleep(3)
    pop_up = driver.find_element("class name", "msg-overlay-bubble-header")
    pop_up.click()
    jobs = driver.find_elements("css selector", ".jobs-search-results__list .job-card-container--clickable")
    for job in jobs:
        job.click()
        sleep(2)
        save_job()
        sleep(2)
    driver.quit()


if __name__ == "__main__":
    linkedin_application_automation()




