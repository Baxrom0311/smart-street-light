#pragma once
#include <Arduino.h>

void setupSensors();
void loopSensors();
float getDistance();
int getAmbientLight();
bool isMotionDetected();
