from PIL import Image,GifImagePlugin

#Will load a GIF into its frames as a list of image files
#Precond- accepts a gif image object
#Postcond - will return a list of image objects with the frames of the gif in it
def loadgif(gif):
    #create empty gif list
    giflist = []
    num = 0
    #Begin to seek frames and dump them into a
    #list of images till failure
    while not EOFError:
        temp = gif
        temp = temp.convert('RGB')
        giflist.append(temp)
        num = gif.tell() +1

    return giflist

#DRIVER PROGRAM TO BE REMOVED LATER
gif = Image.open('day.gif')
somelist = loadgif(gif)
somelist[0].show()
