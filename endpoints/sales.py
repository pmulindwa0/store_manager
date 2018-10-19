from flask import request, jsonify, abort

class Sales:

    def __init__(self):
        self.sales_list = [
            {
            'id': 1,
            'product_name': "Iphone6",
            'quantity': 1,
            'ammount': 1200000,
            'sold_by': "Peter Mulindwa"
            }   
        ]

    def all_sales(self):
        return self.sales_list

    def add_sale(self):
        new_sale = {
            'id': self.sales_list[-1]['id'] + 1,
            'product_name': request.json['product_name'],
            'quantity': request.json['quantity'],
            'ammount': request.json['ammount'],
            'sold_by': request.json['sold_by']
        }
        self.sales_list.append(new_sale)
        return new_sale

    def get_sale(self, sale_id):
        sale = [sale for sale in self.sales_list if sale['id']==sale_id]

        if len(sale) == 0:
            abort(404)
        return sale