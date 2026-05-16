#include "light_control.h"
#include "sensors.h"
#include "config.h"
#include <FastLED.h>

static CRGB leds[NUM_LEDS];
static bool lightOn = false;
static bool manualLight = false;
static String mode = "auto";
static int timeoutSec = DEFAULT_TIMEOUT_SEC;
static int lightThreshold = DEFAULT_LIGHT_THRESHOLD;
static int distanceThreshold = DEFAULT_DISTANCE_THRESHOLD;
static bool isDarkState = false; // hysteresis holati

static void setStrip(bool on) {
  if (on == lightOn) return;
  lightOn = on;
  digitalWrite(LED_PIN, on ? HIGH : LOW);

  if (on) {
    fill_solid(leds, NUM_LEDS, CRGB::White);
    FastLED.setBrightness(255);
  } else {
    fill_solid(leds, NUM_LEDS, CRGB::Black);
    FastLED.setBrightness(0);
  }
  delay(1);
  FastLED.show();
  delay(1);
  Serial.printf(">>> LED STRIP: %s\n", on ? "ON" : "OFF");
}

void setupLightControl() {
  pinMode(LED_PIN, OUTPUT);
  FastLED.addLeds<WS2812B, LED_STRIP_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(0);
  fill_solid(leds, NUM_LEDS, CRGB::Black);
  FastLED.show();
  Serial.println("LED strip tayyor");
}

void loopLightControl() {
  if (mode == "manual") {
    setStrip(manualLight);
    return;
  }

  // Hysteresis: 250 dan pastga tushsa — qorong'u, 350 dan oshsa — yorug'
  int light = getAmbientLight();
  if (light < lightThreshold - 50) isDarkState = true;
  else if (light > lightThreshold + 50) isDarkState = false;

  if (!isDarkState) {
    setStrip(false);
  } else if (isMotionDetected()) {
    setStrip(true);
  } else {
    setStrip(false);
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
