import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_CIVIC_INFO_API_KEY")

e_params = {
    "address": "196 W 300 S Mt Pleasant UT 84647 USA",
    "electionId": "9204",
    "key": api_key
}
elections_response = requests.get("https://www.googleapis.com/civicinfo/v2/voterinfo", e_params)
elections_data = elections_response.json()
print(elections_data)

if "contests" not in elections_data:
    print("There are no contests present")