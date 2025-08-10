#!/data/data/com.termux/files/usr/bin/bash

# Ambientní styly pomocí sox
sox -n ambient1.mp3 synth 30 sin 220 vol 0.2
sox -n alert_cpu.mp3 synth 5 sine 880 vol 0.9
sox -n connected.mp3 synth 1 sine 440 fade h 0.1 0.9 0.1
sox -n disconnected.mp3 synth 2 pinknoise vol 0.3
