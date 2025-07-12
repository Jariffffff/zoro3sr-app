import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_pickaboo(query="headphones", pages=1):
    results = []
    for page in range(1, pages + 1):
        url = f"https://www.pickaboo.com/search?q={query}&page={page}"
        res = requests.get(url, headers={"user-agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.find_all("div", class_="product-details")
        
        for item in items:
            title = item.find("a", class_="product-title")
            price = item.find("span", class_="price")
            if title and price:
                results.append({
                    "title": title.get_text(strip=True),
                    "price": int(price.get_text(strip=True).replace("৳", "").replace(",", "")),
                    "category": query.title(),
                    "source": "Pickaboo"
                })
    return pd.DataFrame(results)
