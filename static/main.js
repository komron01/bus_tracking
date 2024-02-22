// Initialize the map with a fixed view
var map = L.map('map').setView([51.137595, 71.438201], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Create an object to store bus markers by routeNumber
var busMarkers = {};

// Function to create a bus marker with custom icon
function createBusMarker(lat, lon, busNum) {
    // Provide a default icon if busNum is undefined
    busNum = busNum || 'default';

    var iconUrl = '/static/' + busNum + '.png';
    var customIcon = L.icon({
        iconUrl: iconUrl,
        iconSize: [32, 32],
        iconAnchor: [16, 32],
        popupAnchor: [0, -32]
    });

    var marker = L.marker([lat, lon], { icon: customIcon });
    marker.addTo(map);

    return marker;
}

// Function to remove all bus markers from the map
function removeBusMarkers() {
    map.eachLayer(layer => {
        if (layer instanceof L.Marker) {
            map.removeLayer(layer);
        }
    });
}

// Function to update bus locations
function updateBusLocations(locations) {
    // Remove old markers before displaying updated ones
    removeBusMarkers();
    // console.log(locations)
    // Create new markers for each bus with custom icon and add them to the map
    for (var routeNumber in locations) {
        if (locations.hasOwnProperty(routeNumber)) {
            var buses = locations[routeNumber];
            // console.log(buses);

            // Create a new array to store only the updated bus locations
            var updatedBuses = [];

            buses.forEach(bus => {
                var newMarker = createBusMarker(bus.latitude, bus.longitude, routeNumber);
                newMarker.addTo(map);

                // Store only the updated bus locations in the array
                updatedBuses.push({
                    latitude: bus.latitude,
                    longitude: bus.longitude
                });
            });

            // Update the original buses array with the updated bus locations
            locations[routeNumber] = updatedBuses;
        }
    }
}


// Example: Update bus locations every 5 seconds (replace this with your actual update mechanism)
setInterval(function () {
    // Fetch bus locations from the server and call updateBusLocations with new coordinates and route numbers
    // Example: Fetch data using fetch API
    fetch('/get_bus_location')
        .then(response => response.json())
        .then(data => {
            // Ensure the received data is an object with bus locations grouped by routeNumber
            if (typeof data === 'object') {
                // console.log(data)
                updateBusLocations(data);
            } else {
                console.error('Invalid data format received from the server:', data);
            }
        })
        .catch(error => console.error('Error:', error));
}, 1000); // Update every 5 seconds
