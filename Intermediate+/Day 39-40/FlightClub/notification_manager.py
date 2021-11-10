import os
from twilio.rest import Client
import smtplib
from dotenv import load_dotenv

load_dotenv()

GMAIL_SMTP = "smtp.gmail.com"
my_email = os.environ.get("EMAIL")
password = os.environ.get("EMAIL_PW")



class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = 'AC57a33e32f8abccc7ecee66067a26a29f'
        self.auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        self.phone_number = os.environ.get('PHONE_NUMBER')
        self.client = Client(self.account_sid, self.auth_token)

    def send_text(self, flight_data):
        sms_content=f"Low price alert!\nOnly ${flight_data['price']} to fly from\n{flight_data['departure_city']}-{flight_data['dc_code']} to {flight_data['arrival_city']}-{flight_data['ac_code']}, from:\n{flight_data['outbound_date']} to {flight_data['inbound_date']}."
        if flight_data['stop_overs']:
          sms_content += f"\nFlight has {flight_data['stop_overs']} stop over, via {flight_data['via_city']}."
        message = self.client.messages.create(
            messaging_service_sid='MGdbdbce2db415f5108c04c169fd828d27',
            body=sms_content,
            to=self.phone_number
        )
        return sms_content

    def send_emails(self, members, message, flight_link):
        for member in members:
          with smtplib.SMTP(GMAIL_SMTP, port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
              from_addr=my_email,
              to_addrs=member['email'],
              msg=f"Subject:New Low Price Flight!\n\n{message}\n{flight_link}"
            )
