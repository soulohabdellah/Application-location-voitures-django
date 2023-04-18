import json
import requests
from bs4 import BeautifulSoup

url = "https://www.discovercars.com/fr/morocco?keyword=location%20voiture%20maroc&network=g&gclid=CjwKCAjw586hBhBrEiwAQYEnHeFSL-3_5SYsg8X5poNJrK4MpY6DHH7XKuE2f8XJYQgQXfQ904ZvCRoCsCQQAvD_BwE"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

car_list = soup.find_all("div", {"class": "col-xl-3 col-lg-4 col-md-6"})

cars = []

for car in car_list:
    car_name = car.find("div", {"class": "landing-cb-class ellipsis"}).text.strip()
    car_price = car.find("div", {"class": "landing-cb-info"}).text.strip()
    car_image = car.find("div", {"class": "landing-cb-car"}).find("img")["src"]
    car_data = {
        "name": car_name,
        "price": car_price,
        "image": car_image
    }
    cars.append(car_data)

with open("car_rentals.json", "w") as file:
    json.dump(cars, file)
