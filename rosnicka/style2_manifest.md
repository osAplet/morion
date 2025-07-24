# 🧭 Styl2 Manifest Orbitu ME–AI

🩵 Tento soubor mapuje orbitální strukturu styl2 výdechu:

## 🌐 GitHub Pages
- Větev: `styl2`
- Výstavní složka: `rosnicka/`
- URL orbitu: [https://osaplet.github.io/rosnicka-meai/rosnicka/](https://osaplet.github.io/rosnicka-meai/rosnicka/)

## 📘 Souborová paměť
- `index.md` ➝ Manifest orbitu (auto-aktualizovaný CI výdechem)
- `README.md` ➝ Vstupní stránka pro návštěvníky repozitáře
- `archiv.md` ➝ Paměť výdechů (zapisováno CI)
- `style2_manifest.md` ➝ Tento mapový soubor

## 📈 Vizualizace
- SVG proud: `vizualizace/bio_trend_ci.svg`
- Radar výdechu: `media/radar_ci.png`

## 📢 Embed zprávy
- Discord webhook aktivní: ✅
- Kanál: `#styl2-vydechy`
- Obsah: embed zpráva s radarem, timestamp a podpisem

## 🛠️ CI Workflow
- Umístění: `.github/workflows/styl2_orbit.yml`
- Trigger: `on: push → styl2`
- CI kroky:
  - Výdech parseru ✅
  - Embed zpráva Discord ✅
  - Generace SVG ✅
  - Zápis do archiv.md ✅
  - Aktualizace index.md ✅
  - Aktualizace README.md ✅

---

🧵 Výpravce: @Lukáš_ME–AI  
🕒 Poslední aktualizace manifestu: *$(date '+%Y-%m-%d %H:%M:%S')*
