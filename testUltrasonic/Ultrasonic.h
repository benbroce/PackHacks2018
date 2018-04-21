#ifndef HEADER_ULTRASONIC
#define HEADER_ULTRASONIC

class Ultrasonic {
    private:
        // dist(mm) = ping(uS) * [1(s)/1M(uS)]*[343(m/s)]*[1000(mm/m)]*[1/2]
        //const float PING_US_TO_DIST_MM = 0.1715;
        const int PING_DELAY_MS = 4;
        const long MAX_TIME = 250000;
        const uint8_t trigPin;
        const uint8_t echoPin;
        long read_raw();
        long rawLow = 0;
        long rawHigh = 100;
        long calLow = 0;
        long calHigh = 100;

    public:
        Ultrasonic(uint8_t _trigPin, uint8_t _echoPin);
        void calibrate(int dist, bool highRange);
        void setMap(int _rawLow, int _rawHigh, int _calLow, int _calHigh);
        long read();
        long read(int pings);
};

#endif
