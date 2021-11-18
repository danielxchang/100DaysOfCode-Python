from bs4 import BeautifulSoup
import requests
import re
from time import sleep
from selenium import webdriver

chrome_driver_path = "/Users/Daniel/Desktop/chromedriver"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.69 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

google_form_link = "https://forms.gle/1eUv3GAntU5kjTrB6"
form_fields = ["address", "price", "link"]
zillow_link = "https://www.zillow.com/dallas-tx/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22" \
              "usersSearchTerm%22%3A%22Dallas%2C%20TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-97.07077445458984%2C%2" \
              "2east%22%3A-96.48369254541015%2C%22south%22%3A32.5842022918929%2C%22north%22%3A33.051038928484395%7D%" \
              "2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A38128%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible" \
              "%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A601093%7D%2C%22mp%22" \
              "%3A%7B%22min%22%3A0%2C%22max%22%3A2000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22val" \
              "ue%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%2" \
              "2fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22val" \
              "ue%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22" \
              "isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"


class PropertyResearchBot:
    def __init__(self):
        self.listings = {}
        self.driver = webdriver.Chrome(chrome_driver_path)

    def scrape_zillow(self):
        response = requests.get(url=zillow_link, headers=HEADERS)
        zillow_page = response.text
        soup = BeautifulSoup(zillow_page, 'html.parser')
        listing_card_tags = soup.find_all(class_='list-card-info')
        self.listings = {}
        for i, card in enumerate(listing_card_tags):
            card_link_tag = card.contents
            if len(card_link_tag) == 3:
                listing_link = link \
                    if re.search("https", link := card_link_tag[0]['href']) \
                    else "https://zillow.com" + link
                address = card_link_tag[0].contents[0].text
                price = re.split('[^$,0-9]', card_link_tag[-1].contents[0].text)[0]
                self.listings[i] = {
                    'address': address,
                    'price': price,
                    'link': listing_link
                }

    def submit_google_forms(self):
        for listing in self.listings.values():
            self.driver.get(google_form_link)
            sleep(1)
            input_fields = self.driver.find_elements("css selector", ".quantumWizTextinputPaperinputInputArea input")
            for i, field in enumerate(input_fields):
                field.send_keys(listing[form_fields[i]])
            self.driver.find_element("css selector", ".freebirdFormviewerViewNavigationLeftButtons div").click()
            sleep(1)


bot = PropertyResearchBot()
bot.scrape_zillow()
bot.submit_google_forms()
