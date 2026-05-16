#include <Arduino.h>
#include <WiFi.h>
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include "firebase_handler.h"
#include "statistics.h"

static bool wifiConnected = false;
static bool firebaseStarted = false;

void setupWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.print("WiFi ga ulanmoqda");

  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(500);
    Serial.print(".");
    attempts++;
  }

  if (WiFi.status() == WL_CONNECTED) {
    wifiConnected = true;
    Serial.printf("\nWiFi ulandi! IP: %s\n", WiFi.localIP().toString().c_str());
  } else {
    wifiConnected = false;
    Serial.println("\nWiFi ulanmadi. Offline rejimda ishlaydi.");
  }
}

void checkWiFi() {
  static unsigned long lastCheck = 0;
  if (millis() - lastCheck < 30000) return;
  lastCheck = millis();

  if (WiFi.status() != WL_CONNECTED) {
    if (wifiConnected) Serial.println("WiFi uzildi!");
    wifiConnected = false;
    WiFi.reconnect();
  } else if (!wifiConnected) {
    wifiConnected = true;
    Serial.printf("WiFi qayta ulandi! IP: %s\n", WiFi.localIP().toString().c_str());
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("\n=== Smart Street Light v3 ===");

  setupSensors();
  setupLightControl();
  setupWiFi();

  if (wifiConnected) {
    setupFirebase();
    setupStatistics();
    firebaseStarted = true;
  }

  Serial.println("Tizim tayyor!");
}

void loop() {
  loopSensors();
  loopLightControl();
  checkWiFi();

  if (wifiConnected && firebaseStarted) {
    loopFirebase();
    loopStatistics();
  }
}
