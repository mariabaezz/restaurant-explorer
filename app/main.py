from app.services.restaurant_search_service import restaurantSearchService
from app.services.favorites_manager import FavoritesManager
from app.models.restaurant import Restaurant

service = restaurantSearchService("Madrid", "italian")

response = service.transform_response(service.search())

response = service.order_by_distance(response)



favorites = FavoritesManager()

favorites.add_favorite(response[0])
favorites.save_favorites()

favorites.load_favorites()

for fav in favorites.favorites:
    print(fav)