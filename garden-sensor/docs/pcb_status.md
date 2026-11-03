# PCB design status

## Why there are no custom PCB source files

This prototype uses an off-the-shelf Raspberry Pi Pico H development board and separate sensor modules connected with jumper wires. The Pico board and sensor modules are commercially manufactured products; this project does not design, route, or manufacture a custom PCB.

Because no custom PCB was routed by hand, there is no project-owned KiCad/EasyEDA schematic, board layout, or Gerber output to include. The firmware uses the Pico's existing GPIO/ADC pins directly.

## Fabricate explanation text

If the submission form asks why PCB source files are missing, this accurately describes the current design:

> This project does not include a custom PCB. It uses an off-the-shelf Raspberry Pi Pico H development board and separate sensor modules connected with jumper wires. I did not design or hand-route a PCB, so there are no custom schematic, PCB-layout, or Gerber files for this project.

## Scope

This explanation is accurate only while the build uses the standard development board and external modules. If a custom PCB is designed later, add the editable schematic, PCB layout, and manufacturing Gerbers to the repository.
