import requests
import json
import base64

UTF8 = "utf-8"
PDF_NAME = "demo_document.pdf"

# first: reading the binary stuff
# note the 'rb' flag
# result: bytes
with open("demo_document.pdf", "rb") as pdf_content:
    pdf_byte_content = pdf_content.read()

# second: base64 encode read data
# result: bytes
encoded_pdf = base64.b64encode(pdf_byte_content)

# third: decode these bytes to text
# result: string (in utf-8)
pdf_base64_string = encoded_pdf.decode(UTF8)

json_data = {
    # "file_from_url" : "your_url", 
    # do not use file_from_url simultaneously with file_from_content
    "signers": [{"email": "name@provider.com", "order": 0}, {"email": "name+1@provider.com", "order": 1}],
    "file_from_content": pdf_base64_string,
    "file_from_content_name": PDF_NAME,
    "name": PDF_NAME,
    "from_email": "name@provider.com",
    "message": "Please sign this document - Test",
    "subject": "SignTest - YourTeam API - Python",
    "who": "mo",
    "auto_delete_days": 1
    # Add other parameters here
}

response = requests.post(
    "https://yourteam.signrequest.com/api/v1/signrequest-quick-create/",
    headers={"Authorization": "Token YOUR_TOKEN_HERE"},
    json=json_data
)

print("Data:", json_data, "\n")

json_response = json.dumps(response.json(), indent=4)

print("Status:", response.status_code, "\n")
if response.status_code == 201:
    print("Success! SignRequest Created!" + "\n")
elif response.status_code == 400:
    print("Not found.")
print("Response: ", json_response)
