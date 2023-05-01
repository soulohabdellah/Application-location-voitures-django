from bs4 import BeautifulSoup

html = '''
<div class="landing-cb-car">
    <img src="https://www.discovercars.com/images/car/8000/150.png" data-src="https://www.discovercars.com/images/car/8000/150.png" data-url="https://www.discovercars.com/fr/search/search-box-in-modal/morocco" width="150" alt="Chevrolet Spark" title="Chevrolet Spark" class="trigger-gtm-cheapest open-pick-modal cb-img lazyloaded" data-event-action="Image" data-event-label="WheeGo">
</div>
'''

soup = BeautifulSoup(html, "html.parser")

div_element = soup.find("div", class_="landing-cb-car")
img_element = div_element.find("img")
image_url = img_element["src"]

print(image_url)
