import cv2, numpy
from colorDistance  import colorDistance
from convertColor import bgraTOhex, hexTObgra

# import image
image = cv2.imread('./test_data/shipwright.png', -1)
image = numpy.array(image).tolist()

def getColors(pnum):
    palette = cv2.imread(f'./image_manipulation/palettes/p{pnum}.png', -1)
    palette = numpy.array(palette).tolist()

    colors = set()
    for row in palette:
        for col in row:
            color = bgraTOhex(col)
            colors.add(color)
    return colors

def findMatch(color, palette):
    shortest = 999999
    match = ''
    for c in palette:
        distance = colorDistance(hexTObgra(color), hexTObgra(c))
        if distance < shortest:
            shortest = distance
            match = c
    return match

def recolor(image, palette):
    palette = getColors(palette)
    print('')
    for ri, row in enumerate(image):
        print ("\033[A                             \033[A")
        print(f'recoloring image: {int(ri/len(image)*100)}%')
        for ci, col in enumerate(row):
            if col[3] == 255:
                color = bgraTOhex(col)
                color = findMatch(color, palette)
                image[ri][ci] = hexTObgra(color)
            else:
                image[ri][ci][3] = 0
    print ("\033[A                             \033[A")
    print(f'recoloring image: 100% --- DONE')
    return image