from convertColor import *

def getColors(image, input='rgb', output='rgb'):
    colors = set()

    for row in image:
        for col in row:
            color = str()
            if input == 'rgb': color = bgraTOhex(col)
            if input == 'bgr': color = bgraTOhex(col)
            if input == 'lab': color = bgraTOhex(labTOrgb(col))
            colors.add(color)

    colors = list(colors)
    for ci, color in enumerate(colors):
        if output == 'rgb': colors[ci] = hexTOrgba(color)
        if output == 'bgr': colors[ci] = hexTObgra(color)
        if output == 'lab': colors[ci] = rgbTOlab(hexTOrgba(color))

    return colors