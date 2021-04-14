import cv2, numpy
from resize import resize

def getImage(path):
    image = cv2.imread(path, -1)
    image = numpy.array(image).tolist()
    return image

def image_manipulation(args):
    valid_commands = set(
        ['-w', '--width',
        '-h', '--height',
        '-r', '--resize',
        '-c', '--color'])

    image = getImage(args[0])
    if not image:
        print(f'No image found with name {args[0]}')
        return
    
    #settings
    new_height = None
    new_width = None
    recolor = None
    command = None
    error = None

    index = 0
    while index < len(args):
        if args[index] in valid_commands: command = args[index]
        if command == '-w' or command == '--width':
            if len(args) < index+2:
                error = 'Missing arguments'
                break
            try: new_width = int(args[index+1])
            except: error = 'Not a valid input'
            index += 1
        if command == '-h' or command == '--height':
            if len(args) < index+2:
                error = 'Missing arguments'
                break
            try: new_width = int(args[index+1])
            except: error = 'Not a valid input'
            index += 1
        if command == '-r' or command == '--resize':
            if len(args) < index+3:
                error = 'Missing arguments'
                break
            try:
                new_height = int(args[index+1])
                new_width = int(args[index+2])
            except: error = 'Not a valid input'
            index += 2
        if command == '-c' or command == '--recolor':
            if len(args) < index+2:
                error = 'Missing arguments'
                break
            try: recolor = min(int(args[index+1]),8)
            except:
                if args[index+1] == 'all': recolor = 8
                else: error = 'Not a valid input'
            index += 1
        index += 1
        if error: break

    if error: print(f'Error: {error}')
    print(f'settings: command {command} nh {new_height} nw {new_width} recolor {recolor}')