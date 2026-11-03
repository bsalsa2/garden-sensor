# Wiring — proposed Raspberry Pi Pico H build

This pin map matches the current firmware defaults in `firmware/config.example.py`. The parts below are a proposed compatible selection, not proof of what was supplied in a kit or physically assembled. Check the labels and datasheets on the exact parts before connecting power.

## Proposed parts

- Raspberry Pi Pico H (SC0917), with pre-installed headers. The Pico board outline is 51 × 21 mm.
- DFRobot Gravity capacitive soil-moisture sensor, SEN0193. It uses a 3-pin analog interface, operates from 3.3–5.5 V, and is listed as 98 × 23 mm.
- Waveshare DHT22 temperature/humidity module. It is a digital 3-pin module; verify the actual VCC, DATA/DOUT, and GND markings on the module.

## Connections

| Module | Module pin | Pico GPIO / power | Pico physical pin |
|---|---|---|---|
| SEN0193 soil sensor | VCC | 3V3 OUT | 36 |
| SEN0193 soil sensor | GND | GND | 38 |
| SEN0193 soil sensor | AOUT | GP26 / ADC0 | 31 |
| DHT22 module | VCC | 3V3 OUT | 36 |
| DHT22 module | DATA / DOUT | GP15 | 20 |
| DHT22 module | GND | GND | 38 |

The soil sensor's analog output is read by the Pico ADC on GP26. The current firmware reads the DHT22 on GP15 and samples every 600 seconds by default.

## Important checks

1. Confirm the printed labels and pin order on each actual module. Do not rely on wire colors alone.
2. The SEN0193 is not fully waterproof: keep its upper electronics/connector dry and insert only the marked sensing portion into soil.
3. This diagram assumes a 3-pin DHT22 breakout module with the required pull-up circuitry. A bare 4-pin DHT22 may require a 4.7–10 kΩ pull-up resistor between DATA and 3V3; check the exact part.
4. The Pico uses 3.3 V GPIO. Do not connect a signal that can exceed the Pico's input limits.
5. Disconnect USB power before changing wiring.

## Wiring diagram

See [wiring-diagram.svg](wiring-diagram.svg).

## Design status

This is a proposed wiring design based on the firmware assumptions. It has not been verified against a physical build. Update this document and `firmware/config.py` if the actual kit contains different hardware.
