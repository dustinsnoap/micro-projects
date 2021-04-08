from convertColor import bgraTOhex

def getColors(image):
    colors = set()
    for row in image:
        for col in row:
            color = bgraTOhex(col)
            colors.add(color)
    return colors