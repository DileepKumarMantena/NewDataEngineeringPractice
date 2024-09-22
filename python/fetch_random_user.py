import requests
import json

url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    users = data['results']    
    for i, user in enumerate(users, 1):
        name = user['name']
        location = user['location']
        print(f"User {i}:")
        print(f"  Name: {name['first']} {name['last']}")
        print(f"  Gender: {user['gender']}")
        print(f"  Age: {user['dob']['age']}")
        print(f"  Email: {user['email']}")
        print(f"  Location: {location['city']}, {location['country']}")
        print(f"  Phone: {user['phone']}")
        print(f"  Picture: {user['picture']['large']}")
        print("-" * 30)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
