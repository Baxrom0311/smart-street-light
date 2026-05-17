# Tizim Arxitekturasi

## Umumiy arxitektura

```mermaid
graph TB
    subgraph Hardware["🔧 Hardware (ESP32)"]
        US[RCWL-9610A<br/>Ultratovush sensor]
        LS[TEMT6000<br/>Yorug'lik sensor]
        ESP[ESP32 DevKit<br/>Mikrokontroller]
        RL[Relay Module]
        LED[LED Chiroq]
        SP[Quyosh Paneli]
    end

    subgraph Cloud["☁️ Firebase Cloud"]
        RTDB[(Realtime<br/>Database)]
        AUTH[Authentication]
        HOST[Hosting]
    end

    subgraph Client["📱 Web Dashboard"]
        PWA[React PWA]
        UI[Dashboard UI]
    end

    US -->|Masofa| ESP
    LS -->|Yorug'lik| ESP
    SP -->|Quvvat| ESP
    ESP -->|GPIO 26| RL
    RL -->|ON/OFF| LED

    ESP <-->|WiFi/HTTPS| RTDB
    RTDB <-->|WebSocket| PWA
    HOST -->|Serve| PWA
    PWA --> UI
    AUTH -->|Login| PWA
```

## Ma'lumot oqimi

```mermaid
sequenceDiagram
    participant S as Sensorlar
    participant E as ESP32
    participant F as Firebase RTDB
    participant D as Dashboard

    loop Har 300ms
        S->>E: Masofa + Yorug'lik
        E->>E: Harakat aniqlash (debounce)
        E->>E: Relay boshqarish
    end

    loop Har 3s
        E->>F: device/status yangilash
    end

    F-->>D: Real-time listener (WebSocket)
    D->>F: control/mode o'zgartirish
    F-->>E: Stream callback
    E->>E: Rejim o'zgartirish
```

## Rejimlar diagrammasi

```mermaid
stateDiagram-v2
    [*] --> Auto: Default

    Auto --> Manual: Dashboard buyruq
    Auto --> Schedule: Dashboard buyruq
    Manual --> Auto: Dashboard buyruq
    Manual --> Schedule: Dashboard buyruq
    Schedule --> Auto: Dashboard buyruq
    Schedule --> Manual: Dashboard buyruq

    state Auto {
        [*] --> Kutish
        Kutish --> Yoniq: Qorong'u + Harakat
        Yoniq --> Kutish: 5s harakat yo'q
        Yoniq --> Ochiq: Yorug' bo'ldi
        Kutish --> Ochiq: Yorug' bo'ldi
        Ochiq --> Kutish: Qorong'u bo'ldi
    }

    state Manual {
        [*] --> OFF
        OFF --> ON: Toggle
        ON --> OFF: Toggle
    }

    state Schedule {
        [*] --> Tekshirish
        Tekshirish --> Yoniq_S: Vaqt keldi (ON)
        Tekshirish --> Ochiq_S: Vaqt keldi (OFF)
        Yoniq_S --> Tekshirish: Har daqiqa
        Ochiq_S --> Tekshirish: Har daqiqa
    }
```

## Auto rejim flowchart

```mermaid
flowchart TD
    A[Start: Loop] --> B{Yorug'lik > 350?}
    B -->|Ha - Kunduz| C[LED O'CHIQ]
    B -->|Yo'q - Qorong'u| D{Yorug'lik < 250?}
    D -->|Ha| E[isDark = true]
    D -->|Yo'q| F[Hysteresis: o'zgarmaydi]
    E --> G{Harakat bormi?<br/>Distance < 200cm}
    F --> G
    G -->|Ha| H[LED YONIQ]
    G -->|Yo'q| I{5s o'tdimi?}
    I -->|Ha| J[LED O'CHIQ]
    I -->|Yo'q| K[LED YONIQ qoladi]
    C --> A
    H --> A
    J --> A
    K --> A
```

## Sensor debounce logikasi

```mermaid
flowchart LR
    A[O'lchov 1] --> D{3 ta o'lchov<br/>ichida 2 ta<br/>harakat?}
    B[O'lchov 2] --> D
    C[O'lchov 3] --> D
    D -->|Ha| E[lastMotionTime = now]
    D -->|Yo'q| F[O'zgarmaydi]
    E --> G{now - lastMotionTime<br/>< 5000ms?}
    F --> G
    G -->|Ha| H[Motion = TRUE]
    G -->|Yo'q| I[Motion = FALSE]
```

## Tizim komponentlari

```mermaid
graph LR
    subgraph ESP32
        MAIN[main.cpp] --> SENS[sensors.cpp]
        MAIN --> LC[light_control.cpp]
        MAIN --> FB[firebase_handler.cpp]
        MAIN --> STAT[statistics.cpp]
    end

    subgraph Firebase
        RTDB[(Realtime DB)]
        RTDB --> STATUS[/device/status/]
        RTDB --> CONTROL[/device/control/]
        RTDB --> CONFIG[/device/config/]
        RTDB --> HIST[/history/]
        RTDB --> LOG[/motion_log/]
    end

    subgraph React_PWA
        APP[App.jsx] --> DASH[Dashboard.jsx]
        APP --> STATS[Statistics.jsx]
        APP --> MLOG[MotionLog.jsx]
    end

    FB <--> RTDB
    RTDB <--> APP
```

## Deploy arxitekturasi

```mermaid
graph LR
    DEV[Developer] -->|pio upload| ESP32
    DEV -->|npm run build| DIST[dist/]
    DIST -->|firebase deploy| FH[Firebase Hosting]
    FH -->|HTTPS| USER[Foydalanuvchi]
    ESP32 -->|WiFi| FRTDB[Firebase RTDB]
    FRTDB -->|WebSocket| USER
```
