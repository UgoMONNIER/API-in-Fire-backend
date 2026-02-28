from fastapi import APIRouter, HTTPException, Query
from app.services.geocoding import geocoder_port

router = APIRouter(tags=["Geocoding"])

@router.get("/geocoding")
def geocoding(q: str = Query(..., description="Nom du port")):
    port = geocoder_port(q)
    if not port:
        raise HTTPException(status_code=404, detail=f"Port '{q}' introuvable")
    return port