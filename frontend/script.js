// 🗣️ Nastavení hlasu
const utter = new SpeechSynthesisUtterance();
utter.lang = "cs-CZ";

// 🌦️ Načtení počasí
function setBackground(code) {
    const hour = new Date().getHours();
    const isNight = hour >= 20 || hour < 6;

    const iconName = getIconName(weatherCode); // např. "clear"
    const finalIcon = isNight ? `${iconName}_night.png` : `${iconName}.png`;

    const img = document.getElementById("weatherImage");
    img.style.opacity = 0;
    setTimeout(() => {
  img.src = `icons/${finalIcon}`;
  img.style.opacity = 1;
}, 500);
        0: "#ffecb3",
        1: "#d0e6ff",
        2: "#cf8dcf",
        3: "#90a4ae",
        45: "#b0bec5",
        48: "#78909c",
        51: "#aed581",
        61: "#81d4fa",
        71: "#b3e5fc",
        95: "#ff8a80"
    };

    const nightColors = {
        0: "#2c3e50",
        1: "#34495e",
        2: "#3b3b5c",
        3: "#2f2f2f",
        45: "#37474f",
        48: "#263238",
        51: "#4e5d4e",
        61: "#1e88e5",
        71: "#90caf9",
        95: "#c62828"
    };

    const bgColor = isNight ? nightColors[code] || "#222" : dayColors[code] || "#fff";
    document.body.style.backgroundColor = bgColor;
// 🌞🌙 Přepnutí ikony režimu
    const modeIcon = document.getElementById("modeIcon");
    modeIcon.textContent = isNight ? "🌙" : "🌞";
}
function showWeather() {
    const url = "https://api.open-meteo.com/v1/forecast?latitude=50.1&longitude=15.7&current_weather=true";

    fetch(url)
        .then(res => res.json())
        .then(data => {
            const w = data.current_weather;
            const icon = mapWeatherImage(w.weathercode); // obrázek
            const desc = mapWeatherIcon(w.weathercode);  // textový popis
            const temp = w.temperature;
            const wind = w.windspeed;
            const time = new Date().toLocaleTimeString("cs-CZ");

            const output = `${desc}\n🌡️ Teplota: ${temp}°C\n💨 Vítr: ${wind} km/h\n🕒 Čas: ${time}`;
            updateOutput(output);
            setBackground(w.weathercode);
            checkAlerts(temp, wind);
            document.getElementById("weather-image").src = `icons/${icon}`; // ✅ ZOBRAZENÍ OBRÁZKU
        })
        .catch(() => {
            updateOutput("⚠️ Počasí se nepodařilo načíst.");
        });
}

// 🖼️ Výběr obrázku podle kódu
function mapWeatherImage(code) {
    const images = {
        0: "clear.png",
        1: "partly_cloudy.png",
        2: "cloudy.png",
        3: "overcast.png",
        45: "fog.png",
        48: "dense_fog.png",
        51: "drizzle.png",
        61: "rain.png",
        71: "snow.png",
        95: "thunderstorm.png"
    };
    return images[code] || "unknown.png";
}

// 🧠 Výběr textového popisu
function mapWeatherIcon(code) {
    const icons = {
        0: "☀️ Jasno",
        1: "🌤 Lehce oblačno",
        2: "⛅ Částečně oblačno",
        3: "☁️ Zataženo",
        45: "🌫️ Mlha",
        48: "🌫️ Hustá mlha",
        51: "🌦️ Mrholení",
        61: "🌧️ Déšť",
        71: "❄️ Sníh",
        95: "⛈️ Bouřka"
    };
    return icons[code] || "❓ Neznámé počasí";
}

// 📢 Výstup + hlas
function updateOutput(text) {
    document.getElementById("output").innerText = text;
    utter.text = text;
    speechSynthesis.speak(utter);
}

// 🎨 Pozadí podle počasí
function setBackground(code) {
    const backgrounds = {
        0: "#ffecb3",
        1: "#d0e6ff",
        2: "#cf8dcf",
        3: "#90a4ae",
        45: "#b0bec5",
        48: "#78909c",
        51: "#aed581",
        61: "#81d4fa",
        71: "#b3e5fc",
        95: "#ff8a80"
    };
    document.body.style.backgroundColor = backgrounds[code] || "#ffffff";
}

// 🚨 Výstrahy
function checkAlerts(temp, wind) {
    if (temp > 30) alert("🔥 Vedro!");
    if (wind > 50) alert("💨 Silný vítr!");
}

// ⏲️ Spuštění
showWeather();
setInterval(showWeather, 300000); // každých 5 minut
