#pragma once

// WiFi credentials (hardcode fallback)
#define WIFI_SSID "baxrom0311"
#define WIFI_PASS "baxrom0311"

// Pin definitions
#define TRIG_PIN 4    // Ultrasonic TRIG - xavfsiz output pin
#define ECHO_PIN 16   // Ultrasonic ECHO - xavfsiz input pin
#define LIGHT_PIN 34  // TEMT6000 analog - faqat input pin (ADC1)
#define LED_STRIP_PIN 27  // WS2812B data pin
#define NUM_LEDS 13       // LED strip soni
#define LED_PIN 2     // Onboard LED (status)

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
