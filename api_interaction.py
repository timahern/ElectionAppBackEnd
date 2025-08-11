import requests
import Election
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_CIVIC_INFO_API_KEY")

#sets parameters and makes api call to electionQuery to get all upcoming elections
e_params = {
    "key": api_key
}
elections_response = requests.get("https://www.googleapis.com/civicinfo/v2/elections", e_params)
elections_data = elections_response.json()
print(elections_data)


url = "https://www.googleapis.com/civicinfo/v2/divisionsByAddress"
params = {
    "address": "196 W 300 S Mt Pleasant UT 84647 USA",
    "key": api_key
}

response = requests.get(url, params=params)
data = response.json()
#print(data)

#id_list stores all the OCD divisons that the user resides in based off the address they gave
id_list = list(data.get("divisions", {}).keys())

#elections stores all the election objects that are retrieved by electionQuery
elections = elections_data.get("elections", [])
if not data.get("divisions", {}).items():
    print("nothing to see here")
else:
    for division_id, division_info in data.get("divisions", {}).items():
        #id_list.append(division_id)
        #print("the div id for this division is " + division_id, division_info.get("name"))
        print(f"the name for {division_id} is {division_info.get("name")}")

def get_matching_eid_to_user(ocd_list, elections_list):
    related = []

    for election in elections_list:
        eid = election.get("id")
        name = election.get("name")
        date = election.get("electionDay")
        ocd = election.get("ocdDivisionId")
        description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent convallis blandit lorem, at euismod eros fringilla in. Nam aliquet in nunc quis interdum. Phasellus interdum mattis aliquam. Nulla faucibus ultrices odio, sit amet efficitur enim mattis luctus. Aenean imperdiet dictum neque tristique ullamcorper. Praesent id ultrices est. Morbi purus neque, venenatis quis rhoncus at, commodo non leo."
        

        if ocd in ocd_list:
            e = Election.Election(eid, name, date, description)
            related.append(e.to_dict())

    return related

election_match_list = get_matching_eid_to_user(id_list, elections)
#print(election_match_list[0].to_dict())
if election_match_list:
    for i in election_match_list:
        print(i['eID'])
        print(i['name'])
else:
    print("no matching eids")