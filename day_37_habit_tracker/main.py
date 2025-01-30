import requests
import datetime

USERNAME = "USERNAME"
TOKEN = "TOKEN"

# Create account.

pixela_parameters = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url="https://pixe.la/v1/users", json=pixela_parameters)

# Create graph.

graph_config = {
    "id":"graph1",
    "name":"Book Reading Graph",
    "unit":"minutes",
    "type":"float",
    "color":"momiji",
}
header = {
    "X-USER-TOKEN":TOKEN,
}

# graph_response = requests.post(url="https://pixe.la/v1/users/fatih123/graphs", json=graph_config, headers=header)

# Add a pixel.

now = datetime.datetime.now()
a_date = datetime.datetime(2025,1,29)

pixel_config = {
    "date":a_date.strftime("%Y%m%d"),
    "quantity":input("How long did you read books? "),
}

# pixel_response = requests.post(url="https://pixe.la/v1/users/fatih123/graphs/graph1", json=pixel_config, headers=header)

# Update a pixel.

pixel_update = {
    "quantity":input("How long did you read books? "),
}

pixel_update_response = requests.put(url="https://pixe.la/v1/users/fatih123/graphs/graph1/20250129", json=pixel_update, headers=header)
print(pixel_update_response.text)