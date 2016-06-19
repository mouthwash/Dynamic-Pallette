from PIL import Image
from numpy import linspace

#Returns a list of the 8 colors
#Precond - A list of color tuples,
#Postcond- A list of 8 color tuples that range from darkest to lightest
def selection(colorlist):
    #create a list with only the tuples we wish to pull from
    slist = []
    interval = len(colorlist) / 8
    for num in range(len(colorlist)):
        if num % interval == 0:
            slist.append(colorlist[num])

    #pull the middle 8 values of the previous list
    xlist = slist[1:9]
    return xlist

#DRIVER PROGRAM// TO BE REMOVED LATER
#somelist = range(100)

#somelist = selection(somelist)
#print somelist
