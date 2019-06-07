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
        
        # selection filters
        # https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-03033DE6-AD8E-46B3-B4E6-DADA8D389E4E
        selectedItem1 = ui.selectEntity("Select a body", "Bodies")
        selectedItemPoint1 = selectedItem1.point
        selectedItem2 = ui.selectEntity("Select another body", "Bodies")
        selectedItemPoint2 = selectedItem2.point
        lengthBetweenPoints = selectedItemPoint1.distanceTo(selectedItemPoint2)
    
        ui.messageBox("length between cylinders is: " + lengthBetweenPoints)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
