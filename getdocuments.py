import requests
import json

response = requests.get(
    "https://yourteam.signrequest.com/api/v1/documents/",
    headers={"Authorization": "Token YOUR_TOKEN_HERE"}
)

json_response = json.dumps(response.json(), indent=4)

print("Status:", response.status_code, "\n")
if response.status_code == 200:
    print("Success!" + "\n")
elif response.status_code == 404:
    print("Not found.")
print("Response: ", str(json_response))
