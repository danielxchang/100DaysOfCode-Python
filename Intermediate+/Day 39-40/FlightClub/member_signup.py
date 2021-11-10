import os
import requests
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.environ['USERS_ENDPOINT']
headers = {
  "Authorization": os.environ['SHEETY_TOKEN']
}

print("Welcome to Daniel's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
confirm_email = input("Type your email again.\n")
if email == confirm_email and first_name and last_name:
  print("\nSuccess! Your email has been added! You're in the club!")

new_member_data = {
  'user': {
    'firstName': first_name,
    'lastName': last_name,
    'email': email
  }
}

response = requests.post(url=ENDPOINT, json=new_member_data, headers=headers)
