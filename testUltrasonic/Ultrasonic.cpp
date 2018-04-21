#include "Arduino.h"
#include "Ultrasonic.h"

Ultrasonic::Ultrasonic(uint8_t _trigPin, uint8_t _echoPin)
: trigPin(_trigPin), echoPin(_echoPin) {
	pinMode(trigPin, OUTPUT);
	pinMode(echoPin, INPUT);
}

// Calibrates a fixed reading point to its actual [dist]
// Run 2x w/ [highRange] @ true and false to calibrate
void Ultrasonic::calibrate(int dist, bool highRange) {
	if (highRange) {
		rawLow = read_raw();
		calLow = dist;
	} else {
		rawHigh = read_raw();
		calHigh = dist;
	}
}

void Ultrasonic::setMap(int _rawLow, int _rawHigh, int _calLow, int _calHigh) {
	rawLow = _rawLow;
	rawHigh = _rawHigh;
	calLow = _calLow;
	calHigh = _calHigh;
}

// Returns the theoretical distance from sensor (uncalibrated)
int Ultrasonic::read_raw() {
	// Reset trigger
	digitalWrite(trigPin, LOW);
	delayMicroseconds(2);

	// Trigger a ping
	digitalWrite(trigPin, HIGH);
	delayMicroseconds(10);
	digitalWrite(trigPin, LOW);

	// Read pingTime & calc distance
	return pulseIn(echoPin, HIGH, MAX_TIME);
}

// Returns the calibrated distance from the sensor
int Ultrasonic::read() {
	return map(read_raw(), rawLow, rawHigh, calLow, calHigh);
}

// Returns the average of [pings] calibrated readings from the sensor
int Ultrasonic::read(int pings) {
	int sum = 0;
	for (int i = 0; i < pings; i++) {
		sum += read();
		delay(PING_DELAY_MS);
	}
	return (sum / pings);
}
