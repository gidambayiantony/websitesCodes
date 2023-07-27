# Travel Planner App

**Description**

The Travel Planner App is a web application that suggests destinations, allows itinerary creation, and provides weather information for the selected city. Users can input their preferences, and the app will display a list of suggested destinations. After selecting a destination, users can create an itinerary and view weather information for the selected city.

**Files**

- `app.py`: The main Python script using Flask to handle the app's routes and logic.
- `index.html`: HTML template for the main page where users can input their preferences.
- `suggested_destinations.html`: HTML template to display suggested destinations based on user preferences.
- `itinerary.html`: HTML template to display the itinerary for the selected destination.
- `weather.html`: HTML template to display the weather information for the selected city.
- `requirements.txt`: A file containing the required Python packages and their versions for the app to run.

**How to Run**

1. Clone the repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run the app using `python app.py`.
4. Access the app in your web browser at `http://localhost:5000`.

**Dependencies**

- Flask
- requests

**Note**

This app requires an active internet connection to fetch weather information for the selected city.


