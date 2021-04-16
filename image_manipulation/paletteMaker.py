import cv2, numpy, math
# from colorDistance  import colorDistance
from convertColor import bgraTOhex, hexTObgra

def createPalette(image, createImage=False):
    #get color palette
    colors = set()
    # colors.add('000000')
    for row in image:
        for col in row:
            color = bgraTOhex(col)
            colors.add(color)
    colors = list(colors)

    #create image for palette
    if createImage:
        arr_size = math.ceil(math.sqrt(len(colors)))
        palette = list()
        filler = hexTObgra(colors[-1])
        for _ in range(arr_size):
            row = list()
            for _ in range(arr_size):
                if len(colors):
                    color = hexTObgra(colors.pop())
                    row.append(color)
                else: row.append(filler)
            palette.append(row)
        palette = numpy.asarray(palette)
        result = cv2.imwrite(r"palette.png", numpy.asarray(palette))
        if result: print('Palette Created')

    return colors