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

void streamCallback(StreamData data) {
  String path = data.dataPath();

  if (path == "/mode") {
    setMode(data.stringData());
    Serial.printf("Firebase mode: %s\n", data.stringData().c_str());
  } else if (path == "/manual_light") {
    setManualLight(data.boolData());
    Serial.printf("Firebase manual_light: %d\n", data.boolData());
  } else if (path == "/" && data.dataTypeEnum() == firebase_rtdb_data_type_json) {
    FirebaseJson *json = data.to<FirebaseJson *>();
    FirebaseJsonData result;
    if (json->get(result, "mode")) setMode(result.stringValue);
    if (json->get(result, "manual_light")) setManualLight(result.boolValue);
  }
}

void streamTimeoutCallback(bool timeout) {
  if (timeout) Serial.println("Firebase stream timeout, reconnecting...");
}

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

  // Stream for control commands
  if (Firebase.beginStream(streamData, "/device/control")) {
    Firebase.setStreamCallback(streamData, streamCallback, streamTimeoutCallback);
    Serial.println("Firebase stream boshlandi");
  }

  firebaseReady = true;
  Serial.println("Firebase tayyor");
}

void loopFirebase() {
  if (!Firebase.ready()) return;
  if (millis() - lastSend < 3000) return;
  lastSend = millis();

  // Read config periodically (every 30s)
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

  if (isMotionDetected()) lastMotionTs = millis() / 1000;

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
