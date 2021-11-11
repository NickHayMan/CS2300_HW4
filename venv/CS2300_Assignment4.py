#Nicholas Hay
#CS2300
#Assignment 4
print("This is Assignment 4 for CS2300")
print("This is my first python program")
#importing packages
import numpy as np #importing numpy
from numpy import genfromtxt
import csv

#defining file reader. will read lines as rows of a matrix
def reader(Input):
    matrixData = np.genfromtxt(Input,skip_header=0)
    return matrixData


#input format
#Num11  Num12  Num13  Num14  Num15  Num16   Num17  Num18  Num19
#Num21  Num22  Num23  Num24  Num25  Num26   Num27  Num28  Num29
#...
#NumK1 NumK2 NumK3 NumK4 NumK5 Num K6 Num K7 NumK8 NumK9

#num array
#Layout of how the input works
#numArrayInput = np.array([Num11,  Num12,  Num13,  Num14, Num15, Num16, Num17, Num18, Num19,
#                          Num21,  Num22,  Num23,  Num24,  Num25, Num26, Num27, Num28, Num29])
print('Enter the name of the txt file you want to input: ')
fileName = input()
#fill data array from file
inputData = reader(fileName)
print(inputData)
#Layout for how KNum input works
#numKArrayInput = np.array([NumK1, NumK2, NumK3, NumK4, NumK5, NumK6, NumK7, NumK8, NumK9])


#creating objects
#part A simple shading
#eye location value setting

eyeLocationList = [inputData[0], inputData[1], inputData[2]]
eyeLocation = np.array(eyeLocationList) #eyeLocation object

#light direction value setting
lightDirectionList = [inputData[3], inputData[4], inputData[5]]
lightDirection = np.array(lightDirectionList) #lightDirection object

#getting coordinates
pList = [inputData[9], inputData[10], inputData[11]]
qList = [inputData[12], inputData[13], inputData[14]]
rList = [inputData[15], inputData[16], inputData[17]]
#triangle
p = np.array(pList)
q = np.array(qList)
r = np.array(rList)
#find certeroid
centeroid = (1/3)(p*q*r)
#performing culling operation
backOrForward = 2
vertexV = (eyeLocation - centeroid) / np.dot(eyeLocation - centeroid)
if lightDirection * vertexV < 0:
    backOrForward = 0
elif directionN * vertexV > 0:
    backOrForward = 1


#part B - projection




