import json
from app.models.restaurant import Restaurant


class FavoritesManager:
    def __init__(self):
        self.favorites = []

    def add_favorite(self, restaurant):
        for fav in self.favorites:
            if fav.fsq_place_id == restaurant.fsq_place_id:
                return False
        self.favorites.append(restaurant)
        return True

    def save_favorites(self, filename="data/favorites.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([restaurant.to_dict() for restaurant in self.favorites], f, indent=4, ensure_ascii=False)

    def load_favorites(self, filename="data/favorites.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.favorites = [Restaurant(**item) for item in data]
        except FileNotFoundError:
            self.favorites = []

    def remove_favorite(self, fsq_place_id):
        self.favorites = [
            restaurant for restaurant in self.favorites
            if restaurant.fsq_place_id != fsq_place_id
        ]