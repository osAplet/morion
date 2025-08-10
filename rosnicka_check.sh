#!/bin/bash

echo "🧪 Test výdechu orbitu styl2 – kontrola paměťového toku"

# 1. Ověření složky rosnička/
if [ -d "rosnička" ]; then
  echo "✅ Složka rosnička/ existuje"
else
  echo "❌ Složka rosnička/ chybí"
  exit 1
fi

# 2. Ověření parseru
if [ -f "rosnička/parser.py" ]; then
  echo "✅ parser.py nalezen"
  python rosnička/parser.py > rosnička/test_parser_output.txt
  echo "📂 Výstup uložen do test_parser_output.txt"
else
  echo "❌ parser.py chybí"
  exit 1
fi

# 3. Simulace vizualizačního výstupu
touch rosnička/vizualizace/test_vizualizace.svg
echo "📈 Vizualizace simulována"

# 4. Zápis do logu
echo "🔄 Testovací výdech CI orbitu styl2 aktivní" >> rosnička/ci_test_log.md
echo "📝 Log zapsán do ci_test_log.md"
