class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = ''
        self.longitude = ''

    def set_latitude(self, lat):
        self.latitude = f"{lat}"

    def set_longitude(self, long):
        self.longitude = f"{long}"

    def __str__(self):
        result = ''
        result += f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
        return result
