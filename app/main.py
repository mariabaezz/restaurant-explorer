from app.services.restaurant_search_service import restaurantSearchService

service = restaurantSearchService("Madrid", "italian")

response = service.transform_response(service.search())

print(response)