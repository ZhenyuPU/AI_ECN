
class Avion:
    def __init__(self, icao24=None, longitude=None, latitude=None, geo_altitude=None, on_ground=False,
                 velocity=None, true_track=None, vertical_rate=None):
        
        self.icao24 = icao24

        # longitude, latitude, geo_latitude
        longitude = longitude
        latitude = latitude
        geo_altitude = geo_altitude
        on_ground = on_ground

        self.position = [longitude, latitude, geo_altitude, on_ground]

        self.vitesse = velocity

        true_track = true_track
        vertical_rate = vertical_rate

        self.orietation = [true_track, vertical_rate]


    def __str__(self):
        return f"ICAO24: {self.icao24}, position: {self.position}, Velocities: {self.vitesse}, Orietation: {self.orietation}"
    
        
    def __len__(self):
        return len(self.states)


    


