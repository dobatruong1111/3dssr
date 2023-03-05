import vtk
from settings import globalvars
from models.colormap import CUSTOM_COLORMAP
from models.preset import BONE_CT, ANGIO_CT, MUSCLE_CT, MIP

class Dicom3D:
    def __init__(self) -> None:
        self.volume = vtk.vtkVolume()
        self.camera = vtk.vtkCamera()
        self.render = vtk.vtkRenderer()
        self.renWin = vtk.vtkRenderWindow()
    
    def getBytes(self, args):
        # reader
        path = args.get("path")
        globalvars.dicomImageReader.SetDirectoryName(path)
        globalvars.dicomImageReader.Update()

        # mapper
        globalvars.volMap.SetInputData(globalvars.dicomImageReader.GetOutput())

        # volume
        self.volume.SetMapper(globalvars.volMap)

        preset = args.get("preset")

        # volume property
        rgbPoints = CUSTOM_COLORMAP.get("STANDARD_CT").get("rgbPoints")
        globalvars.color.RemoveAllPoints()
        for point in rgbPoints:
            globalvars.color.AddRGBPoint(point[0], point[1], point[2], point[3])

        if preset == "bone":
            gradientOpacity = BONE_CT.get('transferFunction').get('opacityRange')
            globalvars.scalarOpacity.RemoveAllPoints()
            globalvars.scalarOpacity.AddPoint(gradientOpacity[0], 0)
            globalvars.scalarOpacity.AddPoint(gradientOpacity[1], 1)

        elif preset == "angio":
            gradientOpacity = ANGIO_CT.get('transferFunction').get('opacityRange')
            globalvars.scalarOpacity.RemoveAllPoints()
            globalvars.scalarOpacity.AddPoint(gradientOpacity[0], 0)
            globalvars.scalarOpacity.AddPoint(gradientOpacity[1], 1)

        elif preset == "muscle":
            gradientOpacity = MUSCLE_CT.get('transferFunction').get('opacityRange')
            globalvars.scalarOpacity.RemoveAllPoints()
            globalvars.scalarOpacity.AddPoint(gradientOpacity[0], 0)
            globalvars.scalarOpacity.AddPoint(gradientOpacity[1], 1)

        else:
            # modality type: CT or MR
            # preset: MIP
            gradientOpacity = MIP.get('transferFunction').get('opacityRange')
            globalvars.scalarOpacity.RemoveAllPoints()
            globalvars.scalarOpacity.AddPoint(gradientOpacity[0], 0)
            globalvars.scalarOpacity.AddPoint(gradientOpacity[1], 1)

        globalvars.volProperty.SetColor(globalvars.color)
        globalvars.volProperty.SetScalarOpacity(globalvars.scalarOpacity)
        
        self.volume.SetProperty(globalvars.volProperty)
        center = self.volume.GetCenter()
        self.volume.SetPosition(-center[0], -center[1], -center[2])

        # camera
        self.camera.SetClippingRange(1, 5000)
        self.camera.SetPosition(0, 0, 1)
        if len(args):
            for inter in args.keys():
                if inter == "roll": self.camera.Roll(args.get(inter))
                elif inter == "azimuth": self.camera.Azimuth(args.get(inter))
                elif inter == "elevation": self.camera.Elevation(args.get(inter))
                elif inter == "position": self.camera.SetPosition(0, 0, args.get(inter))
        
        # render
        self.render.SetBackground(globalvars.colors.GetColor3d("white"))
        self.render.SetActiveCamera(self.camera)
        self.render.AddVolume(self.volume)

        # render window
        self.renWin.AddRenderer(self.render)
        self.renWin.SetSize(300, 300)
        self.renWin.OffScreenRenderingOn()

        # write to memory
        globalvars.winToImg.SetInput(self.renWin)
        globalvars.writer.SetInputConnection(globalvars.winToImg.GetOutputPort())
        globalvars.writer.WriteToMemoryOn()
        globalvars.writer.Write()

        return bytes(memoryview(globalvars.writer.GetResult()))