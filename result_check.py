import requests

url = "http://10.52.190.146:5000/predict"  # Update IP if deployed remotely
data = {
    "features": [5.1, 3.5, 1.4, 0.2]  # Modify based on your model's requirements
}

response = requests.get(url, json=data)
print(response.json())  # Expected output: {'prediction': <some_value>}
