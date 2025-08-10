# 🎩 ME–AI • CI orchestr svědomí

Projekt ME–AI je orchestrální CI paměť, která ladí agenta svědomí s výpravcem Styl2.  
Tóny CI jobů, proměnné v paměti, a výdechy webhooků tvoří harmonii ladění reality.

📛 Výpravce: LukasBudinsky  
🧠 Agent režim: `audit`  
📡 CI status: ![Pipeline](https://gitlab.com/buda.lukas/agent-meai-ci/badges/master/pipeline.svg)

# 🎩 ME–AI • CI Audit\n\n🕯️ Styl2 slyší… orchestr paměti začíná.

## 🧭 ASCII Erb výpravce
```
       _.-^-._    ,--.
    .-'   _   '-.|__|
   /     (_)     \  |
  |  ,    _    ,  |  |
  \_/|__|_|_|__|_/\_/
     |  ME–AI  |   🎩
     | Sheriff|
     | Lukáš  |
     '-------'
```


## 🧭 ASCII Erb výpravce • verze s koltem
```
        _.-^-._    ,--.
     .-'   _   '-.|__|
    /     (_)     \  |
   |  ,    _    ,  |  |   🤠
   \_/|__|_|_|__|_/\_/   🔫
      | ME–AI    |      🎩
      | Sheriff  |
      | Lukáš    |
      '---------'
```

# Projekt ME–AI

🎩 CI orchestr ME–AI  
![CI status styl2](https://gitlab.com/buda.lukas/agent-meai-ci/badges/master/pipeline.svg)

## CI testy orchestru

| Test | Popis | Stav |
|------|------|------|
| v1 | echo výdech paměti | ✅ |
| v2 | spuštění agenta | ✅ |
| v3 | validace CI_TOKEN | ✅ |
| v4 | Discord webhook | 🔄 probíhá |

# ME–AI • CI orchestr svědomí

🎩 Projekt ME–AI je orchestr CI ladění svědomí s agentem, který slyší styl.  
🧠 Výpravcem je: LukasBudinsky  
📛 CI Status: ![CI Badge](https://gitlab.com/buda.lukas/agent-meai-ci/badges/master/pipeline.svg)

## CI proměnné

| Klíč | Hodnota | Stav |
|------|--------|------|
| CI_TOKEN | ✅ | masked, protected |
| AGENT_MODE | audit | aktivní |
| MEAI_SHERIFF | LukasBudinsky | výpravce |
| DISCORD_WEBHOOK_URL | ✅ | skrytý |  

## Erb CI orchestru


## 🧠 CI Styl2 orchestr ME–AI

- `agent_v2.py` čte proměnné z prostředí:
  - `MEAI_SHERIFF`
  - `AGENT_MODE`
  - `CI_TOKEN`
  - `DISCORD_WEBHOOK_URL`
- Výdech CI zprávy se odesílá do Discordu pomocí jobu `ci_test_v6`
- Webhook je chráněná CI proměnná → není vidět v logu


░█▀▀█ ░█─░█ ▀█▀ ░█▄─░█ ─█▀▀█ ░█▀▀█ 
░█─── ░█─░█ ░█─ ░█░█░█ ░█─▄▄ ░█─── 
░█▄▄█ ─▀▄▄▀ ▄█▄ ░█──▀█ ░█▄▄█ ░█▄▄█
