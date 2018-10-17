from flask import Flask, jsonify, request, abort, make_response
from products import Products

app = Flask(__name__)

product = Products()

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

if __name__ == '__main__':
    app.run(debug=True, port=8080)