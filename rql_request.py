import requests

url = "https://api.rollbar.com/api/1/rql/jobs/"

payload = {
    "force_refresh": False,
    "query_string": "SELECT * FROM item_occurrence WHERE item.counter IN (1,2,3)"
}
headers = {
    "accept": "application/json",
    "X-Rollbar-Access-Token": 'PROD_READ_TOKEN',
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
