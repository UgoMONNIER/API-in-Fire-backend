from pydantic import BaseModel

class Port(BaseModel):
    nom: str
    latitude: float
    longitude: float

    def coordonnees(self) -> list[float]:
        return [self.longitude, self.latitude]