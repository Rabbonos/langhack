import requests
import base64


def main(prompt:str, api_key:str):

    base_url='https://api.aimlapi.com'

    headers = {
        "Authorization": 'Bearer '+api_key,
    }

    payload = {
        "prompt": prompt,
        "model": "stabilityai/stable-diffusion-xl-base-1.0",
    }

    response = requests.post(
        "https://api.aimlapi.com/images/generations/with-url", headers=headers, json=payload
    )

    relative_url=response.json()["output"]["choices"][0]["url"]
    full_url=base_url+relative_url

    return full_url


print(main('a cucumber in the shape of a star', '12011d66443b471d8d5d7d91cc5320ea'))