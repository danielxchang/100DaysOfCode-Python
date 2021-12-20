from selenium import webdriver
chrome_driver_path = "/Users/Daniel/Desktop/chromedriver"


class ScraperBot:
    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(url)
        self.html = self.driver.page_source
