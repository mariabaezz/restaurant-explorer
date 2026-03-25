import requests
import BeautifulSoup
class RestaurantScrapper:
    def __init__(self):
        pass

    def get_page(self, url):
        if not url:
            return "error"
        try:
            response = requests.get(url)
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