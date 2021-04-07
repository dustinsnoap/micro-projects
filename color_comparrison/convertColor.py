def bgraTOhex(bgraColor):
    r = str(hex(bgraColor[2]).split('x')[-1])
    if len(r) == 1: r = '0'+r
    g = str(hex(bgraColor[1]).split('x')[-1])
    if len(g) == 1: g = '0'+g
    b = str(hex(bgraColor[0]).split('x')[-1])
    if len(b) == 1: b = '0'+b
    return r+g+b

def hexTObgra(hex):
    bgra = [0]*4
    if hex == '000000': return bgra
    bgra[2] = int(hex[:2], 16)
    bgra[1] = int(hex[2:4], 16)
    bgra[0] = int(hex[4:], 16)
    bgra[3] = 255
    return bgra

def hexTOrgba(hex):
    rgba = [0]*4
    if hex == '000000': return rgba
    rgba[0] = int(hex[:2], 16)
    rgba[1] = int(hex[2:4], 16)
    rgba[2] = int(hex[4:], 16)
    rgba[3] = 255
    return rgba

def rgbTOlab(rgb):
    num = 0
    RGB = [0, 0, 0]

    for value in inputColor:
        value = float(value) / 255
        if value > 0.04045: value = ((value + 0.055) / 1.055) ** 2.4
        else: value = value / 12.92       
        RGB[num] = value*100
        num = num+1
    XYZ = [0, 0, 0]

    X = RGB[0]*0.4124 + RGB[1]*0.3576 + RGB[2]*0.1805
    Y = RGB[0]*0.2126 + RGB[1]*0.7152 + RGB[2]*0.0722
    Z = RGB[0]*0.0193 + RGB[1]*0.1192 + RGB[2]*0.9505
    XYZ[0] = round(X, 4)
    XYZ[1] = round(Y, 4)
    XYZ[2] = round(Z, 4)

    XYZ[0] = float(XYZ[0]) / 95.047
    XYZ[1] = float(XYZ[1]) / 100.0
    XYZ[2] = float(XYZ[2]) / 108.883

    num = 0
    for value in XYZ:
        if value > 0.008856:
            value = value ** (0.3333333333333333)
        else: value = (7.787*value) + (16/116)
        XYZ[num] = value
        num = num + 1
    Lab = [0, 0, 0]
    L = (116 * XYZ[1]) - 16
    a = 500 * (XYZ[0] - XYZ[1])
    b = 200 * (XYZ[1] - XYZ[2])
    Lab [0] = round(L, 4)
    Lab [1] = round(a, 4)
    Lab [2] = round(b, 4)

    return Lab