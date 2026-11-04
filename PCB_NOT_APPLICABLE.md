# PCB sources: not applicable to this design

## Why this repository has no KiCad/EasyEDA schematic, PCB layout, or Gerber files

This garden-sensor prototype is built around an off-the-shelf Raspberry Pi Pico H development board and separate sensor modules connected with jumper wires. This project does not contain a custom PCB that was designed or routed by hand.

The Pico has its own manufactured circuit board, but it is a purchased development module, not a custom board created for this project. The soil-moisture and temperature/humidity sensors are also purchased modules. Their connections are documented in [the wiring diagram](garden-sensor/docs/wiring-diagram.svg) and [wiring instructions](garden-sensor/docs/wiring.md).

For that reason, there are no project-owned KiCad schematic files, PCB layout files, or Gerber manufacturing outputs to submit. Creating placeholder PCB files would misrepresent the hardware design.

## Text for the Fabricate exemption field

> This project does not have a custom hand-routed PCB. It uses an off-the-shelf Raspberry Pi Pico H development board and separate sensor modules connected with jumper wires. The Pico is a purchased development module, not a PCB designed or routed for this project. Therefore, this project has no custom schematic, PCB layout, or Gerber files. The actual module connections are documented in the wiring diagram and wiring instructions.

This explanation applies only while the project continues to use the standard development board and external sensor modules. If a custom PCB is added later, its editable schematic, layout source, and Gerber manufacturing files should be committed here.
