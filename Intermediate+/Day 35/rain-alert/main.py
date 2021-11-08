import os
import requests
from twilio.rest import Client

account_sid = 'AC57a33e32f8abccc7ecee66067a26a29f'
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
phone_number = os.environ.get("PHONE_NUMBER")
parameters = {
    "lat": 33.150661,
    "lon": -96.825081,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
next_12_hours_data = weather_data['hourly'][:12]
next_12_weather_codes = [hourly_data['weather'][0]['id'] for hourly_data in next_12_hours_data]
if min(next_12_weather_codes) < 700:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MGdbdbce2db415f5108c04c169fd828d27',
        body="It's going to rain today. Bring an ☔️",
        to=phone_number
    )
    print(message.status)