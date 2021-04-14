import sys
sys.path.insert(1, './image_manipulation')
from image import image_manipulation

args = sys.argv[1:]
if args[0] == 'image':
    image_manipulation(args[1:])
else:
    print('command not recgonized')