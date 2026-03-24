from app.models.restaurant import Restaurant
from app.services.restaurant_api_client import RestaurantApiClient, api_key
import json

class restaurantSearchService:
    def __init__(self, city, cuisine_type):
        self.city = city
        self.cuisine_type = cuisine_type
    
    def search(self):

        api_client = RestaurantApiClient(api_key)
        response = api_client.search_restaurants(self.city, cuisine_type=self.cuisine_type)
        

        if response == "error":
            return "error"
        return response
    
    def transform_response(self, response):
        restaurants = []
        for item in response["results"]:
            name = item['name']
            location = item['location']['formatted_address']
            cuisine_type = item['categories'][0]['short_name']
            distance = item.get('distance', 'N/A')
            telephone = item.get('tel', 'N/A')
            
            restaurants.append(Restaurant(name=name, location=location, cuisine_type=cuisine_type, distance=distance, telephone=telephone))
        return restaurants

    def order_by_distance(self, restaurants):
        for restaurant in restaurants:
            if restaurant.distance == 'N/A':
                restaurant.distance = float('inf')
        return sorted(restaurants, key=lambda x: x.distance)
    
