from flask import Flask, render_template, jsonify
from time import time
app = Flask(__name__)

global bus_location
bus_location = [
        {'latitude':  51.2088128, 'longitude': 51.3769565},
        { "latitude": 51.209815, "longitude": 51.377960 },
        { "latitude": 51.210810, "longitude": 51.378950 },
        { "latitude": 51.211820, "longitude": 51.379955 },
        { "latitude": 51.212805, "longitude": 51.377965 }
        ]
# Example route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Example route to provide bus location data (replace this with your actual data source)
@app.route('/get_bus_location')
def get_bus_location():
    # Example: return static bus location data
    i = int(time()) % 4
    print(i, flush=True)
    cur_location = bus_location[i]
    
    

    return jsonify(cur_location)

if __name__ == '__main__':
    app.run(debug=True)
