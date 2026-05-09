import requests
import json
import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

user_agent = {'User-agent': 'Mozilla/5.0'}

def compare_prices(product_laughs, product_glomark):
    # --- Laughs Supermarket ---
    response_laughs = requests.get(product_laughs, headers=user_agent)
    soup_laughs = BeautifulSoup(response_laughs.text, 'html.parser')

    # Product name from h1 or title
    product_name_laughs = soup_laughs.find('h1').get_text(strip=True)

    # Try multiple span class names that might hold the price
    price_laughs = None
    for class_name in ['price', 'woocommerce-Price-amount', 'amount', 'product-price']:
        tag = soup_laughs.find('span', class_=class_name)
        if tag:
            raw = tag.get_text(strip=True).replace('Rs.', '').replace('₨', '').replace(',', '').strip()
            try:
                price_laughs = float(raw)
                if price_laughs > 0:
                    break
            except ValueError:
                continue

    # --- Glomark Supermarket ---
    response_glomark = requests.get(product_glomark, headers=user_agent)
    soup_glomark = BeautifulSoup(response_glomark.text, 'html.parser')

    product_name_glomark = None
    price_glomark = None

    # Search ALL script tags (not just application/ld+json) for JSON with price
    for script in soup_glomark.find_all('script'):
        text = script.string
        if not text:
            continue
        # Look for inline JSON objects containing price
        if '"price"' in text or "'price'" in text:
            try:
                # Try direct JSON parse
                data = json.loads(text)
                if 'offers' in data:
                    price_glomark = float(data['offers']['price'])
                    product_name_glomark = data.get('name', 'Unknown')
                    break
                elif 'price' in data:
                    price_glomark = float(data['price'])
                    product_name_glomark = data.get('name', 'Unknown')
                    break
            except (json.JSONDecodeError, TypeError, KeyError):
                # Try to extract JSON substring from script
                try:
                    start = text.index('{')
                    end = text.rindex('}') + 1
                    data = json.loads(text[start:end])
                    if 'offers' in data:
                        price_glomark = float(data['offers']['price'])
                        product_name_glomark = data.get('name', 'Unknown')
                        break
                    elif 'price' in data:
                        price_glomark = float(data['price'])
                        product_name_glomark = data.get('name', 'Unknown')
                        break
                except (ValueError, json.JSONDecodeError, KeyError):
                    continue

    print('Laughs  ', product_name_laughs, 'Rs.: ', price_laughs)
    print('Glomark ', product_name_glomark, 'Rs.: ', price_glomark)

    if price_laughs > price_glomark:
        print('Glomark is cheaper:', round(price_laughs - price_glomark, 2))
    elif price_laughs < price_glomark:
        print('Laughs is cheaper:', round(price_glomark - price_laughs, 2))
    else:
        print('Price is the same')