""" Subdivide a Pillow Image object"""

from PIL import Image


def subdivide(image):
    """ Subdivide an image object based on its resolution
        Returns a list of region objects
    """

    # tuple holding image size
    x, y = image.size

    # Estimate how many subdivisions to use
    x_SubE = x / 8
    y_SubE = y / 8

    # Create number of subdivisions being used
    x_Sub = x / x_SubE
    y_Sub = y / y_SubE

    # Create 2 lists holding x and y values for points at
    # subdivisions
    x_Splits = [0]
    y_Splits = [0]

    for k in range(1, x_SubE):
        x_Splits.append(x_Splits[k - 1] + x_Sub)

    for k in range(1, y_SubE):
        y_Splits.append(y_Splits[k - 1] + y_Sub)

    subdivisions = []

    for kx in range(len(x_Splits) - 1):
        for ky in range(len(y_Splits) - 1):
            # x-values
            xUL = 0 + x_Splits[kx]
            xLR = xUL + (x_Splits[1] - x_Splits[0])
            # y - values
            yUL = 0 + y_Splits[ky]
            yLR = yUL + (y_Splits[ky + 1] - y_Splits[ky])

            sub = (xUL, yUL, xLR, yLR)
            subdivisions.append(image.crop(sub))

    print subdivisions


if __name__ == '__main__':
    im = Image.open('temp.jpg')
    subdivide(im)
