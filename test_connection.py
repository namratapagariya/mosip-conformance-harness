import requests

INJI_VERIFY_URL = "https://injiverify.collab.mosip.net"

response = requests.get(INJI_VERIFY_URL)
print("Status code:", response.status_code)
print("Reachable hai!" if response.status_code == 200 else "Kuch dikkat hai")