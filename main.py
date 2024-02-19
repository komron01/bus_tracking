from flask import Flask, render_template, jsonify
import psycopg2

app = Flask(__name__)

# Example class to manage bus location data
class BusManager:
    def __init__(self):
        # Initialize an empty list for bus locations
        self.bus_locations = []
        self.current_index = 0
        # Call the method to fetch bus locations from the database
        self.fetch_bus_locations_from_db()

    def get_current_location(self):
        if not self.bus_locations:
            # Handle the case when the bus_locations list is empty
            return {
                'latitude': 0.0,
                'longitude': 0.0,
                'routeNumber': 'default'
            }

        current_location = self.bus_locations[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.bus_locations)
        return {
            'latitude': current_location.get('latitude', 0.0),
            'longitude': current_location.get('longitude', 0.0),
            'routeNumber': current_location.get('routeNumber', 'default')
        }

    def fetch_bus_locations_from_db(self):
        # Modify these parameters with your PostgreSQL connection details
        connection_params = {
            'host': '127.0.0.1',
            'database': 'bus',
            'user': 'postgres',
            'password': '123'
        }

        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(**connection_params)

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Fetch bus locations from the 'bus_data' table
            cursor.execute("SELECT data->>'lat' AS latitude, data->>'lon' AS longitude, data->>'routeNumber' AS routeNumber FROM bus_data;")
            rows = cursor.fetchall()

            # Transform the data into a list of dictionaries
            self.bus_locations = [
                {'latitude': row[0], 'longitude': row[1], 'routeNumber': row[2]} for row in rows
            ]
           

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()


# Create an instance of the BusManager
bus_manager = BusManager()

# Example route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Example route to provide bus location data
@app.route('/get_bus_location')
def get_bus_location():
    cur_location = bus_manager.get_current_location()
    return jsonify(cur_location)

if __name__ == '__main__':
    app.run(debug=True)
