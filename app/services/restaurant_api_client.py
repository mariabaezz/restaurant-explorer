api_key = "5ZZEZEVUGGB52RLGPMBHTUQH4EE5YY35EHXNKNK2R3W4OOVI"
import requests
class RestaurantApiClient:
    def __init__(self, api_key):
        self.base_url = "https://places-api.foursquare.com/places/search"
        self.api_key = api_key

    def search_restaurants(self, location, cuisine_type, limit=10):
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "X-Places-Api-Version": "2025-06-17"
        }

        params = {
            "query": cuisine_type,
            "near": location,
            "limit": limit,
        }

        try:
            response = requests.get(self.base_url, headers=headers, params=params, timeout=5)
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to Foursquare API: {e}")
            return "error"
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data from Foursquare API: {response.status_code} - {response.text}")
            return "error"