"""Pure functions with no hardware in them, so they can be tested on a normal computer."""


def raw_to_percent(raw, dry, wet):
    """Turn a raw sensor reading into 0-100 % moisture.

    dry = reading in dry air, wet = reading with the sensor in water.
    Works whichever of the two numbers is larger.
    """
    if dry == wet:
        raise ValueError("dry and wet calibration values must be different")
    pct = (raw - dry) / (wet - dry) * 100.0
    return max(0.0, min(100.0, pct))


CSV_HEADER = "uptime_s,soil_moisture_raw,soil_moisture_pct,air_temp_c,air_humidity_pct"


def _fmt(value, digits):
    # An empty cell means "the sensor gave no reading this time".
    return "" if value is None else ("%." + str(digits) + "f") % value


def csv_row(uptime_s, raw, pct, temp_c, humidity_pct):
    return "%d,%d,%s,%s,%s" % (uptime_s, raw, _fmt(pct, 1), _fmt(temp_c, 1), _fmt(humidity_pct, 1))
