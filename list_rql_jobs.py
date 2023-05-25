import requests

url = "https://api.rollbar.com/api/1/rql/jobs/?page=1"

headers = {
    "accept": "application/json",
    "X-Rollbar-Access-Token": "PROD_READ_TOKEN"
}

response = requests.get(url, headers=headers)

print(response.text)
