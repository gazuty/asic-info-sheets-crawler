import requests

URL = "https://asic.gov.au/regulatory-resources/regulatory-resources-search/?filter=document&sort=lastUpdated&superseded=false&type=information+sheet"
r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)

print("status:", r.status_code)
print("length:", len(r.text))
print("first_200:", r.text[:200])
