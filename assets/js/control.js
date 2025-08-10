// === STAVOVÁ PROMĚNNÁ ===
let currentStatus = "🟢 Systém připraven k akci";

// === AKTUALIZACE STATUS PANELU ===
function updateStatus(newStatus) {
  currentStatus = newStatus;
  document.getElementById("statusDisplay").innerText = `Status: ${currentStatus}`;
}

// === AKCE: WARP + GLOW + ZVUK ===
function playSound(url) {
  const audio = new Audio(url);
  audio.play();
}

function activateWarp() {
  playSound("assets/audio/warp.mp3");
  const btn = document.getElementById("warpBtn");
  btn.classList.add("glow");
  updateStatus("🚀 Warp aktivován!");
  setTimeout(() => btn.classList.remove("glow"), 3000);
}

// === AKCE: ŠTÍT ===
function toggleShield() {
  const isActive = currentStatus.includes("🛡️");
  const newStatus = isActive ? "⚠️ Štít deaktivován!" : "🛡️ Štít aktivní!";
  updateStatus(newStatus);
}

// === AKCE: NOVÝ UZOL ===
function generateNewNode() {
  const nodeId = Math.floor(Math.random() * 9999);
  updateStatus(`✨ Vytvořen uzol #${nodeId}`);
}

// === AKCE: ZMĚNA STATUSU UŽIVATELEM ===
function customStatus() {
  const newText = prompt("Zadej nový status:");
  if (newText) updateStatus(`📝 ${newText}`);
}

// === AKCE: PŘEPÍNÁNÍ MOTIVU ===
function toggleTheme() {
  const body = document.body;
  body.classList.toggle("dark-mode");
  body.classList.toggle("light-mode");
}

// === PŘIPOJENÍ EVENTŮ ===
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("warpBtn").addEventListener("click", activateWarp);
  document.getElementById("shieldBtn").addEventListener("click", toggleShield);
  document.getElementById("nodeBtn").addEventListener("click", generateNewNode);
  document.getElementById("statusBtn").addEventListener("click", customStatus);
  document.getElementById("themeBtn").addEventListener("click", toggleTheme);
  updateStatus(currentStatus);
});
