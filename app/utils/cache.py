import time

class Cache:
    def __init__(self):
        self._store = {}

    def get(self, key: str):
        if key in self._store:
            value, expires_at = self._store[key]
            if time.time() < expires_at:
                return value
            del self._store[key]
        return None

    def set(self, key: str, value, ttl: int):
        self._store[key] = (value, time.time() + ttl)

    def clear(self):
        self._store = {}

cache = Cache()