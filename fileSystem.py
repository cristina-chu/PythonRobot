#Cristina Chu
#cchu43@gatech.edu
#"I worked on the homework assignment alone, using only this semester's course materials."

#Part 1
from myro import *
#init()

from random import randrange

def avgObstacleValues(aNum):
    right = []
    center = []
    left = []
    count = 0
    
    while timeRemaining(aNum):
        l,c,r = getObstacle()
        left.append(l)
        center.append(c)
        right.append(r)
        count = count +1

        turnLeft(1,randrange(2))

    rightValue = (reduce(lambda x,y:x+y,right))/float(len(right))
    centerValue = (reduce(lambda x,y:x+y,center))/float(len(center))
    leftValue = (reduce(lambda x,y:x+y,left))/float(len(left))
    
    myTuple = (leftValue, centerValue, rightValue)

    return myTuple


#Part 2

from math import sqrt

def findDistances(filenameIn, filenameOut):
    fIn = open(filenameIn,'r')
    fOut = open(filenameOut, 'w')

    points = []
    distances = []
    lines = fIn.readlines()
    fIn.close()
    
    for line in lines:
        if line != '\n':
            values = line.split()
            points.append(values)
    
    distances = map(lambda x: sqrt((int(x[0])-int(x[2]))**2 + (int(x[1])-int(x[3]))**2), points)

    for distance in distances:
        fOut.write(str(distance)+'\n')
        fOut.write('\n')

    fOut.close()

    
#Part 3

from os import listdir

def findImages(path):
    files = listdir(path)

    aList = []

    for name in files:
        if name[-4:]=='.jpg' or name[-4:]=='.gif' or name[-4:]=='.bmp' or name[-4:]=='.png':
            aList.append(name)
        if name[-4:]=='.JPG' or name[-4:]=='.GIF' or name[-4:]=='.BMP' or name[-4:]=='.PNG':
            aList.append(name)
    return aList


#Part 4

from os import path

def generateFileSystemDictionary(path):
    dictionary = {}
    files = listdir(path)
    paths = [(path,files)]
    
    for name in files:
        if name.find('.')==-1:
            newPath = '%s'%path+'/%s'%name
            myTup = newPath,listdir(newPath)
            paths.append(myTup)
            generateFileSystemDictionary(newPath)

    for tups in paths:
        dictionary[tups[0]]=tups[1]

    return dictionary         
            
