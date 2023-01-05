import vtk
from settings import globalvars
from models.colormap import CUSTOM_COLORMAP

def getBytes(inters):
    volume = vtk.vtkVolume()
    camera = vtk.vtkCamera()
    render = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()

    # reader
    path = inters.get("path")
    globalvars.dicomImageReader.SetDirectoryName(path)
    globalvars.dicomImageReader.Update()

    # mapper
    globalvars.volMap.SetInputData(globalvars.dicomImageReader.GetOutput())

    # volume
    volume.SetMapper(globalvars.volMap)

    # volume property
    rgbPoints = CUSTOM_COLORMAP.get("STANDARD_CT").get("rgbPoints")
    globalvars.color.RemoveAllPoints()
    for point in rgbPoints:
        globalvars.color.AddRGBPoint(point[0], point[1], point[2], point[3])

    preset = inters.get("preset")
    if preset == "bone":
        # bone
        globalvars.scalarOpacity.RemoveAllPoints()
        globalvars.scalarOpacity.AddPoint(0, 0)
        globalvars.scalarOpacity.AddPoint(500, 0.15)
        globalvars.scalarOpacity.AddPoint(800, 1)
    else:
        # skin
        globalvars.scalarOpacity.RemoveAllPoints()
        globalvars.scalarOpacity.AddPoint(-500, 0)
        globalvars.scalarOpacity.AddPoint(500, 1)
    
    globalvars.gradientOpacity.RemoveAllPoints()
    globalvars.gradientOpacity.AddPoint(0, 0)
    globalvars.gradientOpacity.AddPoint(90, 0.5)
    globalvars.gradientOpacity.AddPoint(100, 1)

    globalvars.volProperty.SetColor(globalvars.color)
    globalvars.volProperty.SetScalarOpacity(globalvars.scalarOpacity)
    globalvars.volProperty.SetGradientOpacity(globalvars.gradientOpacity)
    
    volume.SetProperty(globalvars.volProperty)
    center = volume.GetCenter()
    volume.SetPosition(-center[0], -center[1], -center[2])

    # camera
    camera.SetClippingRange(1, 5000)
    camera.SetPosition(0, 0, 1)
    if len(inters):
        for inter in inters.keys():
            if inter == "roll": camera.Roll(inters.get(inter))
            elif inter == "azimuth": camera.Azimuth(inters.get(inter))
            elif inter == "elevation": camera.Elevation(inters.get(inter))
            elif inter == "position": camera.SetPosition(0, 0, inters.get(inter))

    # render
    render.SetBackground(globalvars.colors.GetColor3d("white"))
    render.SetActiveCamera(camera)
    render.AddVolume(volume)

    # render window
    renWin.AddRenderer(render)
    renWin.SetSize(300, 300)
    renWin.OffScreenRenderingOn()

    # write to memory
    globalvars.winToImg.SetInput(renWin)
    globalvars.writer.SetInputConnection(globalvars.winToImg.GetOutputPort())
    globalvars.writer.WriteToMemoryOn()
    globalvars.writer.Write()

    return bytes(memoryview(globalvars.writer.GetResult()))