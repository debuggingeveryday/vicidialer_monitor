import requests

def fetch_data(url, headers):
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()  # Raise an error if status code is not 200
        return response.text
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)