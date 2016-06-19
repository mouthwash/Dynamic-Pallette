from PIL import Image,GifImagePlugin
import sys
import os

#Will load a GIF into its frames as a list of image files
#Precond- accepts a name of a gif image
#Postcond - will create a png file for each frame inside the gif
def loadgif(giffile):
    try:
        im = Image.open(giffile)

    except IOError:
        print "Load failed for" , giffile
        sys.exit(1)

    xnum = 0
    try:
        while True:
            im.seek(im.tell() + 1)
            xnum += 1

    except EOFError:
        pass

    im.seek(0)
    num = 0
    try:
        while True:
            newim = Image.new('RGBA', im.size)
            newim.paste(im)
            newim.save(os.getcwd() + '/imFolder/img' + str(num) + '.png' , 'PNG')
            num += 1
            print str(num) + '/' + str(xnum)
            im.seek(im.tell() + 1)

    except EOFError:
        pass
