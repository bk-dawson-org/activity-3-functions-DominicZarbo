import math

radiusBottom = float(input("What is the radius of a layer of the bottom tier "))
heightBottom = float(input("What is the height of a layer of the bottom tier "))
radiusTop = float(input("What is the radius of a layer of the top tier "))
heightTop = float(input("What is the height of a layer of the top tier "))
numberOfLayers = 3
def cakeVolume(radiusBottom, heightBottom, radiusTop, heightTop, numberOfLayers) :   
    volumeBottom = round(((math.pi) * (radiusBottom ** 2) * (heightBottom)) * (numberOfLayers), 2)
    volumeTop = round(((math.pi) * (radiusTop ** 2) * (heightTop)) * (numberOfLayers), 2)
    volumeTotal = volumeBottom + volumeTop
    return volumeTotal
volumeTotal = str(cakeVolume(radiusBottom, heightBottom, radiusTop, heightTop, numberOfLayers))
print("The volume of the cake is " + volumeTotal)

sliceVolume = int(input("What is the desired volume of a slice of cake "))
totalVolume = int(cakeVolume(radiusBottom, heightBottom, radiusTop, heightTop, numberOfLayers))
def cakeSlice(slicevolume) :
    numberOfSlices= int((totalVolume)/(sliceVolume))
    return numberOfSlices
numberOfSlices = str(cakeSlice(sliceVolume))
print("The number of slices to cut is " + numberOfSlices)