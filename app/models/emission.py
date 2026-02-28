from pydantic import BaseModel

class Emission(BaseModel):
    co2e_kg: float
    cargo_tonnes: float
    distance_km: float
    methode: str = "GLEC v3"

    @property
    def co2e_tonnes(self) -> float:
        return self.co2e_kg / 1000

    @property
    def intensite(self) -> float:
        if self.distance_km and self.cargo_tonnes:
            return self.co2e_kg / (self.distance_km * self.cargo_tonnes)
        return 0.0