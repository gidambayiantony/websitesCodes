from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Dictionary to store user data with their online status
users = {}

@socketio.on('connect')
def on_connect():
    user_id = request.args.get('user_id')
    users[user_id] = True
    emit('online_status', {'user_id': user_id, 'status': True}, broadcast=True)

@socketio.on('disconnect')
def on_disconnect():
    user_id = request.args.get('user_id')
    users[user_id] = False
    emit('online_status', {'user_id': user_id, 'status': False}, broadcast=True)

@socketio.on('private_message')
def on_private_message(data):
    sender = data['sender']
    recipient = data['recipient']
    message = data['message']
    emit('private_message', {'sender': sender, 'message': message}, room=recipient)

@socketio.on('group_message')
def on_group_message(data):
    sender = data['sender']
    group_id = data['group_id']
    message = data['message']
    emit('group_message', {'sender': sender, 'message': message}, room=group_id)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

