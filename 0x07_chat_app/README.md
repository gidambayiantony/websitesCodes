## Real-Time Chat App

This repository contains the code for a real-time chat app supporting private and group messaging with online status indicators.

### Contents
- `server.py`: This is the server-side code for the real-time chat app implemented using Flask and Socket.IO. The server handles connections, disconnections, private messages, and group messages. Users' online status is also tracked and displayed to other users.

- `client.html`: This is the client-side code for the real-time chat app implemented using HTML and JavaScript with Socket.IO. The client provides an interface to send private messages and group messages. It also displays the online status of users.

### How to Use
1. Clone this repository to your local machine.

2. Run the Flask server using the following command:
```bash
python server.py

