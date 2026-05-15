#include "statistics.h"
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include <WiFi.h>
#include <FirebaseESP32.h>
#include <time.h>

extern FirebaseData fbdo;

static unsigned long onDurationMs = 0;
static unsigned long darkDurationMs = 0;
static unsigned long lastCheck = 0;
static int motionsCount = 0;
static bool lastMotionState = false;
static unsigned long lastSave = 0;

static String getDateStr() {
  struct tm t;
  if (!getLocalTime(&t)) return "";
  char buf[11];
  sprintf(buf, "%04d-%02d-%02d", t.tm_year + 1900, t.tm_mon + 1, t.tm_mday);
  return String(buf);
}

void setupStatistics() {
  configTime(GMT_OFFSET_SEC, DAYLIGHT_OFFSET_SEC, NTP_SERVER);
  Serial.println("NTP sinxronizatsiya...");
  lastCheck = millis();
}

void loopStatistics() {
  if (!Firebase.ready()) return;

  unsigned long now = millis();
  unsigned long elapsed = now - lastCheck;
  lastCheck = now;

  // Track dark time and on time
  if (getAmbientLight() < getLightThreshold()) {
    darkDurationMs += elapsed;
    if (isLightOn()) onDurationMs += elapsed;
  }

  // Count motions (rising edge)
  bool currentMotion = isMotionDetected();
  if (currentMotion && !lastMotionState) motionsCount++;
  lastMotionState = currentMotion;

  // Save to Firebase every 60 seconds
  if (now - lastSave < 60000) return;
  lastSave = now;

  String date = getDateStr();
  if (date.isEmpty()) return;

  int onMin = onDurationMs / 60000;
  int darkMin = darkDurationMs / 60000;
  int savedPercent = (darkMin > 0) ? ((darkMin - onMin) * 100 / darkMin) : 0;

  String path = "/history/" + date;
  FirebaseJson json;
  json.set("motions_count", motionsCount);
  json.set("on_duration_min", onMin);
  json.set("energy_saved_percent", savedPercent);

  Firebase.set(fbdo, path.c_str(), json);
}
