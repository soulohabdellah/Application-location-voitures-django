import json
import requests
from bs4 import BeautifulSoup
import re

url = "https://www.discovercars.com/fr/morocco?keyword=location%20voiture%20maroc&network=g&gclid=CjwKCAjw586hBhBrEiwAQYEnHeFSL-3_5SYsg8X5poNJrK4MpY6DHH7XKuE2f8XJYQgQXfQ904ZvCRoCsCQQAvD_BwE"
url2 = "https://www.discovercars.com/fr/morocco?keyword=location%20voiture%20maroc&network=g&gclid=CjwKCAjw586hBhBrEiwAQYEnHeFSL-3_5SYsg8X5poNJrK4MpY6DHH7XKuE2f8XJYQgQXfQ904ZvCRoCsCQQAvD_BwE"
response = requests.get(url2)
soup = BeautifulSoup(response.content, "html.parser")

car_list = soup.find_all("div", {"class": "col-xl-3 col-lg-4 col-md-6"})

cars = []

for car in car_list:
    car_name = car.find("div", {"class": "landing-cb-model ellipsis"}).text.strip()
    xcar_name = car_name.split()[:2]

    car_price = car.find("div", {"class": "landing-cb-price-block"}).text.strip()
    nombre = ""
    for c in car_price:
        if c.isdigit() or c == ".":
            nombre += c

    car_image = car.find("div", {"class": "landing-cb-car"}).find("img")["data-src"]
    car_info = car.find("div", {"class": "landing-cb-car-params"}).text.strip()
    # car_info_list = car_info.split('\n')
    car_info_list = re.sub('\n+', ' ', car_info)
    print(car_info_list)
    passengers = car_info_list[0]
    luggage = car_info_list[2]
    doors = car_info_list[4]
    ac = True if 'A/C' in car_info_list else False
    gearbox = 'automatic' if 'Auto' in car_info_list else 'manual'
    car_data = {
        "name": ' '.join(xcar_name),
        "price": float(nombre),
        "image": car_image,
        'passengers': passengers,
        'luggage': luggage,
        'doors': doors,
        'ac': ac,
        'gearbox': gearbox
    }
    cars.append(car_data)

with open("car_rentals.json", "w") as file:
    json.dump(cars, file, indent=4)
