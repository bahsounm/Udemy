import requests
parameters = {"amount": 10, "type": "boolean"}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status() # built in error exception handling
response_code = response.json()["response_code"]
question_data = response.json()["results"]

# this was hardcoded before byt now we use the API to get live data, which is better and what we want

# some characters are replaced see HTML entities, so certain caharcters look weird we can fix this by using html unescape