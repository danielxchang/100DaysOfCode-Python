from selenium import webdriver
import datetime as dt

DURATION = 5
INTERVAL = 5

chrome_driver_path = "/Users/Daniel/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


def show_cps():
    cps = driver.find_element(value="cps").text.split(" : ")[1]
    print(f"Cookies/second: {cps}. Game Over.")


def check_store():
    cookies = int(driver.find_element(value="money").text.replace(',', ''))
    options = driver.find_elements("css selector", "#store div")[::-1]
    option_amounts = [
        int(string.split("\n")[0].split(" - ")[1].replace(',', ''))
        if (string := option.text).find("-") != -1 else 0
        for option in options
    ]

    for i, cost in enumerate(option_amounts):
        if cookies >= cost > 0:
            options[i].click()
            break


def cookie_clicker():
    cookie = driver.find_element(value="cookie")
    last_check = dt.datetime.now()
    end_of_game = last_check + dt.timedelta(minutes=DURATION)

    while (now := dt.datetime.now()) <= end_of_game:
        cookie.click()
        if last_check + dt.timedelta(seconds=INTERVAL) <= now:
            last_check += dt.timedelta(seconds=INTERVAL)
            check_store()

    show_cps()


if __name__ == "__main__":
    cookie_clicker()
