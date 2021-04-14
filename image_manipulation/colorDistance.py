import math

#an approximation
def colorDistance(c1, c2):
    rmean = (c1[0]+c2[0])/2
    r = c1[0] - c2[0]
    g = c1[1] - c2[1]
    b = c1[2] - c2[2]
    red = int((512+rmean)*r*r) >> 8
    green = 4*g*g
    blue = int((767-rmean)*b*b) >> 8

    return math.sqrt(red + green + blue)