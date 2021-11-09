import smtplib
import random
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

MONDAY = 0
SUNDAY = 6
GMAIL_SMTP = "smtp.gmail.com"
YAHOO_SMTP = "smtp.mail.yahoo.com"

my_gmail = os.environ.get("TEST_EMAIL")
recipient = os.environ.get("TEST_EMAIL")
password = os.environ.get("TEST_PW")


def send_email(quote):
    """
    Set up SMTP connection and sent quote email
    :param quote: string
    """
    with smtplib.SMTP(GMAIL_SMTP, port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=recipient,
            msg=f"Subject:{quote}\n\nCheers!"
        )


def gather_quotes():
    """
     Gather list of quotes from quotes.txt
     :return: list of quotes
     """
    with open('quotes.txt') as quotes_file:
        return quotes_file.readlines()


def motivational_monday_quote():
    """
    Send random quote on Mondays
    """
    now = dt.datetime.now()
    day_of_week = now.weekday()

    if day_of_week == MONDAY:
        quote = random.choice(gather_quotes())
        send_email(quote)


if __name__ == "__main__":
    motivational_monday_quote()
