#include "sensors.h"
#include "config.h"

static float distance_cm = 0;
static int ambient_light = 0;
static bool motion = false;
static unsigned long lastRead = 0;

void setupSensors() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.println("Sensorlar tayyor");
}

void loopSensors() {
  if (millis() - lastRead < 500) return;
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

  // Motion detection based on distance threshold
  motion = (distance_cm < DEFAULT_DISTANCE_THRESHOLD && distance_cm > 0);

  Serial.printf("Distance: %.1fcm | Light: %d | Motion: %s\n",
                distance_cm, ambient_light, motion ? "YES" : "NO");
}

float getDistance() { return distance_cm; }
int getAmbientLight() { return ambient_light; }
bool isMotionDetected() { return motion; }
