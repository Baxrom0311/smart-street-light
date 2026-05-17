#include "firebase_handler.h"
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include <WiFi.h>
#include <FirebaseESP32.h>
#include <addons/TokenHelper.h>
#include <addons/RTDBHelper.h>

FirebaseData fbdo;
static FirebaseData streamData;
static FirebaseAuth auth;
static FirebaseConfig fbConfig;
static bool firebaseReady = false;
static unsigned long lastSend = 0;
static unsigned long lastMotionTs = 0;
static bool streamConnected = false;

void setupFirebase() {
  fbConfig.api_key = FIREBASE_API_KEY;
  fbConfig.database_url = FIREBASE_DB_URL;
  auth.user.email = FIREBASE_USER_EMAIL;
  auth.user.password = FIREBASE_USER_PASSWORD;
  fbConfig.token_status_callback = tokenStatusCallback;

  Firebase.reconnectNetwork(true);
  Firebase.begin(&fbConfig, &auth);

  fbdo.setBSSLBufferSize(2048, 512);
  streamData.setBSSLBufferSize(2048, 512);

  firebaseReady = true;
  Serial.println("Firebase tayyor");
}

static void handleStream() {
  if (!streamConnected) {
    if (Firebase.beginStream(streamData, "/device/control")) {
      streamConnected = true;
      Serial.println("Stream ulandi");
    }
    return;
  }

  if (!Firebase.readStream(streamData)) {
    Serial.println("Stream xato, qayta ulanish...");
    streamConnected = false;
    return;
  }

  if (streamData.streamAvailable()) {
    String path = streamData.dataPath();
    Serial.printf("Stream: %s = ", path.c_str());

    if (path == "/mode") {
      String val = streamData.stringData();
      setMode(val);
      Serial.println(val);
    } else if (path == "/manual_light") {
      bool val = streamData.boolData();
      setManualLight(val);
      Serial.println(val ? "true" : "false");
    } else if (path == "/") {
      // Initial load - full JSON
      FirebaseJson *json = streamData.to<FirebaseJson *>();
      FirebaseJsonData result;
      if (json->get(result, "mode")) setMode(result.stringValue);
      if (json->get(result, "manual_light")) setManualLight(result.boolValue);
      Serial.println("(full sync)");
    }
  }
}

void loopFirebase() {
  if (WiFi.status() != WL_CONNECTED) return;
  if (!Firebase.ready()) return;

  // Stream tekshirish — har loop da
  handleStream();

  // Status yuborish — har 3s
  if (millis() - lastSend < 3000) return;
  lastSend = millis();

  // Config o'qish — har 30s
  static unsigned long lastConfig = 0;
  if (millis() - lastConfig > 30000) {
    lastConfig = millis();
    if (Firebase.getJSON(fbdo, "/device/config")) {
      FirebaseJson &json = fbdo.jsonObject();
      FirebaseJsonData result;
      int t = 0, l = 0, d = 0;
      if (json.get(result, "timeout_sec")) t = result.intValue;
      if (json.get(result, "light_threshold")) l = result.intValue;
      if (json.get(result, "distance_threshold")) d = result.intValue;
      setConfig(t, l, d);
    }
  }

  // Motion log
  static bool lastMotionState = false;
  bool currentMotion = isMotionDetected();
  if (currentMotion && !lastMotionState) {
    lastMotionTs = millis() / 1000;
    FirebaseJson logEntry;
    logEntry.set("time", (int)(lastMotionTs * 1000));
    logEntry.set("distance", (int)getDistance());
    logEntry.set("light", getAmbientLight());
    Firebase.push(fbdo, "/motion_log", logEntry);
  }
  lastMotionState = currentMotion;

  if (currentMotion) lastMotionTs = millis() / 1000;

  // Status yuborish
  FirebaseJson json;
  json.set("light_on", isLightOn());
  json.set("motion_detected", isMotionDetected());
  json.set("distance_cm", (int)getDistance());
  json.set("ambient_light", getAmbientLight());
  json.set("mode", getMode());
  json.set("last_motion", (int)lastMotionTs);
  json.set("uptime", (int)(millis() / 1000));
  json.set("wifi_rssi", WiFi.RSSI());

  Firebase.set(fbdo, "/device/status", json);
}

unsigned long getLastMotionTimestamp() { return lastMotionTs; }
