api_key = "ZZSTO04KMZDL5HPL2DQKQNJBT1LOXUKASMIJNKJ5KPNLLY5F"
import requests
class RestaurantApiClient:
    def __init__(self, api_key):
        self.base_url = "https://api.foursquare.com/v3/places/search"
        self.api_key = api_key

    def search_restaurants(self, location, radius=1000, limit=10):
        headers = {
            "Accept": "application/json",
            "Authorization": self.api_key
        }
        params = {
            "query": "restaurant",
            "ll": location,
            "radius": radius,
            "limit": limit
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