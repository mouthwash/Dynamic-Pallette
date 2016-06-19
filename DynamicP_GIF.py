""" Dynamically illustrates color palette user selected GIF image"""


from PIL import Image, ImageDraw
from Subdivide import subdivide
from Average import average
from Selection import selection
from images2gif import writeGif
from loadgif import loadgif
import math
import os

def main():
    """"""

    imName = raw_input('Enter GIF file ')
    tmpIm = Image.open(imName)

    # calculate number of frames in GIF to show render progress
    frameNum = 0
    currentFrame = 0
    try:
        while True:
            tmpIm.seek(tmpIm.tell() + 1)
            frameNum += 1
    except EOFError:
        pass

    loadgif(imName)

    currentdir = os.getcwd()
    imFolder = os.listdir(currentdir + '/imFolder')

    def numKeySort(fileName):
        key_img_rem  = fileName[3:]
        key_png_rem = key_img_rem[:len(key_img_rem) - 4]
        key_png_rem = int(key_png_rem)
        return key_png_rem

    imFolder.sort(key=numKeySort)
    print imFolder

    for file in imFolder:
        imPaletteSave(os.getcwd() + '/imFolder/' + file, currentFrame)
        currentFrame += 1
        print str(currentFrame) + '/' + str(frameNum)

def imPaletteSave(imName, num):
    im = Image.open(imName)
    base = im.size
    im = im.convert('RGB')

    subs, subsVAL = subdivide(im)

    subdivisions = []
    for sub in subs:
        subdivisions.append(average(sub))

    subSorted = list(subdivisions)
    # Alan Zucconi Lumonosity Color Sort
    # Sort subdivisions based on luminosity
    def lum(r, g, b):
        return math.sqrt((.241 * r) + (.691 * g) + (.068 * b))
    subSorted.sort(key=lambda rgb: lum(*rgb))

    colSelect = selection(subSorted)

    x, y = base
    a = x / 8
    b = y / 8

    nIM = Image.new('RGBA', (x + (2 * a), y + (b * 3)), color=(246, 240, 236, 0))
    nIM.paste(im, (a, b, a + x, b + y))

    draw = ImageDraw.Draw(nIM)

    x0 = a
    y0 = y + a
    y1 = y0 + a
    iter = x / len(colSelect)

    for k in range(len(colSelect)):
        draw.rectangle([x0, y0, x0 + iter, y1], colSelect[k])
        x0 += iter

    del draw
    nIM.save(os.getcwd() + '/palFolder/img' + str(num) + '.png', 'PNG')


if __name__ == '__main__':
    main()
