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


document.getElementById("teamSelect").addEventListener("change", function () {
    const team = this.value;

    if (!team) return;

    fetch(`${API_URL}/matches?team=${team}`)
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("matchesList");
            list.innerHTML = "";

            data.forEach(match => {
                const li = document.createElement("li");
                li.textContent = `${match.date} - ${match.opponent} (${match.ground})`;
                list.appendChild(li);
            });
        });
});