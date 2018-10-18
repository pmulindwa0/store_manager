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