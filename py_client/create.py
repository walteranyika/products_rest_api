import requests
from faker import Faker

endpoint = "http://127.0.0.1:8000/api/products/"
faker = Faker()
data = {
    "title": faker.name(),
    "price": faker.random_int()

}
get_response = requests.post(endpoint, json=data)
print(get_response.json())
