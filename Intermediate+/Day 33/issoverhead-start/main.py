import requests
from datetime import datetime
import smtplib
import time
import os

MY_LAT = 3.150661  # Your latitude
MY_LONG = -96.825081  # Your longitude
GMAIL_SMTP = "smtp.gmail.com"
my_email = os.environ.get("TEST_EMAIL")
password = os.environ.get("TEST_PW")
recipient = os.environ.get("TEST_EMAIL")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def close_to_satellite():
    """
    Returns True if your position is within +5 or -5 degrees of the ISS position.
    :return: True or False
    """
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    return abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5


def is_dark():
    """
    retrieve sunrise and sunset hours of the day
    :return: int sunrise, sunset
    """
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    return hour <= sunrise or hour >= sunset


def check_for_satellite():
    while True:
        # Check if current location is close to satellite and currently dark enough to see satellite
        if close_to_satellite() and is_dark():
            with smtplib.SMTP(GMAIL_SMTP, port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=recipient,
                    msg="Subject: LOOK UP! The ISS is nearby!\n\nDon't miss it!"
                )
            print("Reminder email sent!")
        else:
            print("ISS Not close")
        time.sleep(60)


if __name__ == "__main__":
    check_for_satellite()
