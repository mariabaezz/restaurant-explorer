import requests
from bs4 import BeautifulSoup
class RestaurantScrapper:
    def __init__(self):
        pass

    def get_page(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        }

        if not url:
            return "error"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            if response.status_code != 200:
                print(f"Error fetching page: {response.status_code}")
                return "error"
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return "error"
        return response.text
    
    def parse_page(self, html):
        if not html:
            return "error"
        soup = BeautifulSoup(html, 'html.parser')

        return soup

    def extract_rating_count(self, soup):
        if not soup:
            return "error"

        rating_tag = soup.find("p", class_="star-rating")
        if not rating_tag:
            print("Rating tag not found")
            return "N/A"

        rating_class = rating_tag["class"][1]

        mapping = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }

        rating = mapping.get(rating_class, "N/A")
        return rating
