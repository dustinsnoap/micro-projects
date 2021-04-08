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

def bgrTOrgb(bgr):
    rgb = list()
    rgb.append(bgr[2])
    rgb.append(bgr[1])
    rgb.append(bgr[0])
    if len(bgr) == 4: rgb.append(bgr[3])
    return rgb


def rgbTOlab(rgb):
    rgb = rgb[:3]
    num = 0
    RGB = [0, 0, 0]

    for value in rgb:
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

def labTOrgb(lab):
    y = (lab[0]+16)/116
    x = lab[1]/500 + y
    z = y - lab[2]/200

    if y**3 > 0.008856: y = y**3
    else: y = (y-16 / 116) / 7.787
    if x**3 > 0.008856: x = x**3
    else: x = (x-16 / 116) / 7.787
    if z**3 > 0.008856: z = z**3
    else: z = (z-16 / 116) / 7.787

    x = (95.047 * x) / 100
    z = (108.883 * z) / 100

    r = x * 3.2406 + y * -1.5372 + z * -.4986
    g = x * -.9689 + y * 1.88758 + z * 0.0415
    b = x * .0557 + y * -.204 + z * 1.057

    if r > 0.0031308: r = 1.055 * r**(1/2.4) - 0.055
    else: r = r * 12.92
    if g > 0.0031308: g = 1.055 * g**(1/2.4) - 0.055
    else: g = g * 12.92
    if b > 0.0031308: b = 1.055 * b**(1/2.4) - 0.055
    else: b = b * 12.92

    return [int(r*255), int(g*255), int(b*255)]