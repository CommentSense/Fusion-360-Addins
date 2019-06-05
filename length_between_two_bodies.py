#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback,

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        design = app.activeProduct
        
        ui  = app.userInterface
        ui.messageBox('Select two cylindrical faces')
        selectedItem1 = ui.selectEntity("Select a Cylinder", "CylindricalFaces")
        selectedItemPoint1 = selectedItem1.point
        selectedItem2 = ui.selectEntity("Select another Cylinder", "CylindricalFaces")
        selectedItemPoint2 = selectedItem2.point
        lengthBetweenPoints = selectedItemPoint1.distanceTo(selectedItemPoint2)
    
        ui.messageBox("length between cylinders is: " + lengthBetweenPoints)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
