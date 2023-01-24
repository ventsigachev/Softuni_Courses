class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = None
        self.longitude = None

    def set_latitude(self, lat):
        self.latitude = lat

    def set_longitude(self, long):
        self.longitude = long

    def __str__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
