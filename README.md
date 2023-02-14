# Dicom server side rendering

## Installation
Install Poetry: https://python-poetry.org/docs/#installation

Install dependencies:
```commandline
poetry install
```
Initialize virtual environment
```commandline
poetry shell
```
Run App
```commandline
poetry run sanic server.app
```
For PyCharm users, check out this guide on how to initialize with Poetry
https://www.jetbrains.com/help/pycharm/poetry.html#9f0a3a09

## API

Example: <br>
`POST http://localhost:8000/dicom` <br>
`{
    "path": "./data",
    "preset": "bone",
    "position": 500,
    "roll": 0,
    "elevation": 0,
    "azimuth": 0
}` <br>
Description: <br>

- `path`: path to dicom directory
- `preset`: bone and skin
- `position`: the position of camera
- `roll`: rotate on z-axis
- `elevation`: rotate on x-axis
- `azimuth`: rotate on y-axis

Note: <br>

- roll, elevation and azimuth are ordinal
