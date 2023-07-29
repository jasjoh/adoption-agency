import os
import requests

from dotenv import load_dotenv
load_dotenv()

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']

def auth_and_get_token():
    res = requests.post("https://api.petfinder.com/v2/oauth2/token",
                        data={'grant_type': 'client_credentials',
                                  'client_id': PETFINDER_API_KEY,
                                  'client_secret': PETFINDER_SECRET_KEY})

    return res.json()['access_token']


def get_pet_list(access_token):
    res = requests.get("https://api.petfinder.com/v2/animals",
                       params = {"limit": "100"},
                        headers={"Authorization": f"Bearer {access_token}"})

    return res.json()