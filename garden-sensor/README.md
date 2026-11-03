# Garden Sensor

A small, low-cost sensor station that measures **TODO: what it measures, e.g. soil moisture and air temperature** in a garden bed and **TODO: what it does with the readings, e.g. logs them to a file / shows them on a screen**, so watering and planting decisions can be based on data instead of guesswork.

> **Status:** TODO: pick one and keep it honest: *design in progress* / *building* / *working on the bench* / *running in the garden since DATE*.

<!-- TODO: add a photo or two of the finished build, and a screenshot of the readings.
     Before uploading photos, remove location data (EXIF) and don't show your house number or street. -->

## Why I'm building this

TODO: two or three honest sentences about the problem you want to solve. For example, what goes wrong when you water by feel, or what you'd like to know about your garden that you can't see now.

## What it does

Only list what is actually working. Move anything unfinished to the roadmap.

- [ ] TODO: Measures **...** every **...** minutes
- [ ] TODO: Stores readings in **...** (CSV file on an SD card, serial output, etc.)
- [ ] TODO: Shows or sends them by **...**

## Hardware

| Part | Qty | What it's for | Notes |
|---|---|---|---|
| TODO: microcontroller board | 1 | Runs the firmware | |
| TODO: soil moisture sensor | 1 | Measures how wet the soil is | Needs calibration, see below |
| TODO: temperature (and humidity) sensor | 1 | Air conditions | |
| TODO: power (battery pack / USB supply) | 1 | | |
| TODO: weatherproof enclosure | 1 | Protects the electronics | |
| TODO: wires, connectors, screws | | | |

**Estimated cost:** TODO (add up the real prices; say if any parts were donated or granted).

## How it works

```
[soil sensor] ──┐
                ├──> [microcontroller] ──> [storage / display]
[air sensor]  ──┘            ▲
                        [power supply]
```

TODO: replace the diagram above if your design is different, then add two or three sentences on what the firmware does each cycle (wake, read sensors, convert, save, sleep).

## Wiring

| Sensor / part | Sensor pin | Board pin |
|---|---|---|
| TODO | TODO | TODO |

TODO: add a wiring diagram or photo in `docs/`.

## Build it yourself

1. **Get the parts** listed above.
2. **Make the case.** TODO: link to the CAD or print files in this repo (for example `hardware/`).
3. **Wire it** following the table above. Double-check power polarity before connecting anything.
4. **Flash the firmware.** Install MicroPython on the board, then copy the code over (this assumes a Raspberry Pi Pico; adjust if you use something else):
   ```
   cp firmware/config.example.py firmware/config.py     # then edit config.py
   pip install mpremote
   mpremote cp firmware/logic.py :logic.py
   mpremote cp firmware/config.py :config.py
   mpremote cp firmware/main.py :main.py
   ```
5. **Calibrate the soil sensor.** Read the sensor in dry air and again in a glass of water, and put those two raw values in `firmware/config.py` as `SOIL_DRY_RAW` and `SOIL_WET_RAW`. Different sensors and different soils read differently, so don't skip this.
6. **Put it in the garden bed** and check that the readings change when you water.

## Configuration

Settings such as the pins, the reading interval and the calibration values live in `firmware/config.py` (copy `firmware/config.example.py` and edit it).

**Never commit secrets** (Wi-Fi passwords, API keys). Keep them in a file that is listed in `.gitignore`, and commit a copy with fake values, such as `config.example.py`.

## Data format

Readings are saved one per line in `readings.csv` on the board. `uptime_s` is seconds since the board started (the Pico has no clock that survives a power cut). An empty cell means the sensor gave no reading. `data/example_readings_made_up.csv` shows the format with **made-up numbers, not real measurements**.

```
uptime_s,soil_moisture_raw,soil_moisture_pct,air_temp_c,air_humidity_pct
```

To plot a file: `python tools/plot_readings.py readings.csv plot.png` (needs `pip install matplotlib`).

Run the tests with `python -m unittest discover -s tests -v`.

## Accuracy and known limits

Be specific about what you actually checked. For example:

- TODO: how you checked the soil readings (for example, weighing a pot of soil dry and wet, or comparing with a hand test)
- TODO: how long it has run outdoors, and what failed (condensation, battery life, sensor drift, wires coming loose)
- TODO: anything you know it does *not* measure well

## Repository layout

```
firmware/     code that runs on the board (main.py, logic.py, config.example.py)
tests/        unit tests for the calculations
tools/        plot_readings.py
docs/         wiring.md, BUILD_LOG.md, photos
data/         example readings (made up)
```

## Build log

TODO: link to your journal or build notes, with dates and hours, showing the real process including what didn't work.

## Roadmap

- [ ] TODO: next improvement
- [ ] TODO: another one

## License

TODO: choose and add a `LICENSE` file. Common choices are MIT for code and CERN-OHL or CC BY for hardware designs.

## Credits

TODO: credit libraries, tutorials, and designs you used or adapted, with links. If a program or sponsor provided parts or funding, you can thank them here, and some programs ask you to.
