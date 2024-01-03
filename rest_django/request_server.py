import requests
import cloudscraper

crs = cloudscraper.create_scraper()



r = requests.get("http://127.0.0.1:8000/great", params={"abc":123, "22":321})

print(crs.get("http://127.0.0.1:8000/great").text)
