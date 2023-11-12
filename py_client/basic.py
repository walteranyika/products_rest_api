import requests

#
# endpoint = "https://httpbin.org/status/bin"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.post(endpoint, json={"name": "John Mark"}, params={"abc": 123})
# get_response = requests.get(endpoint, json={"name": "John Mark"})
get_response = requests.post(endpoint, json={"description": "Uji Mix"})
#
# print(get_response.json())

# https://www.youtube.com/watch?v=c708Nf0cHrs

# get_response = requests.get(endpoint)

print(get_response.content)
