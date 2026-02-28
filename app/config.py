from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "API Under Fire — Searoutes Platform"
    version: str = "1.0.0"
    nominatim_url: str = "https://nominatim.openstreetmap.org/search"
    http_user_agent: str = "api-under-fire/1.0"
    vessel_speed_knots: float = 14.0
    co2_kg_per_tonne_km: float = 0.015
    cache_ttl_port: int = 86400 * 30
    cache_ttl_route: int = 86400
    cache_ttl_vessel: int = 300

settings = Settings()