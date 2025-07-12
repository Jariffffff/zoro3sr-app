from scraper.daraz import scrape_daraz
from scraper.pickaboo import scrape_pickaboo
from scraper.rokomari import scrape_rokomari

def scrape_all(query: str, source: str = "daraz", pages: int = 1):
    if source == "daraz":
        return scrape_daraz(query, pages)
    elif source == "pickaboo":
        return scrape_pickaboo(query, pages)
    elif source == "rokomari":
        return scrape_rokomari(query, pages)
    else:
        raise ValueError("❌ Unsupported source selected")
