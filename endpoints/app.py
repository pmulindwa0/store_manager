from flask import Flask, jsonify, request, abort, make_response
from products import Products
from sales import Sales

app = Flask(__name__)

product = Products()
sales = Sales()
# Error Handling

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Server Not Found'}), 404)

# Routes

@app.route('/store_manager/api/v1/user/products', methods=['GET'])
def get_products():
    return jsonify({'products': product.get_all_products()}), 200

@app.route('/store_manager/api/v1/admin/products', methods=['POST'])
def create_product():
    return jsonify({'product': product.create_pdt()}), 201

@app.route('/store_manager/api/v1/user/products/<int:pdt_id>', methods=['GET'])
def get_product(pdt_id):
    return jsonify({'product': product.get_pdt(pdt_id)}), 200

@app.route('/store_manager/api/v1/admin/sales', methods=['GET'])
def get_sales():
    return jsonify({'sales': sales.all_sales()}), 200

@app.route('/store_manager/api/v1/user/sales', methods=['POST'])
def create_sale():
    return jsonify({'sale': sales.add_sale()}), 201

@app.route('/store_manager/api/v1/user/sales/<int:sales_id>', methods=['GET'])
def get_sale(sales_id):
    return jsonify({'product': sales.get_sale(sales_id)})

if __name__ == '__main__':
    app.run(debug=True, port=8080)