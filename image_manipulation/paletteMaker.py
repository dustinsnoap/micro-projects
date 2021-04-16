import cv2, numpy, math
# from colorDistance  import colorDistance
from convertColor import bgraTOhex, hexTObgra

def createPalette(image, createImage=False):
    #get color palette
    colors = set()
    # colors.add('000000')
    print('')
    for ri, row in enumerate(image):
        print ("\033[A                             \033[A")
        print(f'creating palette: {int(ri/len(image)*100)}%')
        for col in row:
            color = bgraTOhex(col)
            colors.add(color)
    colors = list(colors)
    print ("\033[A                             \033[A")
    print(f'creating palette: 100% --- DONE')

    #create image for palette
    if createImage:
        print('')
        arr_size = math.ceil(math.sqrt(len(colors)))
        palette = list()
        filler = hexTObgra(colors[-1])
        for ri in range(arr_size):
            print ("\033[A                             \033[A")
            print(f'creating palette image: {int(ri/arr_size*100)}%')
            row = list()
            for _ in range(arr_size):
                if len(colors):
                    color = hexTObgra(colors.pop())
                    row.append(color)
                else: row.append(filler)
            palette.append(row)
        palette = numpy.asarray(palette)
        cv2.imwrite(r"palette.png", numpy.asarray(palette))
        print ("\033[A                             \033[A")
        print(f'creating palette image: 100% --- DONE')

    return colors