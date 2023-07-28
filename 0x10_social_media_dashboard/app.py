from flask import Flask, render_template, request

app = Flask(__name__)

# Your backend code for managing social media accounts, scheduling posts, and analyzing engagement metrics goes here.

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

