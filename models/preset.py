from models.colormap import CUSTOM_COLORMAP

BONE_CT = {
    'name': 'viewer.preset3D.bone',
    'modalityTypes': ['CT'],
    'transferFunction': {
        'dataRange': [-1269, 2673],
        'opacityRange': [184.129411764706, 2271.070588235294],
    },
    'colorMap': CUSTOM_COLORMAP.get('STANDARD_CT'),
    'gradientOpacity': 0.2,
    'useShadow': True
}

ANGIO_CT = {
    'name': 'viewer.preset3D.angio',
    'modalityTypes': ['CT'],
    'transferFunction': {
        'dataRange': [-3024, 1785],
        'opacityRange': [125.42352941176478, 1785]
    },
    'colorMap': CUSTOM_COLORMAP.get('STANDARD_CT'),
    'gradientOpacity': 0.2,
    'useShadow': True
}

ANGIO_MR = {
    'name': 'viewer.preset3D.angio',
    'modalityTypes': ['MR'],
    'transferFunction': {
        'dataRange': [0, 242],
        'opacityRange': [63.58431372549019, 139.50588235294118]
    },
    'colorMap': CUSTOM_COLORMAP.get('STANDARD_CT'),
    'gradientOpacity': 0.2,
    'useShadow': True
}

MUSCLE_CT = {
    'name': 'viewer.preset3D.muscle',
    'modalityTypes': ['CT'],
    'transferFunction': {
        'dataRange': [-3024, 1785],
        'opacityRange': [-63.16470588235279, 559.1764705882356]
    },
    'colorMap': CUSTOM_COLORMAP.get('STANDARD_CT'),
    'gradientOpacity': 0.2,
    'useShadow': True
}

MIP = {
    'name': 'viewer.preset3D.mip',
    'modalityTypes': ['CT', 'MR'],
    'transferFunction': {
        'dataRange': [-1000, 1000],
        'opacityRange': [-1661.5882352941176, 2449.5490196078435]
    },
    'colorMap': CUSTOM_COLORMAP.get('BLACK_TO_WHITE')   
}

