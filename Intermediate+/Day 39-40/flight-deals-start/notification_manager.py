import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = 'AC57a33e32f8abccc7ecee66067a26a29f'
        self.auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        self.phone_number = os.environ.get('PHONE_NUMBER')
        self.client = Client(self.account_sid, self.auth_token)

    def send_text(self, flight_data):
        message = self.client.messages.create(
            messaging_service_sid='MGdbdbce2db415f5108c04c169fd828d27',
            body=f"Low price alert!\n"
                 f"Only ${flight_data['price']} to fly from\n"
                 f"{flight_data['departure_city']}-{flight_data['dc_code']} to "
                 f"{flight_data['arrival_city']}-{flight_data['ac_code']}, from\n"
                 f"{flight_data['outbound_date']} to {flight_data['inbound_date']}.",
            to=self.phone_number
        )
        print(message.status)
