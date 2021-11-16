from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/Daniel/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('http://secure-retreat-92358.herokuapp.com/')
# article_count = driver.find_element("css selector", value="#articlecount a")
# article_count.click()

# all_portals = driver.find_element("link text", "All portals")
# all_portals.click()

f_name = driver.find_element("name", "fName")
f_name.send_keys("Daniel")

l_name = driver.find_element("name", "lName")
l_name.send_keys("Chang")

email = driver.find_element("name", "email")
email.send_keys("daniel@gmail.com")

sign_up = driver.find_element("class name", "btn-primary")
sign_up.click()
