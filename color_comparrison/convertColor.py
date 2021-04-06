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