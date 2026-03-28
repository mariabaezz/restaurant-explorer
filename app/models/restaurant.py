class Restaurant:
    def __init__(self, fsq_place_id, name, location, distance, cuisine_type, telephone=None, rating=None):
        self.fsq_place_id = fsq_place_id
        self.name = name

        self.location = location
        self.distance = distance
        self.cuisine_type = cuisine_type
        self.telephone = telephone
        self.rating = rating

    def __repr__(self):
        return f"Restaurant(name={self.name}, location={self.location}, distance={self.distance}, cuisine_type={self.cuisine_type}, telephone={self.telephone}, rating={self.rating})"
    
    def to_dict(self):
        return {
            "fsq_place_id": self.fsq_place_id,
            "name": self.name,
            "location": self.location,
            "distance": self.distance,
            "cuisine_type": self.cuisine_type,
            "telephone": self.telephone,
            "rating": self.rating
        }