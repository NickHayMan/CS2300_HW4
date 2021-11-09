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

numArrayInput = np.empty(18)
numArrayInput.fill(0)
#Laoyout for how KNum input works
#numKArrayInput = np.array([NumK1, NumK2, NumK3, NumK4, NumK5, NumK6, NumK7, NumK8, NumK9])
numKArrayInput = np.empty(9)
numKArrayInput.fill(0)
print(numArrayInput)
print(numKArrayInput)

#creating objects
#part A simple shading
#eye location value setting
eyeLocation = [numArrayInput[0], numArrayInput[1], numArrayInput[2]]

#light direction value setting
lightDirection = [numArrayInput[3], numArrayInput[4], numKArrayInput[5]]

#getting coordinates
p = [numArrayInput[9], numArrayInput[10], numArrayInput[11]]
q = [numArrayInput[12], numArrayInput[13], numArrayInput[14]]
r = [numArrayInput[15], numArrayInput[16], numArrayInput[17]]

#performing culling operation
backOrForward = 2
directionN = 0
center = 0
vertexV = (eyeLocation - center) #/||eyeLocation -center||
if directionN * vertexV < 0:
    backOrForward = 1
elif directionN * vertexV > 0:
    backOrForward = 0






