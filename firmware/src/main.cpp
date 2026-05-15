#include <Arduino.h>
#include <WiFi.h>
#include <WiFiManager.h>
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include "firebase_handler.h"
#include "statistics.h"

WiFiManager wm;

void setupWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.print("WiFi ga ulanmoqda");

  unsigned long start = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - start < 10000) {
    delay(500);
    Serial.print(".");
  }

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("\nHardcode WiFi topilmadi. WiFiManager AP ochilmoqda...");
    wm.setConfigPortalTimeout(180);
    if (!wm.autoConnect("SmartLight-AP")) {
      Serial.println("WiFi ulanmadi. Qayta ishga tushirilmoqda...");
      ESP.restart();
    }
  }

  Serial.println("\nWiFi ulandi!");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("\n=== Smart Street Light ===");

  setupWiFi();
  setupSensors();
  setupLightControl();
  setupFirebase();
  setupStatistics();
}

void loop() {
  loopSensors();
  loopLightControl();
  loopFirebase();
  loopStatistics();
}
