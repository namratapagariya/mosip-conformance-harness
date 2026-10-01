import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("OPENID_TOKEN")
TEST_ID = "eVJx7UBxRv9IlKV"  # jo pichhle step mein mila tha

INFO_URL = f"https://www.certification.openid.net/api/info/{TEST_ID}"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(INFO_URL, headers=headers)
print("Status code:", response.status_code)
print(response.json())