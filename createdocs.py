import requests
import json
import base64

PDF_NAME = "demo_document.pdf"

pdf = open("demo_document.pdf", "rb").read()
encodedPdf = base64.b64encode(pdf)

#print("Original PDF: ", pdf)
#print("Encoded PDF: ", encodedPdf)

response = requests.post(
    "https://yourteam.signrequest.com/api/v1/documents/",
    headers={"Authorization": "Token YOUR_TOKEN_HERE"},
    data={
        # "file_from_url" : "your_url",
        # do not use file_from_url simultaneously with file_from_content
        "file_from_content": encodedPdf,
        "file_from_content_name": PDF_NAME,
        "name": PDF_NAME,
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
