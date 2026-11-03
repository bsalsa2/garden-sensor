# Reference assembly notes

## What is included

- Raspberry Pi Pico H envelope: 51 × 21 mm published board outline.
- DFRobot SEN0193 soil-probe envelope: 98 × 23 mm published outline.
- DHT22 module envelope: 28 × 13 × 10 mm, provisional; measure the actual module.
- Enclosure: 100 × 70 × 24 mm, provisional design choice.
- Ventilated lid and internal electronics layout.

## Generated model files

- [Editable FreeCAD document (.FCStd)](garden_sensor_reference_assembly.FCStd)
- [STEP assembly](garden_sensor_reference_assembly.step)
- [STL preview](garden_sensor_reference_assembly.stl)
- `generate_reference_model.py`: editable CadQuery source; regenerates STEP and STL.
- `generate_reference_assembly.FCMacro`: FreeCAD macro; regenerates the editable `.FCStd` document and STEP export.

## Important limitation

This is a **reference layout**, not a measured production assembly or a record of a completed physical build. The actual sensor kit, connector orientation, header clearance, screw locations, DHT22 module dimensions, cable routing, and enclosure fit have not been verified. Do not print the enclosure or represent this as final CAD until the actual parts have been measured and the model checked against them.

The soil probe is shown outside the enclosure. Keep its upper electronics and connector dry; only the probe's marked sensing portion belongs in soil.
