import requests
try:
    response = requests.get("http://www.fmoviessss.com/")
except requests.exceptions.RequestException as e:
    print(e)

# print(response.status_code)