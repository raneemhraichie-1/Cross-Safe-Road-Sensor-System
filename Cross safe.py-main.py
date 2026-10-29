

from microbit import *
from machine import time_pulse_us
from utime import sleep_us

DETECT_DISTANCE = 35
CLEAR_DISTANCE = 40
FLASH_INTERVAL = 200

pedestrian_detected = False
red_on = False
last_flash = running_time()
last_measurement = running_time()

pin8.write_digital(0)
pin13.write_digital(0)
display.off()

while True:

    # Check distance every 100 milliseconds
    if running_time() - last_measurement >= 100:
        last_measurement = running_time()

        # Working ultrasonic sensor sequence
        pin0.write_digital(0)
        sleep_us(1000)

        print("ECHO before:", pin1.read_digital())

        pin0.write_digital(1)
        sleep_us(10)
        pin0.write_digital(0)

        pulse = time_pulse_us(pin1, 1, 30000)

        if pulse > 0:
            distance = pulse / 58
            print("Distance:", round(distance, 1), "cm")

            if distance <= DETECT_DISTANCE:
                pedestrian_detected = True

            elif distance >= CLEAR_DISTANCE:
                pedestrian_detected = False

        # If a reading fails, keep the previous state

    if pedestrian_detected:
        # Green always OFF
        pin13.write_digital(0)

        # Red flashes continuously
        if running_time() - last_flash >= FLASH_INTERVAL:
            red_on = not red_on
            pin8.write_digital(int(red_on))
            last_flash = running_time()

    else:
        # Red OFF, green solid ON
        red_on = False
        pin8.write_digital(0)
        pin13.write_digital(1)
        last_flash = running_time()

    sleep(10)
