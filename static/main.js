var map = L.map('map').setView([51.2088128, 51.3769565], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

var busMarkers = [];

// Function to create a bus marker with custom icon
function createBusMarker(lat, lon, busNum) {
    var iconUrl = '/static/'+ busNum + '.png'; // Assuming your icon files are named with bus numbers
    var customIcon = L.icon({
        iconUrl: iconUrl,
        iconSize: [32, 32], // Adjust the icon size as needed
        iconAnchor: [16, 32], // Adjust the anchor point if necessary
        popupAnchor: [0, -32] // Adjust the popup anchor if needed
    });

    var marker = L.marker([lat, lon], { icon: customIcon }).addTo(map);
    return marker;
}

// Function to update bus location
function updateBusLocation(lat, lon, busNum) {
    // Remove existing markers
    busMarkers.forEach(marker => map.removeLayer(marker));

    // Create a new marker with custom icon and add it to the map
    var newMarker = createBusMarker(lat, lon, busNum);
    busMarkers.push(newMarker);

    map.panTo([lat, lon]);
}

// Example: Update bus location every 5 seconds (replace this with your actual update mechanism)
setInterval(function() {
    // Fetch bus location from the server and call updateBusLocation with new coordinates and bus number
    // Example: Fetch data using fetch API
    fetch('/get_bus_location')
        .then(response => response.json())
        .then(data => {
            updateBusLocation(data.latitude, data.longitude, data.bus_num);
        })
        .catch(error => console.error('Error:', error));
}, 1000); // Update every 5 seconds
