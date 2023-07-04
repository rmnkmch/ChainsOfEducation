class CacheDatabase(object):
    """Base of cached data"""

    def __init__(self) -> None:
        self.data: dict[str] = {}

    def get(self, key: str):
        if key in self.data.keys():
            return self.data[key]
        return None

    def add(self, key: str, value):
        self.data[key] = value

    def clear(self):
        self.data.clear()
