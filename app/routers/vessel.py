from fastapi import APIRouter, HTTPException
from app.services.vessel import get_vessel

router = APIRouter(tags=["Vessel"])

@router.get("/vessel/{imo}")
def vessel(imo: str):
    v = get_vessel(imo)
    if not v:
        raise HTTPException(status_code=404, detail=f"Navire IMO '{imo}' introuvable")
    return v