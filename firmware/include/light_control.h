#pragma once
#include <Arduino.h>

void setupLightControl();
void loopLightControl();
bool isLightOn();
void setManualLight(bool on);
void setMode(const String &mode);
String getMode();
void setConfig(int timeout, int lightTh, int distTh);
int getTimeoutSec();
int getLightThreshold();
int getDistanceThreshold();
