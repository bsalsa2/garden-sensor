# Fusion 360 script: Garden Sensor enclosure source model
# Run inside Autodesk Fusion 360: Utilities > Scripts and Add-Ins > Scripts > +
# This creates editable parametric bodies. Then use File > Save As to save
# the design as garden_sensor_enclosure.f3d.
#
# Concept dimensions only. Confirm the exact Pico 2 W, sensor breakout,
# connector, cable-gland and fastener dimensions before manufacturing.

import adsk.core
import adsk.fusion
import traceback

def mm(value):
    # Fusion API internal length unit is cm.
    return value / 10.0

def rectangle(sketch, x1, y1, x2, y2):
    lines = sketch.sketchCurves.sketchLines
    lines.addTwoPointRectangle(
        adsk.core.Point3D.create(mm(x1), mm(y1), 0),
        adsk.core.Point3D.create(mm(x2), mm(y2), 0)
    )

def make_offset_plane(component, base_plane, offset_mm):
    planes = component.constructionPlanes
    plane_input = planes.createInput()
    plane_input.setByOffset(base_plane, adsk.core.ValueInput.createByReal(mm(offset_mm)))
    return planes.add(plane_input)

def extrude(component, profile, distance_mm, operation):
    extrudes = component.features.extrudeFeatures
    feature_input = extrudes.createInput(profile, operation)
    feature_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(mm(distance_mm)))
    return extrudes.add(feature_input)

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox('Open a Fusion design first, then run this script.')
            return

        root = design.rootComponent

        # Overall concept enclosure: 110 x 80 x 35 mm, 2.4 mm walls/floor.
        # The board and sensor breakout are represented by fit envelopes only.
        base_occ = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        base_comp = adsk.fusion.Component.cast(base_occ.component)
        base_comp.name = 'Garden Sensor - Enclosure Base'

        outer_sketch = base_comp.sketches.add(base_comp.xYConstructionPlane)
        outer_sketch.name = 'Base outer profile - 110 x 80'
        rectangle(outer_sketch, -55, -40, 55, 40)
        outer_profile = outer_sketch.profiles.item(0)
        base_solid = extrude(base_comp, outer_profile, 35, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        base_solid.name = 'Enclosure base blank'

        # Open cavity from the top, leaving a 2.4 mm floor and side walls.
        cavity_plane = make_offset_plane(base_comp, base_comp.xYConstructionPlane, 35)
        cavity_sketch = base_comp.sketches.add(cavity_plane)
        cavity_sketch.name = 'Internal cavity - 2.4 mm walls'
        rectangle(cavity_sketch, -52.6, -37.6, 52.6, 37.6)
        cavity_profile = cavity_sketch.profiles.item(0)
        cavity_cut = extrude(base_comp, cavity_profile, -32.6, adsk.fusion.FeatureOperations.CutFeatureOperation)
        cavity_cut.name = 'Open enclosure cavity'

        # Four generic internal mounting pads; hole positions are intentionally
        # omitted until the actual board/header and fastener pattern are measured.
        pad_plane = make_offset_plane(base_comp, base_comp.xYConstructionPlane, 2.4)
        pad_sketch = base_comp.sketches.add(pad_plane)
        pad_sketch.name = 'Generic mounting pads'
        circles = pad_sketch.sketchCurves.sketchCircles
        for x, y in [(-43, -28), (-43, 28), (43, -28), (43, 28)]:
            circles.addByCenterRadius(
                adsk.core.Point3D.create(mm(x), mm(y), 0), mm(4.0)
            )
        pad_profile = pad_sketch.profiles.item(0)
        pads = extrude(base_comp, pad_profile, 6.0, adsk.fusion.FeatureOperations.JoinFeatureOperation)
        pads.name = 'Four generic internal pads'

        # Separate removable lid plate, positioned above the base.
        lid_occ = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        lid_comp = adsk.fusion.Component.cast(lid_occ.component)
        lid_comp.name = 'Garden Sensor - Removable Lid'
        lid_plane = make_offset_plane(lid_comp, lid_comp.xYConstructionPlane, 35)
        lid_sketch = lid_comp.sketches.add(lid_plane)
        lid_sketch.name = 'Lid profile - 110 x 80'
        rectangle(lid_sketch, -55, -40, 55, 40)
        lid_profile = lid_sketch.profiles.item(0)
        lid_body = extrude(lid_comp, lid_profile, 2.4, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        lid_body.name = 'Flat removable lid'

        ui.messageBox(
            'Garden Sensor concept enclosure created. Save the design as an .f3d file.\n\n'
            'IMPORTANT: This is provisional geometry, not manufacturing-ready. '
            'Measure the actual Pico 2 W, sensor breakout, cable glands and fasteners; '
            'then revise the mounting and cable-entry details before printing.'
        )
    except:
        if ui:
            ui.messageBox('Fusion script failed:\n{}'.format(traceback.format_exc()))
