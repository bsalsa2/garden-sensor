"""Garden Sensor reference assembly (CadQuery, units: mm).

This is a planning model only, not manufacturing-ready CAD. It uses the
published 51 x 21 mm Pico board outline and 98 x 23 mm SEN0193 probe outline.
The DHT22 module envelope (28 x 13 x 10 mm) and enclosure are provisional.
Measure the actual kit before printing or claiming fit.

Run: python generate_reference_model.py
Requires: pip install cadquery
Outputs: garden_sensor_reference_assembly.step and .stl in this folder.
"""
import cadquery as cq
from pathlib import Path

OUT = Path(__file__).resolve().parent

# Provisional enclosure concept.
L, W, H, WALL, FLOOR = 100.0, 70.0, 24.0, 2.0, 2.0
outer = cq.Workplane("XY").box(L, W, H, centered=(True, True, False))
inner = (cq.Workplane("XY").workplane(offset=FLOOR)
         .box(L - 2 * WALL, W - 2 * WALL, H,
              centered=(True, True, False)))
base = outer.cut(inner)

# Removable lid; ventilation slots sit over the approximate DHT22 position.
lid = cq.Workplane("XY").box(L, W, 2.0, centered=(True, True, False)).translate((0, 0, H))
for x in (-12.0, -4.0, 4.0, 12.0):
    vent = (cq.Workplane("XY").workplane(offset=H)
            .center(x, 20.0).slot2D(12.0, 2.0, angle=90).extrude(2.0))
    lid = lid.cut(vent)

# Simplified component envelopes, not detailed manufacturer models.
pico = (cq.Workplane("XY").box(51.0, 21.0, 1.6, centered=(True, True, False))
        .translate((-16.0, -8.0, 4.0)))
dht22 = (cq.Workplane("XY").box(28.0, 13.0, 10.0, centered=(True, True, False))
         .translate((20.0, 17.0, 4.0)))
soil_probe = (cq.Workplane("XY").box(98.0, 23.0, 1.6, centered=(True, True, False))
              .translate((0.0, -58.0, 0.0)))

assembly = cq.Assembly(name="Garden_Sensor_Reference_Assembly")
assembly.add(base, name="Enclosure_Base")
assembly.add(lid, name="Ventilated_Lid")
assembly.add(pico, name="Pico_H_Envelope_51x21")
assembly.add(dht22, name="DHT22_Module_Envelope_Provisional")
assembly.add(soil_probe, name="DFRobot_SEN0193_Envelope_98x23")
assembly.save(str(OUT / "garden_sensor_reference_assembly.step"), cq.exporters.ExportTypes.STEP)
cq.exporters.export(cq.Compound.makeCompound(
    [base.val(), lid.val(), pico.val(), dht22.val(), soil_probe.val()]
), str(OUT / "garden_sensor_reference_assembly.stl"))
print("Wrote reference STEP and STL to", OUT)
