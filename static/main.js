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

// Function to update bus location
function updateBusLocation(lat, lon, routeNumber) {
    // Check if markers exist for the given routeNumber
    if (!busMarkers[routeNumber]) {
        busMarkers[routeNumber] = [];
    } else {
        // Remove existing markers for the given routeNumber
        busMarkers[routeNumber].forEach(marker => map.removeLayer(marker));
    }

    // Create a new marker with custom icon and add it to the map
    var newMarker = createBusMarker(lat, lon, routeNumber);
    busMarkers[routeNumber].push(newMarker);
}

// Example: Update bus location every 5 seconds (replace this with your actual update mechanism)
setInterval(function () {
    // Fetch bus location from the server and call updateBusLocation with new coordinates and route number
    // Example: Fetch data using fetch API
    fetch('/get_bus_location')
        .then(response => response.json())
        .then(data => {
            // Ensure the received data has at least latitude, longitude, and routeNumber
            if (data.latitude !== undefined && data.longitude !== undefined && data.routeNumber !== undefined) {
                updateBusLocation(data.latitude, data.longitude, data.routeNumber);
            } else {
                console.error('Invalid data format received from the server:', data);
            }
        })
        .catch(error => console.error('Error:', error));
}, 1000); // Update every 1 seconds
