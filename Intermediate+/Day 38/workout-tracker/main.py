from os import environ
import requests
import datetime as dt
from dotenv import load_dotenv

load_dotenv()
GENDER = "male"
WEIGHT_KG = 59
HEIGHT_CM = 178
AGE = 24

APP_ID = environ.get("NIX_APP_ID")
API_KEY = environ.get("NIX_API_KEY")
TOKEN = f"Bearer {environ.get('SHEETY_TOKEN')}"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_post_endpoint = environ.get("SHEETY_WORKOUT_POST")
nix_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': "0"
}


def exercise_tracker():
    exercise = input("Tell me which exercise you did: ")

    exercise_data = {
        "query": exercise,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }

    exercise_response = requests.post(url=exercise_endpoint, headers=nix_headers, json=exercise_data)
    data = exercise_response.json()
    exercise_dt = dt.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    date, time = exercise_dt.split()

    for exercise in data["exercises"]:
        exercise_data = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise['name'].title(),
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories']
            }
        }

        sheety_response = requests.post(url=sheety_post_endpoint, json=exercise_data, headers={"Authorization": TOKEN})
        print(sheety_response.status_code)


if __name__ == "__main__":
    exercise_tracker()
