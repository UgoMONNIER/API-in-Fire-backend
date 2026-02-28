from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import geocoding, routing, emissions, vessel

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="Maritime routing, CO₂ emissions and vessel tracking API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(geocoding.router, prefix="/api")
app.include_router(routing.router,   prefix="/api")
app.include_router(emissions.router, prefix="/api")
app.include_router(vessel.router,    prefix="/api")

@app.get("/api/health")
def health():
    return {"status": "ok", "version": settings.version}