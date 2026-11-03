"""Garden sensor firmware (MicroPython, Raspberry Pi Pico).

Every INTERVAL_S seconds: read soil moisture and air temperature/humidity, save one line to LOG_FILE.
ASSUMES: a capacitive soil moisture sensor on an analog pin and a DHT22 on a digital pin.
Not yet tested on real hardware: change it to match what you actually build.
"""
import os
import time

import dht
from machine import ADC, Pin

import config
from logic import CSV_HEADER, csv_row, raw_to_percent

soil = ADC(config.SOIL_ADC_PIN)
air = dht.DHT22(Pin(config.DHT_PIN))
start = time.ticks_ms()


def file_exists(path):
    try:
        os.stat(path)
        return True
    except OSError:
        return False


def read_air():
    """Returns (temp_c, humidity_pct), or (None, None) if the sensor didn't answer."""
    try:
        air.measure()
        return air.temperature(), air.humidity()
    except OSError:
        return None, None


if not file_exists(config.LOG_FILE):
    with open(config.LOG_FILE, "w") as f:
        f.write(CSV_HEADER + "\n")

while True:
    raw = soil.read_u16()
    pct = raw_to_percent(raw, config.SOIL_DRY_RAW, config.SOIL_WET_RAW)
    temp_c, humidity = read_air()
    uptime_s = time.ticks_diff(time.ticks_ms(), start) // 1000
    line = csv_row(uptime_s, raw, pct, temp_c, humidity)
    with open(config.LOG_FILE, "a") as f:
        f.write(line + "\n")
    print(line)
    time.sleep(config.INTERVAL_S)
