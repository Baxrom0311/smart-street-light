#include <Arduino.h>
#include <FastLED.h>

#define DATA_PIN 26
#define NUM_LEDS 13

CRGB leds[NUM_LEDS];

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("FastLED TEST - GPIO 27, 13 LEDs");

  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(255);
  fill_solid(leds, NUM_LEDS, CRGB::Black);
  FastLED.show();
  delay(500);

  Serial.println("WHITE ON");
  fill_solid(leds, NUM_LEDS, CRGB::White);
  FastLED.show();
}

void loop() {
  // 3s oq, 2s o'chiq
  Serial.println("ON - WHITE");
  fill_solid(leds, NUM_LEDS, CRGB::White);
  FastLED.setBrightness(255);
  FastLED.show();
  delay(3000);

  Serial.println("OFF");
  fill_solid(leds, NUM_LEDS, CRGB::Black);
  FastLED.show();
  delay(2000);

  Serial.println("ON - RED");
  fill_solid(leds, NUM_LEDS, CRGB::Red);
  FastLED.setBrightness(255);
  FastLED.show();
  delay(3000);

  Serial.println("OFF");
  fill_solid(leds, NUM_LEDS, CRGB::Black);
  FastLED.show();
  delay(2000);
}
