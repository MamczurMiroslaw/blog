import requests

# defining URL
url = 'http://127.0.0.1:8080/rebuild'

# my sending data
data = {
    "test_size": 0.9
}

# declaring headers
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# sending request
response = requests.post(url, json=data, headers=headers)

# printing answer as json
print(response.json())
