import cv2, numpy
from colorDistance  import colorDistance
from convertColor import bgraTOhex, hexTObgra

# import image
image = cv2.imread('./test_data/mesmall.png', -1)
image = numpy.array(image).tolist()

p1 = cv2.imread('./test_data/pall.png', -1)
p1 = numpy.array(p1).tolist()

#get color palette
colors = set()
colors.add('000000')
for ri, row in enumerate(p1):
    for ci, col in enumerate(row):
        color = bgraTOhex(col)
        colors.add(color)

def findMatch(color, palette):
    shortest = 999999
    match = ''
    for c in palette:
        distance = colorDistance(hexTObgra(color), hexTObgra(c))
        if distance < shortest:
            shortest = distance
            match = c
    return match

def convertImage(image, palette):
    for ri, row in enumerate(image):
        print(f'row: {ri} - {int(ri/len(image)*100)}%')
        for ci, col in enumerate(row):
            if col[3] == 255:
                color = bgraTOhex(col)
                color = findMatch(color, palette)
                image[ri][ci] = hexTObgra(color)
            else:
                image[ri][ci][3] = 0
    return image

image = convertImage(image, colors)

# result=cv2.imwrite(r'result.png', image)
result = cv2.imwrite(r"menes.png", numpy.asarray(image))
print(result)

# test = colorDistance(color1, color2)