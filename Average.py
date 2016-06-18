from PIL import Image

#Function that will average Image objects.
#Precond - Accepts an image subsection
#Postcond - will output the average color of the image subsection
def average(image):
    #Create a color list
    colorlist = []
    length, width = image.size
    pixel = image.load()
    #Go through the image size in a nested for loop
    for num in range(length):
        for xnum in range(width):
            r,g,b = pixel[num,xnum]
            color = [r,g,b]
            colorlist.append(color)

    #Create color variables to store added color values
    red = 0
    green = 0
    blue = 0

    #Iterate through the color list to find the average rgb value
    #And store those values into color variables
    for color in colorlist:
        red += color[0]
        green += color[1]
        blue += color[2]

    #Average value evaluations
    red = red/(length * width)
    green = green/(length * width)
    blue = blue/(length * width)

    average = [red,green,blue]
    return average
