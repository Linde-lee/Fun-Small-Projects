import requests
from datetime import datetime

USERNAME = "lindlee"
TOKEN = "hukaljujujujuu"
GRAPH_ID = "graph1"

### Set up User:  ###
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#to check if I have created user
#response = requests.post(url=pixela_endpoint, json=user_parameters)
#print(response.text)

### Set up Graph:   ###
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Daily Meditation",
    "unit": "min",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)
# to see my graph: https://pixe.la/v1/users/lindlee/graphs/graph1.html

### Create a Pixel:  ###
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

post_pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you medidate today? ")
}

#response = requests.post(url=post_pixel_endpoint, json=post_pixel_data, headers=headers)
#print(response.text)

### Update a Pixel:  ###
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantify": "9"
}
#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

### Delete a Pixel:  ###
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#response = requests.delete(url=delete_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)