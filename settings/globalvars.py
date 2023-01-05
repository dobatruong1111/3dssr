import vtk

colors = vtk.vtkNamedColors()

dicomImageReader = vtk.vtkDICOMImageReader()

volMap = vtk.vtkSmartVolumeMapper()
volMap.SetBlendModeToComposite()
volMap.SetRequestedRenderModeToGPU()

volProperty = vtk.vtkVolumeProperty()
volProperty.ShadeOn()
volProperty.SetInterpolationTypeToLinear()
volProperty.SetAmbient(0.4)
volProperty.SetDiffuse(1.0)
volProperty.SetSpecular(0.4)

gradientOpacity = vtk.vtkPiecewiseFunction()
scalarOpacity = vtk.vtkPiecewiseFunction()
color = vtk.vtkColorTransferFunction()

winToImg = vtk.vtkWindowToImageFilter()
writer = vtk.vtkPNGWriter()