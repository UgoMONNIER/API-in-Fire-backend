from app.models.route import Route
from app.models.emission import Emission
from app.config import settings

def calculer_emissions(route: Route, cargo_tonnes: float = 10.0) -> Emission:
    co2e_kg = route.distance_km * cargo_tonnes * settings.co2_kg_per_tonne_km
    return Emission(
        co2e_kg=co2e_kg,
        cargo_tonnes=cargo_tonnes,
        distance_km=route.distance_km
    )