import requests
from bs4 import BeautifulSoup

# pull item data from page link
def scrape_item(link):
    data = requests.get(link)
    soup = BeautifulSoup(data.text, "html.parser")

    # gather item name/details
    item_name = ""
    h2 = soup.select_one(".food-storage-container h2")
    if h2:
        item_name = h2.get_text(strip=True)

    print("Item" + item_name)

    # gather item stats
    def get_time(type):
        div = soup.select_one(f".food-inside {type}")
        if not div:
            return ""
        sibling = div.find_next_sibling("div", class_="food-storage-right")
        if not sibling:
            return ""
        span = sibling.select_one(".red-image span")
        if not span:
            return ""
        return span.get_text(strip=True)
    
    pantry = get_time(".pantryimg1")
    fridge = get_time(".pantryimg2")
    freezer = get_time(".pantryimg3")

    print("Pantry: " + pantry)
    print("Fridge: " + fridge)
    print("Freezer: " + freezer)

    return 0

scrape_item("https://stilltasty.com/Fooditems/index/16402")
scrape_item("https://stilltasty.com/fooditems/index/18411")