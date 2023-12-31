import requests

r = requests.get("http://127.0.0.1:8000/great", params={"abc":123})

print(r.json())
