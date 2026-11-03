# Copy this file to config.py and edit it. config.py is ignored by git.
# These pin numbers are GPIO numbers on a Raspberry Pi Pico. Change them to match your wiring.

SOIL_ADC_PIN = 26        # GP26 = ADC0 (physical pin 31)
DHT_PIN = 15             # GP15 (physical pin 20)
INTERVAL_S = 600         # seconds between readings (600 = every 10 minutes)

# Calibration: read the sensor in dry air and again in a glass of water, then put the raw values here.
# The numbers below are placeholders and WILL be wrong for your sensor.
SOIL_DRY_RAW = 50000
SOIL_WET_RAW = 25000

LOG_FILE = "readings.csv"
