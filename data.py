import requests

# File:    data.py
# Project: PyQuizApp

# These parameters can be changed or added to (except type; boolean type is supported here, multiple choice is not)
# Too see the options, visit: https://opentdb.com/api_config.php
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
