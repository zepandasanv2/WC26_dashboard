const stadiums = {
    "Mexico City": [19.4326, -99.1332],
    "New York": [40.7128, -74.0060],
    "Los Angeles": [34.0522, -118.2437],
    "Toronto": [43.65107, -79.347015]
};

const map = L.map('map').setView([20, -100], 3);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data © OpenStreetMap'
}).addTo(map);

const API_URL = "http://127.0.0.1:5000";

fetch(`${API_URL}/teams`)
    .then(res => res.json())
    .then(data => {
        const select = document.getElementById("teamSelect");

        data.forEach(team => {
            const option = document.createElement("option");
            option.value = team;
            option.textContent = team;
            select.appendChild(option);
        });
    });

let markers = [];

document.getElementById("teamSelect").addEventListener("change", function () {
    const team = this.value;

    if (!team) return;

    markers.forEach(m => map.removeLayer(m));
    markers = [];

    fetch(`${API_URL}/matches?team=${team}`)
        .then(res => res.json())
        .then(data => {

            data.forEach(match => {
                const coords = stadiums[match.ground];

                if (coords) {
                    const marker = L.marker(coords)
                        .addTo(map)
                        .bindPopup(`
                                    <div style="font-size:14px">
                                    <strong>${team} vs ${match.opponent}</strong><br>
                                    <hr>
                                    Date: ${match.date}<br>
                                    Time: ${match.time}<br>
                                    Stadium: ${match.ground}
                                    </div>
                                `);
                    markers.push(marker);
                }
                if (!coords) {
                    console.log("Missing coordinates for:", match.ground);
                }
            });
        });
});

let bounds = [];

data.forEach(match => {
    const coords = stadiums[match.ground];

    if (coords) {
        const marker = L.marker(coords)
            .addTo(map)
            .bindPopup(`
                <strong>${team} vs ${match.opponent}</strong><br>
                ${match.date}<br>
                ${match.ground}
            `);

        markers.push(marker);
        bounds.push(coords);
    }
});

if (bounds.length > 0) {
    map.fitBounds(bounds);
}