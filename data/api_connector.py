import requests
from config.settings import API_KEY, BASE_URL

def obtener_datos(endpoint):
    headers = {"x-apisports-key": API_KEY}
    url = f"{BASE_URL}/{endpoint}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"⚠️ Error al obtener datos desde la API: {e}")
        return None
