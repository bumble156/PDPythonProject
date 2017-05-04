# This code was adapted from the work of Sim Reaney and Andy Evans
# Source: http://www.geog.leeds.ac.uk/courses/other/programming/info/code/modelling/calibration/MonteCarlo.java

from numpy import genfromtxt
import random

maxNum = 0
minNum = 0
interval = 0
numberOfBins = 20
bins = [[0.0 for x in range(numberOfBins)] for y in range(2)]

def setNumbers(filename):
    data = fileAsArray(filename)
    
    i = 0
    while (i < numberOfBins):
        bins[0][i] = interval + (interval * (i) + minNum)

        j = 0
        while (j < len(data)):
            if data[j] < bins[0][i]:
                bins[1][i] = bins[1][i] + 1
                
            j = j + 1
            
        bins[1][i] = bins[1][i] / len(data)
        #print str(bins[0][i])+ " \t\t" + str(bins[1][i])
        i = i + 1

def getNumber(random):
    value = 0.0
    i = 0
    
    while (i < numberOfBins):
        if random < bins[1][i]:
            value = bins[0][i]
            break
        
        i = i + 1

    return value

def fileAsArray(filename):
    data2d = genfromtxt(filename, delimiter=',')
    
    position = 0
    data = []
    global minNum
    global maxNum
    
    for line in data2d:
        for value in line:
            data.append(value)
            if position == 0:
                maxNum = value
                minNum = value
                
            if value > maxNum:
                maxNum = value
                
            if value < minNum:
                minNum = value
                
            position = position + 1

    global interval
    interval = float(maxNum - minNum)/numberOfBins

    return data

setNumbers('testData.txt')
print getNumber(random.uniform(0,1))
#print getNumber(0.35)
