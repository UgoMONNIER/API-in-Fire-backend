import requests
from app.models.port import Port
from app.utils.cache import cache
from app.config import settings

def geocoder_port(nom: str) -> Port | None:
    cached = cache.get(f"port:{nom}")
    if cached:
        return cached

    try:
        response = requests.get(
            settings.nominatim_url,
            params={"q": nom, "format": "json", "limit": 1},
            headers={"User-Agent": settings.http_user_agent},
            timeout=5
        )
        response.raise_for_status()
        data = response.json()

        if not data:
            return None

        port = Port(
            nom=nom,
            latitude=float(data[0]["lat"]),
            longitude=float(data[0]["lon"])
        )

        cache.set(f"port:{nom}", port, settings.cache_ttl_port)
        return port

    except requests.RequestException as e:
        print(f"❌ Erreur geocoding {nom}: {e}")
        return None