#pragma once

// WiFi credentials (hardcode fallback)
#define WIFI_SSID "YOUR_WIFI_SSID"
#define WIFI_PASS "YOUR_WIFI_PASSWORD"

// Pin definitions
#define TRIG_PIN 5
#define ECHO_PIN 18
#define LIGHT_PIN 34
#define RELAY_PIN 26
#define LED_PIN 2

// Thresholds (defaults, overridden by Firebase)
#define DEFAULT_LIGHT_THRESHOLD 300
#define DEFAULT_DISTANCE_THRESHOLD 200
#define DEFAULT_TIMEOUT_SEC 30

// Firebase credentials
#define FIREBASE_API_KEY "AIzaSyDTGp-CAQmfuhuc4bGYXEaWoEhXnWMpPrU"
#define FIREBASE_DB_URL "https://smart-street-light-iot-default-rtdb.firebaseio.com"
#define FIREBASE_USER_EMAIL "device@smartlight.com"
#define FIREBASE_USER_PASSWORD "SmartLight2026!"

// NTP
#define NTP_SERVER "pool.ntp.org"
#define GMT_OFFSET_SEC 18000  // UTC+5 (Tashkent)
#define DAYLIGHT_OFFSET_SEC 0
