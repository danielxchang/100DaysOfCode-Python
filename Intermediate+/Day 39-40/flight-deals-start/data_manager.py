import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
AUTH = os.environ.get("SHEETY_TOKEN")


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            "Authorization": AUTH
        }
        response = requests.get(url=f"{SHEETY_ENDPOINT}", headers=self.headers)
        self.data = response.json()['prices']

    def retrieve_data(self):
        return self.data

    def edit_row(self, iata_code, id):
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        requests.put(url=f"{SHEETY_ENDPOINT}/{id}", headers=self.headers, json=body)
