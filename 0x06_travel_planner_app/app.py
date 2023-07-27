from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace this with your OpenWeatherMap API key
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest_destinations():
    # Your logic to suggest destinations based on user preferences
    # You can use any data source or APIs for this

    destinations = ['New York', 'Paris', 'Tokyo', 'Sydney']
    return render_template('suggested_destinations.html', destinations=destinations)

@app.route('/create_itinerary', methods=['POST'])
def create_itinerary():
    # Your logic to create the itinerary based on user-selected destination
    # You can use any data source or APIs for this

    selected_destination = request.form['destination']
    itinerary = ['Day 1: Visit attractions in ' + selected_destination,
                 'Day 2: Explore ' + selected_destination + ' museums',
                 'Day 3: Enjoy local cuisines in ' + selected_destination]
    
    return render_template('itinerary.html', destination=selected_destination, itinerary=itinerary)

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()

    weather = {
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
    }

    return render_template('weather.html', city=city, weather=weather)

if __name__ == '__main__':
    app.run(debug=True)

