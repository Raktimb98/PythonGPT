import requests
import json

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyCdEK_PQtYgIoyOb1UmrxUakQjPH0SpSXo"

headers = {
    'Content-Type': 'application/json'
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "creat a link of beautiful image of cow"
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())
