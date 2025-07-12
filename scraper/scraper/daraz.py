import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_daraz(query="headphones", pages=1):
    results = []
    for page in range(1, pages + 1):
        url = f"https://www.daraz.com.bd/catalog/?q={query}&page={page}"
        res = requests.get(url, headers={"user-agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.find_all("div", class_="gridItem--Yd0sa")
        
        for item in items:
            title = item.find("div", class_="title--wFj93")
            price = item.find("span", class_="price--NVB62")
            if title and price:
                results.append({
                    "title": title.get_text(strip=True),
                    "price": int(price.get_text(strip=True).replace("৳", "").replace(",", "")),
                    "category": query.title(),
                    "source": "Daraz"
                })
    return pd.DataFrame(results)
