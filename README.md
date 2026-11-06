# Garden Sensor

A small garden-monitoring project built around a Raspberry Pi Pico. The idea is to collect soil-moisture and air-condition readings and keep a simple record so changes can be compared over time.

**Project status:** Design and firmware are in progress. The CAD files are reference models, and the hardware has not yet been documented as assembled or tested.

## What the project is meant to do

- Read an analog capacitive soil-moisture sensor.
- Read air temperature and relative humidity from a DHT22 sensor.
- Save readings as CSV data on the Pico.
- Print each reading over the USB serial connection so it can be viewed on a computer.

The current firmware is a starting point. It has not been verified on the finished hardware, so the wiring and configuration should be checked against the exact parts used.

## Current design

The software and wiring documents currently describe a **Raspberry Pi Pico H**, a capacitive soil sensor, and a DHT22 module. The Pico reads the soil sensor through an ADC input and reads the DHT22 through a digital GPIO pin.

The parts list has changed during planning. Check the [bill of materials](bom.csv) before ordering anything; it may need to be updated to match the final board and sensors.

## Hardware and wiring

| Part | Purpose | Status |
|---|---|---|
| Raspberry Pi Pico | Reads sensors and runs MicroPython | Planned |
| Capacitive soil-moisture sensor | Measures soil moisture as an analog signal | Sensor owned; exact model should be confirmed |
| DHT22 module | Measures air temperature and humidity | Planned |
| USB power and data cable | Powers the Pico and connects it to a computer | Required |
| Enclosure | Protects the electronics | CAD reference exists; fit not verified |
| Jumper wires | Connect the sensors to the Pico | Required |

The proposed pin connections and safety checks are in [the wiring guide](garden-sensor/docs/wiring.md). Check the labels on the actual modules before wiring. The Pico uses 3.3 V GPIO, so sensor signal voltage must stay within the Pico's input limits.

## How the firmware works

The MicroPython program repeatedly:

1. Reads the soil sensor's raw ADC value.
2. Converts that value to a percentage using dry and wet calibration readings.
3. Requests temperature and humidity from the DHT22.
4. Appends a row to a CSV log.
5. Prints the row over the serial connection, then waits for the next interval.

The default interval and calibration values are in [the example configuration](garden-sensor/firmware/config.example.py). The program assumes a DHT22 on the configured digital pin and a capacitive sensor on the configured ADC pin.

A soil-moisture percentage is an estimate based on calibration, not a universal measurement of water content. Calibration should be done with the actual sensor and soil.

## CAD and project files

The enclosure model is a **provisional reference design**. It has not been checked against measured components or a completed physical build.

- [Editable Onshape garden sensor document](https://cad.onshape.com/documents/76dcfb4d009c138c2a52466f/w/306111fc660342a21d2bcbd/e/0c180c4d4b855de5293ec742)
- [Editable FreeCAD source (.FCStd)](garden-sensor/hardware/garden_sensor_reference_assembly.FCStd)
- [STEP assembly export (.step)](garden-sensor/hardware/garden_sensor_reference_assembly.step)
- [STL preview (.stl)](garden-sensor/hardware/garden_sensor_reference_assembly.stl)
- [CadQuery model generator](garden-sensor/hardware/generate_reference_model.py)
- [FreeCAD macro](garden-sensor/hardware/generate_reference_assembly.FCMacro)
- [CAD assumptions and limitations](garden-sensor/hardware/REFERENCE_ASSEMBLY.md)
- [Wiring diagram](garden-sensor/docs/wiring-diagram.svg)

The enclosure dimensions and internal clearances are provisional. Measure the actual board, sensor modules, connectors, and cables before making a final enclosure.

## Repository contents

- `garden-sensor/firmware/` — MicroPython program, configuration example, and sensor/data logic.
- `garden-sensor/hardware/` — CAD source files and model exports.
- `garden-sensor/docs/` — Wiring notes, diagrams, and design-status documentation.
- `garden-sensor/tests/` — Tests for hardware-independent data and calibration functions.
- `garden-sensor/tools/` — Utilities for working with logged readings.
- `bom.csv` — Parts list and purchasing notes.

## PCB status

This version uses a standard development board and separate sensor modules connected with jumper wires. It does not have a custom-designed PCB, so there are no project-specific KiCad or EasyEDA schematic, board-layout, or Gerber files. See [the PCB status note](garden-sensor/docs/pcb_status.md).

## Testing and limitations

The firmware's hardware-independent logic can be tested on a regular computer, but that does not prove the sensors or complete device work. The hardware build, sensor calibration, enclosure fit, and outdoor performance still need to be checked and recorded.

The soil probe's electronics and connector should be kept dry. Do not assume that an enclosure or sensor module is weatherproof unless its rating and the cable entries have been checked for the actual installation.

## Next steps

- Confirm the exact Pico board and sensor module models.
- Bring the bill of materials and wiring guide into line with the final parts.
- Assemble the circuit and verify each sensor reading.
- Calibrate the soil sensor using the soil and growing setup where it will be used.
- Check the enclosure fit, cable routing, and protection from rain and condensation.
- Record test results and any changes made to the design.

## Credits

This project uses the Raspberry Pi Pico and MicroPython ecosystem. Component-specific libraries, datasheets, and design references should be credited here as they are selected and used.
