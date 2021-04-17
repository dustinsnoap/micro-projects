# micro-projects
projects too small to make an entire repo for
 
# Image manipulation
You can resize, recolor, or create a palette of every color in the image.
 
Arguments
image: signifies that you want to manipulate an image
-w or --width: Takes 1 argument [width]. This command will resize your image proportionally to fit the width specified.
-h or --height: Takes 1 argument [height]. This command will resize your image proportionally to fit the height specified.
-r or --resize: Takes 2 arguments [height] and [width] ie. -r 24 24 will resize the image to 24 pixels by 24 pixels.
-c --recolor: Takes 1 argument [pallete-num]. Currently this is set up with two palettes based on the NES capabilities. 1 is the standard palette, 8 includes every color the NES was capable of. You can add your own by adding images or creating new palettes and adding them to the palette directory.
-p or --palette: Takes no arguments. This will create a new palette image based on your image.
 
ex. python3 main.py image test.png -p -r 24 24 -c 1
This will create a palette of the specified image, resize it to 24 by 24 pixels and recolor it to  stand NES colors.
 
To do so...
1. Put your image in the root folder.
2. Run the program using the commands above.
3. Look in the results directory for your new image.

Known Issues:
-Increasing the size of the image doesn't always work as expected.