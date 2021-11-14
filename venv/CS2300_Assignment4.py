#Nicholas Hay
#CS2300
#Assignment 4
print("This is Assignment 4 for CS2300")
print("This is my first python program")
#importing packages
import numpy as np #importing numpy
from numpy import genfromtxt
import csv
import math

#defining file reader. will read lines as rows of a matrix
def reader(Input):
    matrixData = np.genfromtxt(Input,skip_header=0)
    return matrixData

#used some input code from Dr. Hanratty's coding assignment
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

eyeLocationList = [inputData[0][0], inputData[0][1], inputData[0][2]]
eyeLocation = np.array(eyeLocationList) #eyeLocation object

#light direction value setting
lightDirectionList = [inputData[0][3], inputData[0][4], inputData[0][5]]
lightDirection = np.array(lightDirectionList) #lightDirection object

#getting coordinates
pList = [inputData[1][0], inputData[1][1], inputData[1][2]]
qList = [inputData[1][3], inputData[1][4], inputData[1][5]]
rList = [inputData[1][6], inputData[1][7], inputData[1][8]]
#points
p = np.array(pList)
q = np.array(qList)
r = np.array(rList)
eyeLocation = np.array(eyeLocationList) #eyeLocation object
#find certeroid
c = [(p[0] + q[0] + r[0])/3, (p[1] + q[1] + r[1])/3, (p[2] + q[2] + r[2])/3]
centeroid = np.array(c)
print('centeroid: ')
print(centeroid)
#normalizing
normal = eyeLocation - centeroid
x = pow(normal,2)
sum = x[0]+x[1]+x[2]
normalized = math.sqrt(sum)
#view vector
viewVector = (eyeLocation - centeroid) / normalized
#vector normal
u = q - p
w = r - p
    #cross product
cross = [u[1]*w[2] - w[1]*u[2], u[2]*w[0] - w[2]*u[0], u[0]*w[1]-w[0]*u[1]]
crossProduct = np.array(cross)
x = pow(crossProduct,2)
sum = x[0]+x[1]+x[2]
xNormalized = math.sqrt(sum)
#finding n
n = (crossProduct)/xNormalized
#computing the culling output
dotVandN = (viewVector[0]*n[0] + viewVector[1]*n[1] + viewVector[2]*n[2])
#performing culling operation
cull = 2
if dotVandN < 0:
    cull = 0
else:
    cull = 1
print("culling result: ", cull)
print("---------------------------------")
print("centeroid: " , centeroid)
print("view vector: ", viewVector)
print("Vector normal: ", n)


#part B - projection
#getting points
qList = [inputData[0][0], inputData[0][1], inputData[0][2]]
q = np.array(qList)
nList = [inputData[0][3], inputData[0][4], inputData[0][5]]
n = np.array(nList)
vList = [inputData[0][6], inputData[0][7], inputData[0][8]]
v = np.array(vList)
#points (x)
x1List = [inputData[1][0], inputData[1][1], inputData[1][2]]
x2List = [inputData[1][3], inputData[1][4], inputData[1][5]]
x3List = [inputData[1][6], inputData[1][7], inputData[1][8]]
x4List = [inputData[2][0], inputData[2][1], inputData[2][2]]
x5List = [inputData[2][3], inputData[2][4], inputData[2][5]]
x6List = [inputData[2][6], inputData[2][7], inputData[2][8]]
x7List = [inputData[3][0], inputData[3][1], inputData[3][2]]
x8List = [inputData[3][3], inputData[3][4], inputData[3][5]]
x9List = [inputData[3][6], inputData[3][7], inputData[3][8]]
x1 = np.array(x1List)
x2 = np.array(x2List)
x3 = np.array(x3List)
x4 = np.array(x4List)
x5 = np.array(x5List)
x6 = np.array(x6List)
x7 = np.array(x7List)
x8 = np.array(x8List)
x9 = np.array(x9List)
xArray = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
#parallel projection

#learning python, could not get arrays to work. Had to code like this.
print("projecting each point")
temp = q - x1
temp2 = v * n
projX1 = x1 + ((temp*n) / temp2)*v
print("x1: ", projX1)


temp = q - x2
temp2 = v * n
projX2 = x2 + ((temp*n) / temp2)*v
print("x2: ", projX2)

temp = q - x3
temp2 = v * n
projX3 = x3 + ((temp*n) / temp2)*v
print("x3: ", projX3)

temp = q - x4
temp2 = v * n
projX4 = x4 + ((temp*n) / temp2)*v
print("x4: ", projX4)

temp = q - x5
temp2 = v * n
projX5 = x5 + ((temp*n) / temp2)*v
print("x5: ", projX5)








