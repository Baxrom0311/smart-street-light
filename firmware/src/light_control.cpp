#include "light_control.h"
#include "sensors.h"
#include "config.h"

static bool lightOn = false;
static bool manualLight = false;
static String mode = "auto";
static unsigned long lastMotionTime = 0;
static int timeoutSec = DEFAULT_TIMEOUT_SEC;
static int lightThreshold = DEFAULT_LIGHT_THRESHOLD;
static int distanceThreshold = DEFAULT_DISTANCE_THRESHOLD;

static void setRelay(bool on) {
  lightOn = on;
  digitalWrite(RELAY_PIN, on ? HIGH : LOW);
  digitalWrite(LED_PIN, on ? HIGH : LOW);
}

void setupLightControl() {
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  setRelay(false);
  Serial.println("Rele tayyor");
}

void loopLightControl() {
  if (mode == "manual") {
    setRelay(manualLight);
    return;
  }

  // Auto mode
  bool isDark = getAmbientLight() < lightThreshold;
  bool motion = isMotionDetected();

  if (motion) lastMotionTime = millis();

  if (isDark && (millis() - lastMotionTime < (unsigned long)timeoutSec * 1000)) {
    setRelay(true);
  } else {
    setRelay(false);
  }
}

bool isLightOn() { return lightOn; }
void setManualLight(bool on) { manualLight = on; }
void setMode(const String &m) { mode = m; }
String getMode() { return mode; }
int getTimeoutSec() { return timeoutSec; }
int getLightThreshold() { return lightThreshold; }
int getDistanceThreshold() { return distanceThreshold; }

void setConfig(int timeout, int lightTh, int distTh) {
  if (timeout > 0) timeoutSec = timeout;
  if (lightTh > 0) lightThreshold = lightTh;
  if (distTh > 0) distanceThreshold = distTh;
}
