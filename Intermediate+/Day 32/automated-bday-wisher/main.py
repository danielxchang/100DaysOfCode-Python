import pandas
import datetime as dt
import random
import smtplib
import os

NUM_TEMPLATES = 3
GMAIL_SMTP = "smtp.gmail.com"

my_email = os.environ.get("TEST_EMAIL")
password = os.environ.get("TEST_PW")


def automated_birthday_wisher():
    """
    Checks if today matches a birthday in the birthdays.csv and sends birthday email
    """
    birthdays = {}
    birthdays_df = pandas.read_csv("birthdays.csv")
    for i, data in birthdays_df.iterrows():
        birthday = (data.month, data.day)
        if not birthdays.get(birthday):
            birthdays[birthday] = [data]
        else:
            birthdays[birthday].append(data)

    today = (dt.date.today().month, dt.date.today().day)

    if today in birthdays:
        birthday_people = birthdays[today]
        send_emails(birthday_people)
    else:
        print("There are no birthdays today...😥")


def send_emails(people):
    """
    sends birthday emails to all people in people list
    :param people: list
    """
    with smtplib.SMTP(GMAIL_SMTP, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        for person in people:
            name = person['name']
            email = person['email']
            email_content = update_template(name)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject: Happy Birthday {name}!\n\n{email_content}"
            )
            print(f"Sent email to {email}")


def update_template(name):
    """
    picks a random letter from letter templates and replaces the [NAME] with the person's actual name from birthdays.csv
    :param name: string
    :return: string updated letter content
    """
    file_path = f"letter_templates/letter_{random.randint(1, NUM_TEMPLATES)}.txt"
    with open(file_path) as template:
        old_content = template.read()
        new_content = old_content.replace("[NAME]", name)
    return new_content


if __name__ == "__main__":
    automated_birthday_wisher()
