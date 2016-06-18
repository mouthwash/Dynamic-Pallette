""" Dynamically illustrates color palette user selected GIF image"""


from PIL import Image
from Subdivide import subdivide
from Average import average
import math

imName = raw_input('Enter Image Name')
im = Image.open(imName)

subdivisions = subdivide(im)

for sub in subdivisions:
    average(sub)

subCopy = list(subdivisions)

# Alan Zucconi Lumonosity Color Sort
# Sort subdivisions based on luminosity
def lum(r, g, b):
    return math.sqrt((.241 * r) + (.691 * g) + (.068 * b))

# 'List' Louis brightness sort method
rgb = []
for k in subCopy:
    tmp = k.load()
    r, g, b = tmp[25, 25]
    rgb.append(r + g + b)
rgb.sort()

nIM = Image.new()
x0 = 0
y0 = 0  # unchanging
x1 = 20
y1 = 10  # unchanging

for k in len(rgb):
    x0 += 10
    y0 += 10
    nIM.rectangle([x0, y0, x1, y1], fill=subCopy[k])
