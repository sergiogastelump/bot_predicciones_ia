import requests
from config.settings import API_KEY, BASE_URL

def obtener_datos(endpoint):
    """
    Llama a la API de sports. Por ahora lo dejamos genérico.
    """
    headers = {"x-apisports-key": API_KEY}
    url = f"{BASE_URL}/{endpoint}"
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"⚠️ Error al obtener datos desde la API: {e}")
        return None
