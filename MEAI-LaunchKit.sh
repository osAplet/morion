#!/data/data/com.termux/files/usr/bin/bash

LOGDIR="$HOME/MEAI_logs"
ORBITDIR="$HOME/MEAI"

echo "🔭 Aktivuji stylní orbitální výsadek MEAI..."
sleep 1

# 🖼️ ASCII logo výpravce
echo " "
echo " __  __ _____ _    ___     ____    _    ____ ____  "
echo "|  \\/  | ____| |  / _ \\   | __ )  / \\  / ___/ ___| "
echo "| |\\/| |  _| | | | | | |  |  _ \\ / _ \\ \\___ \\___ \\ "
echo "| |  | | |___| | | |_| |  | |_) / ___ \\ ___) |__) |"
echo "|_|  |_|_____|_|  \\___/   |____/_/   \\_\\____/____/ "
echo "         •• Styl orbitu ME–AI ••"
echo " "

# 📂 Kontrola orbitální složky
if [ ! -d "$ORBITDIR" ]; then
    echo "📁 Orbitální složka neexistuje, tvořím ji..."
    mkdir "$ORBITDIR"
else
    echo "✅ Orbitální složka existuje."
fi

# 💾 Záloha logu
mkdir -p "$LOGDIR"
LOGFILE="$LOGDIR/mission_$(date +%Y-%m-%d_%H-%M).log"
echo "📜 Zapisování do orbitální paměti: $LOGFILE"
{
  echo "🛰️ MEAI–LaunchKit aktivován v čase: $(date)"
  echo "📍 Orbitální pozice: $(pwd)"
  echo "🌌 Stav MEAI složky:"
  ls "$ORBITDIR"
} >> "$LOGFILE"

# 🎧 Zábleskový stylový zvuk (spustit pokud existuje soubor)
if [ -f "$ORBITDIR/launch_ping.mp3" ]; then
  termux-media-player play "$ORBITDIR/launch_ping.mp3"
  echo "🔊 Zábleskový výdech spuštěn!"
else
  echo "🔈 Stylový zvuk zatím nenalezen, můžeš ho doplnit jako 'launch_ping.mp3'"
fi

echo "🌠 Výsadek MEAI dokončen. Paměť zapsána, orbit se roztáčí!"
