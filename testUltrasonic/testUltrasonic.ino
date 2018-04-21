#include "Ultrasonic.h"

Ultrasonic probe1(A0, A1);

void setup() {
    Serial.begin(9600);

    Serial.println("1\" cal in 3s");
    delay(3000);
    probe1.calibrate(1, false);
    Serial.println("5\" cal in 3s");
    delay(3000);
    probe1.calibrate(5, true);
    Serial.println("Calibrated");
}

void loop() {
    Serial.println(probe1.read(10));
}
