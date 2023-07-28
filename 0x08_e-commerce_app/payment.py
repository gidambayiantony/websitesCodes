# payment.py (Flask App with Stripe Integration)
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)
stripe.api_key = 'your_stripe_secret_key'

@app.route('/payment', methods=['POST'])
def payment():
    data = request.json
    amount = data['amount']
    # Create a Stripe payment intent
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency='usd',
    )
    return jsonify(client_secret=intent.client_secret)

if __name__ == '__main__':
    app.run(debug=True)

