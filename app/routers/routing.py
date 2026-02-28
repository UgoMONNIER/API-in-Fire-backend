from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.geocoding import geocoder_port
from app.services.routing import calculer_route

router = APIRouter(tags=["Routing"])

class RouteRequest(BaseModel):
    depart: str
    arrivee: str
    eviter_suez: bool = False
    eviter_hra: bool = False

@router.post("/route")
def route(req: RouteRequest):
    depart  = geocoder_port(req.depart)
    arrivee = geocoder_port(req.arrivee)

    if not depart:
        raise HTTPException(status_code=404, detail=f"Port '{req.depart}' introuvable")
    if not arrivee:
        raise HTTPException(status_code=404, detail=f"Port '{req.arrivee}' introuvable")

    route = calculer_route(depart, arrivee, req.eviter_suez, req.eviter_hra)
    if not route:
        raise HTTPException(status_code=500, detail="Erreur calcul de route")

    return {
        "depart":       depart,
        "arrivee":      arrivee,
        "distance_km":  route.distance_km,
        "distance_nm":  round(route.distance_km / 1.852, 2),
        "duree_heures": route.duree_heures,
        "duree_jours":  route.duree_jours,
        "geojson":      route.geojson,
        "eviter_suez":  route.eviter_suez,
    }