from PIL import Image
from numpy import linspace

#Returns a list of the 4 colors
#Precond - A list of color tuples,
#Postcond- A list of 4 color tuples that range from darkest to lightest
def selection(colorlist):
    #create a list with only the tuples we wish to pull from
    slist = linspace(0, len(colorlist), 10)

    #pull the middle 8 values of the previous list
    xlist = slist[1:9]
    return xlist

#DRIVER PROGRAM// TO BE REMOVED LATER
somelist = range(100)

somelist = selection(somelist)
print somelist
