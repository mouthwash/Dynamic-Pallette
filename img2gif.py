from PIL import Image
from images2gif import writeGif

def img2gif(filename,images):
    writeGif(filename,images, duration = 0.1)
