import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("OPENID_TOKEN")
BASE_URL = "https://www.certification.openid.net/api/plan"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

params = {
    "planName": "oid4vp-1final-verifier-haip-test-plan",
    "variant": '{"credential_format": "sd_jwt_vc", "response_mode": "direct_post.jwt"}'
}

body = {
    "alias": "namrata-test"
}

response = requests.post(BASE_URL, headers=headers, params=params, json=body)
print("Status code:", response.status_code)
print(response.json())