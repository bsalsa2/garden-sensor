# Wiring (assumed parts: Raspberry Pi Pico, capacitive soil moisture sensor, DHT22)

Check this against your actual parts and their datasheets before powering anything on.

| Part | Part pin | Pico pin |
|---|---|---|
| Soil moisture sensor | VCC | 3V3 OUT (physical pin 36) |
| Soil moisture sensor | GND | GND (physical pin 38) |
| Soil moisture sensor | AOUT (analog out) | GP26 / ADC0 (physical pin 31) |
| DHT22 | VCC (+) | 3V3 OUT (physical pin 36) |
| DHT22 | GND (-) | GND (physical pin 38) |
| DHT22 | DATA | GP15 (physical pin 20) |

- A bare 4-pin DHT22 usually needs a 10 kilo-ohm resistor between DATA and 3V3. Many 3-pin DHT22 breakout boards already have one. Check yours.
- Keep the electronics inside the case. Only the soil sensor's probe goes in the ground, up to its marked line.
- If your parts differ, edit `firmware/config.py` and this file.
