import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_rokomari(query="book", pages=1):
    results = []
    for page in range(1, pages + 1):
        url = f"https://www.rokomari.com/book/search?term={query}&page={page}"
        res = requests.get(url, headers={"user-agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.find_all("div", class_="book-list-wrapper")

        for item in items:
            title = item.find("p", class_="book-title")
            price = item.find("p", class_="book-price")
            if title and price:
                results.append({
                    "title": title.get_text(strip=True),
                    "price": int(price.get_text(strip=True).replace("৳", "").replace(",", "")),
                    "category": query.title(),
                    "source": "Rokomari"
                })
    return pd.DataFrame(results)
