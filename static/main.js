var map = L.map('map').setView([51.137595, 71.438201], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

var busMarkers = [];

// Function to create a bus marker with custom icon
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

    var marker = L.marker([lat, lon], { icon: customIcon }).addTo(map);
    return marker;
}

// Function to update bus location
function updateBusLocation(lat, lon, routeNumber) {
    // Remove existing markers
    busMarkers.forEach(marker => map.removeLayer(marker));

    // Provide a default value for routeNumber if it's not present in the received data
    routeNumber = routeNumber || 'default';

    // Create a new marker with custom icon and add it to the map
    var newMarker = createBusMarker(lat, lon, routeNumber);
    busMarkers.push(newMarker);

    map.panTo([lat, lon]);
}

// Example: Update bus location every 5 seconds (replace this with your actual update mechanism)
setInterval(function () {
    // Fetch bus location from the server and call updateBusLocation with new coordinates and route number
    // Example: Fetch data using fetch API
    fetch('/get_bus_location')
        .then(response => response.json())
        .then(data => {
            // Ensure the received data has at least latitude and longitude
            if (data.latitude !== undefined && data.longitude !== undefined) {
                updateBusLocation(data.latitude, data.longitude, data.routeNumber);
            } else {
                console.error('Invalid data format received from the server:', data);
            }
        })
        .catch(error => console.error('Error:', error));
}, 1000); // Update every 5 seconds
