import requests
import json

data = {
    "file_from_url": "your_file_url_here",
    "signers": [
        {
            "email": "name+1@provider.com"
        },
        {
            "email": "name+2@provider.com"
        }
    ],
    "from_email": "name@provider.com",
    "message": "Please sign this document - Test",
    "subject": "SignTest - YourTeam API - Python",
    "who": "o",
    "auto_delete_days": 1
    # Add other parameters here
}

response = requests.post(
    "https://yourteam.signrequest.com/api/v1/signrequest-quick-create/",
    headers={"Authorization": "Token YOUR_TOKEN_HERE"},
    json=data
)

print("Data:", data, "\n")

json_response = json.dumps(response.json(), indent=4)

print("Status:", response.status_code, "\n")
if response.status_code == 201:
    print("Success! SignRequest Created!" + "\n")
elif response.status_code == 400:
    print("Not found.")
print("Response: ", json_response)
