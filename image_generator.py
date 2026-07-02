import requests
from config import HF_TOKEN, MODEL_URL


headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def generate_image(prompt):

    payload = {
        "inputs": prompt
    }

    response = requests.post(
        MODEL_URL,
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        raise Exception(response.text)

    return response.content