# Hardware - Ulash sxemasi

## Komponentlar ro'yxati

| # | Komponent | Model | Soni | Vazifasi |
|---|-----------|-------|------|----------|
| 1 | Mikrokontroller | ESP32 DevKit 38-pin | 1 | Asosiy boshqaruv |
| 2 | Ultratovush sensor | RCWL-9610A (3.3V) | 1 | Masofa o'lchash |
| 3 | Yorug'lik sensor | TEMT6000 | 1 | Kunduz/tun aniqlash |
| 4 | Relay modul | 3.3V 1-kanal | 1 | LED yoqish/o'chirish |
| 5 | LED chiroq | 12V yoki 5V | 1 | Ko'cha yoritgichi |
| 6 | Quyosh paneli | Mini 6V | 1 | Energiya manbai (maket) |

## Pin konfiguratsiya

```
ESP32 DevKit 38-pin
┌─────────────────────────────┐
│                             │
│  GPIO 4  ──► RCWL TRIG     │
│  GPIO 16 ◄── RCWL ECHO     │
│  GPIO 34 ◄── TEMT6000 OUT  │
│  GPIO 26 ──► RELAY IN      │
│  GPIO 2  ──► Onboard LED   │
│                             │
│  3.3V    ──► Sensorlar VCC │
│  GND     ──► Umumiy GND    │
│                             │
└─────────────────────────────┘
```

## Ulash sxemasi

```
                    ┌──────────────┐
                    │   ESP32      │
                    │   DevKit     │
                    │              │
    RCWL-9610A      │   GPIO 4 ───┼──► TRIG
    ┌────────┐      │   GPIO 16 ──┼──◄ ECHO
    │  VCC ──┼──◄───┼── 3.3V      │
    │  GND ──┼──◄───┼── GND       │
    │  TRIG ─┼──►───┼── GPIO 4    │
    │  ECHO ─┼──►───┼── GPIO 16   │
    └────────┘      │              │
                    │              │
    TEMT6000        │   GPIO 34 ──┼──◄ OUT
    ┌────────┐      │              │
    │  VCC ──┼──◄───┼── 3.3V      │
    │  GND ──┼──◄───┼── GND       │
    │  OUT ──┼──►───┼── GPIO 34   │
    └────────┘      │              │
                    │              │
    RELAY MODULE    │   GPIO 26 ──┼──► IN
    ┌────────┐      │              │
    │  VCC ──┼──◄───┼── 3.3V      │
    │  GND ──┼──◄───┼── GND       │
    │  IN  ──┼──◄───┼── GPIO 26   │
    │  COM ──┼──►── LED (+)       │
    │  NO  ──┼──►── Power (+)     │
    └────────┘      │              │
                    └──────────────┘
```

## Muhim eslatmalar

1. **RCWL-9610A** 3.3V da ishlaydi — to'g'ridan-to'g'ri ESP32 ga ulash mumkin
2. **Relay** 3.3V logic bilan ishlashi kerak (5V relay ishlamaydi)
3. **GPIO 34** faqat input — analog o'qish uchun ideal
4. **Kod yuklash paytida** barcha simlarni ajrating (flash xatosi bo'lmasligi uchun)
5. **GPIO 5, 12, 15** ishlatmang — bu strapping pinlar
