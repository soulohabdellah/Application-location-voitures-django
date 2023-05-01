import json
import base64
import re

# Load data from JSON file
with open("car_rentals.json", "r") as file:
    data = json.load(file)

# Access car rental information
for car in data:
    car_name = car["name"]
    car_price = car["price"]
    car_image_data = car["image"]
    car_info = car["info"]

    # Clean car name for use as file name
    clean_car_name = re.sub(r"[^\w\s-]", "", car_name)
    clean_car_name = re.sub(r"\s+", "_", clean_car_name)
    clean_car_name = re.sub(r"-+", "_", clean_car_name)

    # Decode and save the image
    image_data = base64.b64decode(car_image_data.split(",")[1])
    with open(f"{clean_car_name}.png", "wb") as image_file:
        image_file.write(image_data)

    # Process the car rental information as needed
    print(car_name, car_price, car_info)
