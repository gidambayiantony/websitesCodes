# cart.py (Flask App)
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json
    product_id = data['product_id']
    # Retrieve cart from session or create if not exists
    cart = session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    session['cart'] = cart
    return jsonify({'message': 'Product added to cart'})

@app.route('/view_cart', methods=['GET'])
def view_cart():
    cart = session.get('cart', {})
    return jsonify(cart)

if __name__ == '__main__':
    app.run(debug=True)

