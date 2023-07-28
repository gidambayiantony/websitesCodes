# app.py (Flask App)
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    # Authenticate user and set session
    session['user_id'] = data['user_id']
    return jsonify({'message': 'Login successful'})

@app.route('/logout', methods=['GET'])
def logout():
    # Clear session
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'})

if __name__ == '__main__':
    app.run(debug=True)

