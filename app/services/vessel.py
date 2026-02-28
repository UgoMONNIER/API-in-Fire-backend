import random
from app.config import settings

VESSELS_MOCK = {
    "9811000": {"nom": "Ever Given",         "pavillon": "Panama",  "vitesse": 12.3, "cap": 245},
    "9454448": {"nom": "CMA CGM Marco Polo", "pavillon": "France",  "vitesse": 14.1, "cap": 112},
    "9703291": {"nom": "MSC Oscar",          "pavillon": "Panama",  "vitesse": 15.2, "cap": 78},
    "9164263": {"nom": "Maersk Alabama",     "pavillon": "USA",     "vitesse": 13.8, "cap": 190},
}

def get_vessel(imo: str) -> dict | None:
    if imo in VESSELS_MOCK:
        v = VESSELS_MOCK[imo]
        return {
            "imo":      imo,
            "nom":      v["nom"],
            "pavillon": v["pavillon"],
            "vitesse":  v["vitesse"] + random.uniform(-0.5, 0.5),
            "cap":      v["cap"],
            "latitude":  random.uniform(-10, 50),
            "longitude": random.uniform(-20, 120),
            "statut":   "En route",
        }
    return None