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

## Ulash sxemasi

```
                         ┌───────────────────────┐
                         │      ESP32 DevKit      │
                         │                       │
    ┌──────────┐         │  3.3V ●───────────┐   │         ┌──────────┐
    │RCWL-9610A│         │                   │   │         │  RELAY   │
    │          │         │  GND  ●───────┐   │   │         │  MODULE  │
    │ VCC ─────┼─────────┼───────────────┼───┘   │         │          │
    │ GND ─────┼─────────┼───────────────┘       │         │ VCC ─────┼── 3.3V
    │ TRIG ────┼─────────┼── GPIO 4              │         │ GND ─────┼── GND
    │ ECHO ────┼─────────┼── GPIO 16             │         │ IN ──────┼── GPIO 26
    └──────────┘         │                       │         │          │
                         │                       │         │ COM ─────┼──┐
    ┌──────────┐         │                       │         │ NO ──────┼──┼──┐
    │ TEMT6000 │         │                       │         └──────────┘  │  │
    │          │         │                       │                       │  │
    │ VCC ─────┼─────────┼── 3.3V                │         ┌──────────┐  │  │
    │ GND ─────┼─────────┼── GND                 │         │ 💡 LED   │  │  │
    │ OUT ─────┼─────────┼── GPIO 34 (ADC)       │         │  CHIROQ  │  │  │
    └──────────┘         │                       │         │          │  │  │
                         │  GPIO 2 ● (Status LED)│         │ (+) ─────┼──┘  │
                         │                       │         │ (-) ─────┼─────┘
    ┌──────────┐         │                       │         └──────────┘
    │☀️ SOLAR  │         │  VIN/USB ● (Quvvat)   │
    │  PANEL   ├─────────┼── 5V                  │
    └──────────┘         └───────────────────────┘
```

## Signal yo'nalishlari

```
    ESP32                    Komponent           Yo'nalish
    ─────                    ─────────           ─────────
    GPIO 4  ──────────────►  RCWL TRIG           OUTPUT (10μs pulse)
    GPIO 16 ◄──────────────  RCWL ECHO           INPUT  (duration)
    GPIO 34 ◄──────────────  TEMT6000 OUT        ANALOG INPUT (0-4095)
    GPIO 26 ──────────────►  RELAY IN            OUTPUT (HIGH/LOW)
    GPIO 2  ──────────────►  Onboard LED         OUTPUT (status)
```

## Pin konfiguratsiya diagrammasi

```mermaid
graph TD
    subgraph PIN["ESP32 Pin Tayinlash"]
        direction LR
        P4["🟢 GPIO 4 — TRIG (OUTPUT)"]
        P16["🔵 GPIO 16 — ECHO (INPUT)"]
        P34["🟡 GPIO 34 — TEMT6000 (ANALOG)"]
        P26["🔴 GPIO 26 — RELAY (OUTPUT)"]
        P2["⚪ GPIO 2 — Status LED"]
    end

    subgraph SAFE["✅ Xavfsiz pinlar"]
        S1[GPIO 4, 13, 14, 16, 17]
        S2[GPIO 18, 19, 21, 22, 23]
        S3[GPIO 25, 26, 27, 32, 33]
        S4[GPIO 34, 35, 36, 39<br/>faqat INPUT]
    end

    subgraph DANGER["⛔ Ishlatmang"]
        D1[GPIO 0 — Boot]
        D2[GPIO 5 — SPI Flash]
        D3[GPIO 6-11 — Flash bus]
        D4[GPIO 12 — VDD_SDIO]
        D5[GPIO 15 — JTAG]
    end
```

## Quvvat ta'minoti sxemasi

```mermaid
graph TD
    subgraph POWER["Quvvat manbai"]
        SOLAR[☀️ Quyosh paneli<br/>6V]
        BATTERY[🔋 Akkumulyator<br/>3.7V Li-ion]
        USB[🔌 USB<br/>5V]
    end

    subgraph REG["Kuchlanish regulyatori"]
        R33[3.3V Regulator]
    end

    subgraph DEVICES["Qurilmalar"]
        ESP[ESP32 — 3.3V]
        SENS[Sensorlar — 3.3V]
        REL[Relay — 3.3V]
    end

    SOLAR --> BATTERY
    BATTERY --> R33
    USB --> R33
    R33 --> ESP
    R33 --> SENS
    R33 --> REL
```

## Sensor ishlash prinsipi

```mermaid
sequenceDiagram
    participant ESP as ESP32
    participant US as RCWL-9610A

    ESP->>US: TRIG = HIGH (10μs)
    ESP->>US: TRIG = LOW
    US->>US: Ultratovush yuborish
    Note over US: Tovush to'siqqa uriladi
    US->>US: Aks-sado qaytadi
    US->>ESP: ECHO = HIGH (duration)
    ESP->>ESP: Masofa = duration × 0.034 / 2
```

## Muhim eslatmalar

> ⚠️ **RCWL-9610A** 3.3V da ishlaydi — to'g'ridan-to'g'ri ESP32 ga ulash mumkin
>
> ⚠️ **Relay** 3.3V logic bilan ishlashi kerak (5V relay ishlamaydi)
>
> ⚠️ **GPIO 34** faqat input — analog o'qish uchun ideal
>
> ⚠️ **Kod yuklash paytida** barcha simlarni ajrating
>
> ⚠️ **GPIO 5, 6-11, 12, 15** ishlatmang — strapping/flash pinlar
