# SignRequest API - Python Client - Lite

Client developed to make GET and POST requests to SignRequest's API.

## Getting Started:

Register a team in https://signrequest.com/#/ and generate a Token.

-Make sure you have Python3 installed in your computer:
https://www.python.org/

-Install Requests library running ```pip3 install requests``` in your shell. 

### getdocuments.py

With this file it is possible to make GET requests to ```/documents/``` using your team's credentials.

## Create Documents:

### createdocs.py

With this file it is possible to send POST requests to ```/documents/``` so that you can create new documents at SignRequest's API. 

1. Add your team's subdomain in ```response```.
2. Add your document's data.
i) Fill the header with your Token at "your_token_here".
3. Run the code with ```python3 createdocs.py```.

## Create a Sign Request:

### createsignrequest.py

With this file it is possible to send POST requests to ```/signrequests/``` so that you can generate new sign requests at SignRequest's API.

1. Add your team's subdomain in ```response```.

**DATA OBJECT:** 

2. Add your newly created document in data.document.
3. Add the signers information in data.signers[].
4. Add the sender e-mail address at "from_email".
5. Add your customized message.
6. Add any additional information in the Data Object, such as "who" needs to sign or subject.
7. Add your team's Token at the header.

For more information check the documentation for the "/signrequests/" endpoint.

https://signrequest.com/api/v1/docs/#tag/signrequests

### quickcreatesr.py 

With this file it is possible to create a new document while sending a POST request to ```signrequest-quick-create```.