# Setup requests library
import requests
import json
import os

# Create url link to the crawl location
url = "https://tiki.vn/api/personalish/v1/blocks/listings"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
}

params = {
    "limit": 12,
    "include": "advertisement",
    "is_mweb": 1,
    "aggregations": 2,
    "version": "home-persionalized",
    "_v": "within_promotions",
    "trackity_id": "9910f7f4-4ee4-00c0-9a7a-636f88e1ccd3",
    "urlKey": "laptop-may-vi-tinh-linh-kien",
    "categoryId": 1846,
    "category": 1846,
    "page": 1
}

product_list = []

# Get data by page
for i in range(1, 4):
    params["page"] = i
    response = requests.get(url, headers=headers,params=params)
    
    if response.status_code == 200:
        # print(response.json().get("data"))
        
        print("-----GET DATA FROM PAGE {}-----".format(params["page"]))
        for product in response.json().get("data"):
            product_data = {
                "id": product["id"],
                "name": product["name"],
                "brand_name": product["brand_name"],
                "price": product["price"],
                "thumbnail": product["thumbnail_url"],
                "review_count": product["review_count"],
                "rating_average": product["rating_average"]
            }
            
            # print(product["name"] + ": " + str(product["price"]))
            product_list.append(product_data)
        
# Write data to json file
with open("product_data.json", 'w', encoding='utf-8') as file:
    json.dump(product_list, file, ensure_ascii=False, indent=4)        
            
# print(product_list)