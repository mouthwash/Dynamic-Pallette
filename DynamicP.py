""" Dynamically illustrates color palette user selected GIF image"""


from PIL import Image, ImageDraw
from Subdivide import subdivide
from Average import average
from Selection import selection
import math

def main():
    """"""

    imName = raw_input('Enter Image Name ')
    im = Image.open(imName)
    base = im.size

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
    nIM.show()


if __name__ == '__main__':
    main()
