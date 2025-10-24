# http requests
# get is where we get data from the external system

# post is where we give the external system data

import requests
import datetime as dt
USERNAME = "bahsounm"
TOKEN = "0987654321"

date_today = dt.datetime.now()
formatted_date = str(date_today.year) + str(date_today.month) + str(date_today.day)

pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
    }
# aftrer creating a user there is no need for this anymore
# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

# creating our grpah
graph_endpoint = "https://pixe.la/v1/users/{}/graphs".format(USERNAME)

graph_params = {
    "id": "graph1",
    "name": "Podcast Graph",
    "unit": "episode",
    "type": "int",
    "color": "ajisai"
}

# how we can authenticate ourselves
headers = {"X-USER-TOKEN": TOKEN}

# aftrer creating a user there is no need for this anymore
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


# creating a new pixzel on our graph
record_enpoint = "https://pixe.la/v1/users/{}/graphs/{}".format(USERNAME, graph_params["id"])

record_param = {
    "date": formatted_date,
    "quantity": "1"
}
# response = requests.post(url=record_enpoint, headers=headers, json=record_param)
# print(response.text)

# put will change an exsting piece of data
update_data_enpoint = "https://pixe.la/v1/users/{}/graphs/{}/{}".format(USERNAME, graph_params["id"],formatted_date)

update_data_param = {
    "quantity": "3"
}

# response = requests.put(url=update_data_enpoint,json= update_data_param, headers=headers)
# print(response.text)
# delete will delete a piece of data

delete_data_enpoint = "https://pixe.la/v1/users/{}/graphs/{}/{}".format(USERNAME, graph_params["id"],formatted_date)

response = requests.delete(url=delete_data_enpoint, headers=headers)
print(response.text)