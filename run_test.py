import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("OPENID_TOKEN")
RUNNER_URL = "https://www.certification.openid.net/api/runner"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

params = {
    "test": "oid4vp-1final-verifier-happy-flow",
    "plan": "RkhwBnodKb438"
}

response = requests.post(RUNNER_URL, headers=headers, params=params)
print("Status code:", response.status_code)
print(response.json())