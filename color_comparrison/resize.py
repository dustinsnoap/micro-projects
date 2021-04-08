import cv2, numpy
from convertColor import bgrTOrgb, rgbTOlab, labTOrgb
from imageInfo import getColors

# import image
image = cv2.imread('./test_data/avatar.png', -1)
image = numpy.array(image).tolist()

# helper functions
def getSubSectionArray(arr, x_start, y_start, x_end, y_end):
    newarr = list()
    for row in arr[y_start:y_end]:
        newarr.append(row[x_start:x_end])
    return newarr

def getColorAverage(arr, weights=[1,1,1,1,1], restrictColor=True):
    #weights = [middle, top, right, bottom, left]
    l = 0
    a = 0
    b = 0
    counter = 0
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
        current_x = 0
        while current_x < old_width:
            current_x += ss_width
        current_y += ss_height

getColorAverage(image)