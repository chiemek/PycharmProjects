# an API is used to send and receive data from the internet

# rapid api it is a website that have a lot of api
import requests
import json

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"Lagos"}

headers = {
	"X-RapidAPI-Key": "1a33baa962mshfb43a9fba6d4ca8p11b28fjsn01da04d7daa9",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
result = response.json()

print(json.dumps(result, indent = 4))