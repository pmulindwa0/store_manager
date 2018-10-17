from flask import request, jsonify, abort

class Products:

    def __init__(self):
        self.all_products = [
            {
                'id': 1,
                'name': "Iphone6",
                'quantity': 24,
                'ammount': 1200000,
                'image': "iphone.jpeg"
            },
            {
                'id': 2,
                'name': "Bits by peter",
                'quantity': 176,
                'ammount': 80000,
                'image': "bits.jpeg"
            }
        ]

    def get_all_products(self):
        return self.all_products

