from pydantic import BaseModel
from app.models.port import Port

class Route(BaseModel):
    depart: Port
    arrivee: Port
    distance_km: float
    duree_heures: float
    geojson: dict
    eviter_suez: bool = False
    eviter_hra: bool = False

    @property
    def duree_jours(self) -> float:
        return self.duree_heures / 24

    @property
    def points_gps(self) -> int:
        return len(self.geojson.get("coordinates", []))