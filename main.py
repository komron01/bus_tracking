from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Example class to manage bus location data
class BusManager:
    def __init__(self):
        self.bus_locations = [
            {'latitude': 51.2088128, 'longitude': 51.3769565, 'bus_num': 43},
            {'latitude': 51.209815, 'longitude': 51.377960, 'bus_num': 43},
            {'latitude': 51.210810, 'longitude': 51.378950, 'bus_num': 43},
            {'latitude': 51.211820, 'longitude': 51.379955, 'bus_num': 43},
            {'latitude': 51.212805, 'longitude': 51.377965, 'bus_num': 43}
        ]
        self.current_index = 0

    def get_current_location(self):
        current_location = self.bus_locations[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.bus_locations)
        return current_location

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
