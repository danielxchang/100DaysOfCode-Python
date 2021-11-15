import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

PRODUCT_URL = "https://www.amazon.com/AmazonBasics-Rubber-Encased-Dumbbell-Weight/dp/B074DZ5YL9?ref_=ast_sto_dp&th=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.69 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
TARGET_PRICE = 20

GMAIL_SMTP = "smtp.gmail.com"
my_email = os.environ.get("EMAIL")
password = os.environ.get("EMAIL_PW")


def get_amazon_price():
    response = requests.get(url=PRODUCT_URL, headers=HEADERS)
    amazon_page = response.text

    soup = BeautifulSoup(amazon_page, "lxml")
    price_tag = soup.find(name="span", class_="a-offscreen")
    price = float(price_tag.getText().split("$")[1])
    return price


def send_email_alert(price, name):
    with smtplib.SMTP(GMAIL_SMTP, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Price Alert! \n\n {name} is now ${price}. Buy now!\n"
                f"{PRODUCT_URL}"
        )


def amazon_price_tracker():
    price = get_amazon_price()
    product = PRODUCT_URL.split("com/")[1].split("/")[0].replace("-", " ")
    if price < TARGET_PRICE:
        send_email_alert(price, product)


if __name__ == "__main__":
    amazon_price_tracker()
