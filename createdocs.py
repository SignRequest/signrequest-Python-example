import requests
import json
import base64

response = requests.post(
    "https://yourteam.signrequest.com/api/v1/documents/",
    headers={"Authorization": "Token YOUR_TOKEN_HERE"},
    data={
        "file_from_url": 'your_url_here',
        "auto_delete_days": 1
        # Add other parameters here
    }
)

json_response = json.dumps(response.json(), indent=4)

print("Status:", response.status_code, "\n")
if response.status_code == 201:
    print("Success! Document Created!" + "\n")
elif response.status_code == 404:
    print("Not found.")
print("Response: ", str(json_response))
