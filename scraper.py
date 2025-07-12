import pandas as pd

def get_sample_data():
    return pd.DataFrame({
        "title": ["Phone A", "Shoes B", "Laptop C", "Shirt D"],
        "price": [1200, 800, 55000, 1300],
        "category": ["Electronics", "Footwear", "Electronics", "Fashion"]
    })