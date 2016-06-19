from PIL import Image,GifImagePlugin

#Will load a GIF into its frames as a list of image files
#Precond-
#Postcond
def loadgif(gif):
    gifx = Image.open('day.gif')
    gifx.show()

gif = 1
loadgif(gif)
