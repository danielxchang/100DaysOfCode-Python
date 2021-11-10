from flight_data import FlightData
import requests
import os
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()

TEQUILA_API_KEY = os.environ.get("FS_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {"apikey": TEQUILA_API_KEY}

    def get_iata_code(self, city):
        query = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=self.headers, params=query)
        return response.json()['locations'][0]['code']

    def get_flight_data(self, home_iata, destination_iata):
        today = date.today()
        query = {
            "fly_from": home_iata,
            "fly_to": destination_iata,
            "date_from": (today + timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (today + timedelta(days=180)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "USD",
            "one_for_city": 1,
            "max_stopovers": 0
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=self.headers)
        return FlightData(response.json())
