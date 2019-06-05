#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        
        # Get the root component of the active design
        rootComp = adsk.fusion.Component.cast(design.rootComponent)
        
        # create a new sketch on the xy plane
        sketches = rootComp.sketches
        xzPlane = rootComp.xZConstructionPlane
        sketch = sketches.add(xzPlane)
        
        # draw circles
        circles = sketch.sketchCurves.sketchCircles
        circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 2)
        cricle2 = circles.addByCenterRadius(adsk.core.Point3D.create(2, 0, 0), 1)
        

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
