#include "sensors.h"
#include "config.h"

static float distance_cm = 0;
static int ambient_light = 0;
static bool motion = false;
static unsigned long lastRead = 0;
static unsigned long lastMotionTime = 0;

// Debounce: 3 ta o'lchov ichida 2 tasi harakat ko'rsatsa — harakat bor
static int motionCount = 0;
static int readCount = 0;

void setupSensors() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.println("Sensorlar tayyor");
}

void loopSensors() {
  if (millis() - lastRead < 300) return;
  lastRead = millis();

  // Ultrasonic RCWL-9610A
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH, 30000);
  distance_cm = (duration > 0) ? duration * 0.034 / 2.0 : 999;

  // TEMT6000 light sensor
  ambient_light = analogRead(LIGHT_PIN);

  // Motion detection with debounce
  bool currentDetect = (distance_cm < DEFAULT_DISTANCE_THRESHOLD && distance_cm > 2);

  readCount++;
  if (currentDetect) motionCount++;

  // Har 3 o'lchov dan keyin qaror
  if (readCount >= 3) {
    if (motionCount >= 2) {
      lastMotionTime = millis();
    }
    motionCount = 0;
    readCount = 0;
  }

  // Hold: oxirgi harakatdan 5s ichida "motion = true"
  motion = (millis() - lastMotionTime < 5000);

  Serial.printf("Distance: %.1fcm | Light: %d | Motion: %s\n",
                distance_cm, ambient_light, motion ? "YES" : "NO");
}

float getDistance() { return distance_cm; }
int getAmbientLight() { return ambient_light; }
bool isMotionDetected() { return motion; }
