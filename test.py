import requests
import json


print("Testing the API")
# Create a test item
item = {
    'name': 'phone',
    'description': 'lost phone',
    'location': 'London'
}
# Use requests.post to create a new item
response = requests.post('http://127.0.0.1:5000/i', json=item)

# Create a test claim
claim = {
    'item_id': response.json()['uuid'],
    'name': 'John Doe',
    'email': 'no@thanks.com'
}

# Use requests.post to create a new claim
response = requests.post('http://127.0.0.1:5000/c', json=claim)

# Use requests.get to retrieve the claims
response = requests.get('http://127.0.0.1:5000/c')

# Print the claims
print(json.dumps(response.json(), indent=4))

# Use requests.get to retrieve the items
response = requests.get('http://127.0.0.1:5000/i')

# Print the items
print(json.dumps(response.json(), indent=4))