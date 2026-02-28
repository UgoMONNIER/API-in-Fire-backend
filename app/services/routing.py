import searoute as sr
from app.models.port import Port
from app.models.route import Route
from app.utils.cache import cache
from app.config import settings

def calculer_route(
    depart: Port,
    arrivee: Port,
    eviter_suez: bool = False,
    eviter_hra: bool = False
) -> Route | None:
    cache_key = f"route:{depart.nom}:{arrivee.nom}:{eviter_suez}:{eviter_hra}"
    cached = cache.get(cache_key)
    if cached:
        return cached

    try:
        result = sr.searoute(
            depart.coordonnees(),
            arrivee.coordonnees(),
            units="km",
            speed_knot=settings.vessel_speed_knots,
        )

        route = Route(
            depart=depart,
            arrivee=arrivee,
            distance_km=result["properties"]["length"],
            duree_heures=result["properties"]["duration_hours"],
            geojson=result["geometry"],
            eviter_suez=eviter_suez,
            eviter_hra=eviter_hra
        )

        cache.set(cache_key, route, settings.cache_ttl_route)
        return route

    except Exception as e:
        print(f"❌ Erreur routing: {e}")
        return None