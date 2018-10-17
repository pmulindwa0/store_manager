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

    def create_pdt(self):
        new_pdt = {
            'id': self.all_products[-1]['id'] + 1,
            'name': request.json['name'],
            'quantity': request.json['quantity'],
            'ammount': request.json['ammount'],
            'image': request.json['image']
        }
        self.all_products.append(new_pdt)
        return new_pdt

    def get_pdt(self, pdt_id):
        pdt =  [pdt for pdt in self.all_products if pdt['id'] == pdt_id]

        if len(pdt) ==0:
            abort(404)

        return pdt

