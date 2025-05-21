import requests

def get_products():
    api_url = "https://api.escuelajs.co/api/v1/products"
    response = requests.get(api_url)
    return response.json()

def get_categories():
    cat_url = "https://api.escuelajs.co/api/v1/categories"
    response = requests.get(cat_url)
    return response.json()

def post_product(product):
    api_url = "https://api.escuelajs.co/api/v1/products"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(api_url, json=product)
    return response.json()