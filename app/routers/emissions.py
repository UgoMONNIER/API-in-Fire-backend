from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.geocoding import geocoder_port
from app.services.routing import calculer_route
from app.services.emissions import calculer_emissions

router = APIRouter(tags=["Emissions"])

class EmissionRequest(BaseModel):
    depart: str
    arrivee: str
    cargo_tonnes: float = 10.0
    eviter_suez: bool = False

@router.post("/emissions")
def emissions(req: EmissionRequest):
    depart  = geocoder_port(req.depart)
    arrivee = geocoder_port(req.arrivee)

    if not depart:
        raise HTTPException(status_code=404, detail=f"Port '{req.depart}' introuvable")
    if not arrivee:
        raise HTTPException(status_code=404, detail=f"Port '{req.arrivee}' introuvable")

    route = calculer_route(depart, arrivee, req.eviter_suez)
    if not route:
        raise HTTPException(status_code=500, detail="Erreur calcul de route")

    emission = calculer_emissions(route, req.cargo_tonnes)

    return {
        "depart":       req.depart,
        "arrivee":      req.arrivee,
        "distance_km":  route.distance_km,
        "cargo_tonnes": req.cargo_tonnes,
        "co2e_kg":      emission.co2e_kg,
        "co2e_tonnes":  emission.co2e_tonnes,
        "intensite":    emission.intensite,
        "methode":      emission.methode,
    }