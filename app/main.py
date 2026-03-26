from app.services.restaurant_search_service import restaurantSearchService
from app.services.favorites_manager import FavoritesManager
from app.models.restaurant import Restaurant
from app.services.restaurant_scrapper import RestaurantScrapper

#service = restaurantSearchService("Madrid", "italian")

#response = service.transform_response(service.search())

#response = service.order_by_distance(response)


scrap = RestaurantScrapper()

html = scrap.get_page("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
soup = scrap.parse_page(html)
soup = scrap.extract_rating_count(soup)
print(soup)