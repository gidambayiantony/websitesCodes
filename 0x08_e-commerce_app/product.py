# product.py (Product Model)
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['e_commerce']
collection = db['products']

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def save(self):
        product_data = {
            'name': self.name,
            'price': self.price,
            'description': self.description
        }
        collection.insert_one(product_data)

    @staticmethod
    def get_all():
        products = collection.find()
        return products

