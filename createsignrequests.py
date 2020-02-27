import requests
import json

data = {
    "document": 'https://yourteam.signrequest.com/api/v1/documents/uuid/',
    "signers": [
        {
                "email": "name+1@provider.com"
        },
        {
            "email": "name+2@provider.com"
        }
    ],
    "from_email": "name@provider.com",
    "message": "Please sign this documents - TEST",
    "subject": "SignTest - YourTeam API - Python",
    "who": "o",
    "needs_to_sign": "true"
    # Add other parameters here
}

response = requests.post(
    "https://yourteam.signrequest.com/api/v1/signrequests/",
    headers={"Authorization": "Token YOUR_TOKEN_HERE"},
    json=data
)

print("Data:", data)

json_response = json.dumps(response.json(), indent=4)

print("Status:", response.status_code, "\n")
if response.status_code == 201:
    print("Success! SignRequest Created!" + "\n")
elif response.status_code == 400:
    print("Not found.")
print("Response: ", json_response)
