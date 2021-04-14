import cv2, numpy, math
from convertColor import bgrTOrgb, rgbTObgr, rgbTOlab, labTOrgb
from imageInfo import getColors
from colorDistance import colorDistance

# import image
image = cv2.imread('./test_data/p1.jpg', -1)
image = numpy.array(image).tolist()

# helper functions
def getSubSectionArray(arr, x_start, y_start, x_end, y_end):
    newarr = list()
    for row in arr[y_start:y_end]:
        newarr.append(row[x_start:x_end])
    return newarr

def getColorAverage(arr, weights=[1,1,1,1,1], matchColor=True):
    #weights = [middle, top, right, bottom, left]
    l = 0
    a = 0
    b = 0
    counter = 0
    colors = list()
    if matchColor: colors = getColors(arr, 'bgr', 'rgb')
    for ri, row in enumerate(arr):
        row_weight = weights[0]
        if ri == 0: row_weight = weights[1]
        if ri == len(arr): row_weight = weights[3]
        for ci, col in enumerate(row):
            weight = weights[0] * row_weight
            if ci == 0: weight = weights[4] * row_weight
            if ci == len(arr[0]): weights[2] * row_weight
            relevance = col[3]/255 if len(col) == 4 else 1
            rgb = bgrTOrgb(col)
            lab = rgbTOlab(rgb)
            l += relevance * lab[0] * weight
            a += relevance * lab[1] * weight
            b += relevance * lab[2] * weight
            counter += 1
    lab = [l/counter, a/counter, b/counter]
    rgb = labTOrgb(lab)
    if matchColor:
        closest_color = list()
        closest_distance = 99999
        for color in colors:
            distance = colorDistance(color, rgb)
            if distance < closest_distance:
                closest_color = color
                closest_distance = distance
        rgb = closest_color
    return rgb

#main function
def resize(image, new_height, new_width):
    #image sizing
    old_height = len(image)
    old_width = len(image[0])

    #subsection sizing
    ss_height = old_height / new_height
    ss_width = old_width / new_width

    current_x = 0
    current_y = 0

    new_image = list()

    while current_y < old_height:
        print(f'current: {int(current_y*100)/100} - {int(100*current_y/old_height)}%')
        new_row = list()
        current_x = 0
        while current_x < old_width:
            #slices
            xs = math.floor(current_x)
            xe = math.ceil(current_x + ss_width)
            ys = math.floor(current_y)
            ye = math.ceil(current_y+ss_height)
            #weights
            wn = 1 - (current_y - ys)
            we = 1 - (xe - current_x)
            ws = 1 - (ye - current_y)
            ww = 1 - (current_x - xs)
            weights = [1, wn, we, ws, ww]
            #fun stuff
            ssarr = getSubSectionArray(image, xs, ys, xe, ye)
            color = rgbTObgr(getColorAverage(ssarr, weights))
            new_row.append(color)
            current_x += ss_width
        new_image.append(new_row)
        current_y += ss_height
    return new_image