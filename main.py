import requests
import datetime

TOKEN = 'a;sldjfqpoweriupt'
USER_NAME = 'nozomu'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token':TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs'
graph_config = {
    'id': GRAPH_ID,
    'name': '100 Days of Python Graph',
    'unit': 'times',
    'type': 'int',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# today = datetime.datetime.now()
today = datetime.datetime(year=2021, month=9, day=11)
today = today.strftime('%Y%m%d')
print(today)

pixel_creation_endpoint = f'{graph_endpoint}/{GRAPH_ID}'
pixel_data = {
    'date': today,
    'quantity': '2',
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_update_endpoint = f'{pixel_creation_endpoint}/{today}'

pixel_update_data = {
    'quantity': '5',
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

response = requests.delete(url=pixel_update_endpoint, headers=headers)
print(response.text)