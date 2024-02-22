from flask import Flask, render_template, jsonify
import psycopg2

app = Flask(__name__)

# Example class to manage bus location data
class BusManager:
    def __init__(self):
        # Initialize an empty dictionary for bus locations grouped by routeNumber
        self.bus_locations = {}
        # Establish a single database connection when the BusManager is created
        self.connection = self.create_connection()
        # Call the method to fetch bus locations from the database
        self.fetch_bus_locations_from_db()

    def create_connection(self):
        # Modify these parameters with your PostgreSQL connection details
        connection_params = {
            'host': '127.0.0.1',
            'database': 'bus',
            'user': 'postgres',
            'password': '123'
        }
        # Connect to the PostgreSQL database
        return psycopg2.connect(**connection_params)

    def fetch_bus_locations_from_db(self):
        self.bus_locations = {}

        try:
            # Create a cursor object to execute SQL queries
            cursor = self.connection.cursor()
            query = '''SELECT DISTINCT ON (data->>'routeNumber')
                            data->>'lat' AS latitude,
                            data->>'lon' AS longitude,
                            data->>'routeNumber' AS routeNumber
                        FROM bus_data
                        ORDER BY (data->>'routeNumber'), (data->>'terminalDate')::timestamp DESC;
                    '''
            # Fetch bus locations from the 'bus_data' table
           # cursor.execute("SELECT data->>'lat' AS latitude, data->>'lon' AS longitude, data->>'routeNumber' AS routeNumber FROM bus_data;")
            cursor.execute(query)
            rows = cursor.fetchall()
            # print(rows,flush=True)

            # Transform the data into a dictionary grouped by routeNumber
            for row in rows:
                route_number = row[2]
                if route_number not in self.bus_locations:
                    self.bus_locations[route_number] = []
                self.bus_locations[route_number].append({'latitude': row[0], 'longitude': row[1]})

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Close the cursor after each query (optional, you can keep it open if needed)
            cursor.close()

# Create an instance of the BusManager
bus_manager = BusManager()

# Example route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Example route to provide bus location data for all buses grouped by routeNumber
@app.route('/get_bus_location')
def get_bus_location():
    # Retrieve the most updated bus locations grouped by routeNumber
    bus_manager.fetch_bus_locations_from_db()
    all_locations = bus_manager.bus_locations
    # print(jsonify(all_locations), flush=True)
    return jsonify(all_locations)

if __name__ == '__main__':
    app.run(debug=True)
