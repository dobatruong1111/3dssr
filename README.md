# Dicom server side rendering

## Run

`sanic server.app`

## API

Example: \\
`POST http://localhost:8000/dicom` \\
`{
    "path": "./data",
    "preset": "bone",
    "position": 500,
    "roll": 0,
    "elevation": 0,
    "azimuth": 0
}` \\
Description: \\

- `path`: path to dicom directory
- `preset`: bone and skin
- `position`: the position of camera
- `roll`: rotate on z-axis
- `elevation`: rotate on x-axis
- `azimuth`: rotate on y-axis

Note: \\

- roll, elevation and azimuth are ordinal