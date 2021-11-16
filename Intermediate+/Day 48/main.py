from selenium import webdriver
from pprint import pprint


chrome_driver_path = "/Users/Daniel/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# driver.get("https://www.amazon.com/AmazonBasics-Rubber-Encased-Dumbbell-Weight/dp/B074DZ5YL9?ref_=ast_sto_dp&th=1")
# price = driver.find_element("css selector", ".a-span12 .a-text-price").text
# print(price)

# driver.get("https://www.python.org/")
# event_elements = driver.find_elements("css selector", ".event-widget li")
# upcoming_events = {
#     i: {
#         'time': event.find_element("tag name", "time").text,
#         'name': event.find_element("tag name", "a").text
#     } for i, event in enumerate(event_elements)
# }
#
# pprint(upcoming_events)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

driver.quit()