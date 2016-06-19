""" Dynamically illustrates color palette user selected GIF image"""


from PIL import Image, ImageDraw
from Subdivide import subdivide
from Average import average
import math


imName = raw_input('Enter Image Name ')
im = Image.open(imName)
base = im.size

subs, subsVAL = subdivide(im)

subdivisions = []
for sub in subs:
    subdivisions.append(average(sub))


# # Alan Zucconi Lumonosity Color Sort
# # Sort subdivisions based on luminosity
# def lum(r, g, b):
    # return math.sqrt((.241 * r) + (.691 * g) + (.068 * b))

# Liszt 'List' Louis brightness sort method
# rgb = []
# for k in subdivisions:
    # r, g, b = tmp[25, 25]
    # rgb.append(r + g + b)
# rgb.sort()

nIM = Image.new('RGBA', base, color=(0, 0, 0, 0))
draw = ImageDraw.Draw(nIM)

for k in range(len(subs)):
    draw.rectangle(xy=subsVAL[k], fill=subdivisions[k])

nIM.show()
