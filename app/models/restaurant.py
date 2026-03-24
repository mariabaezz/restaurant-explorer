class Restaurant:
    def __init__(self, name, location, distance, cuisine_type, telephone=None):
        self.name = name

        self.location = location
        self.distance = distance
        self.cuisine_type = cuisine_type
        self.telephone = telephone

    def __repr__(self):
        return f"Restaurant(name={self.name}, location={self.location}, distance={self.distance}, cuisine_type={self.cuisine_type}, telephone={self.telephone})"