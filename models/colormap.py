def to_rgb_points(colormap):
    rgb_points = []
    for item in colormap:
        crange = item['range']
        color = item['color']
        for index, r in enumerate(crange):
            if len(color) == len(crange):
                rgb_points.append([r] + color[index])
            else:
                rgb_points.append([r] + color[0])
    return rgb_points

COLORMAP_CT = [
    {
        "name": 'air',
        "range": [-1000],
        "color": [[0, 0, 0]]
    },
    {
        "name": 'lung',
        "range": [-600, -400],
        "color": [[194 / 255, 105 / 255, 82 / 255]]
    },
    {
        "name": 'fat',
        "range": [-100, -60],
        "color": [[194 / 255, 166 / 255, 115 / 255]]
    },
    {
        "name": 'soft tissue',
        "range": [40, 80],
        "color": [[102 / 255, 0, 0], [153 / 255, 0, 0]]
    },
    {
        "name": 'bone',
        "range": [400, 1000],
        "color": [[255 / 255, 217 / 255, 163 / 255]]
    }
]

CUSTOM_COLORMAP = {
    "STANDARD_CT": {
        "id": "color-map-standard-ct",
        "name": "Standard color map for CT",
        "modalityTypes": ["CT"],
        "rgbPoints": to_rgb_points(COLORMAP_CT),
        "options": {}
    },
    "BLACK_TO_WHITE": {
        "id": "color-map-black-to-white",
        "name": "Black to white",
        "rgbPoints": to_rgb_points([]),
        "options": {
            "lowerBoundColor": [0, 0, 0],
            "upperBoundColor": [1, 1, 1]
        }
    }
}

