import numpy as np
key = np.array([1,2,3,4,5,6,7,8])
print("slicing")
print(key[1:3])
print(key[::2])
print(key[0] + key[2])
print("Hello Africa")
tool = np.array([[2,5,7,8],[3,8,5,2]])
print(tool[1][3])
# so the first index specific the matric then the second matrix is for the index of value
print(tool[0] + tool[1])
print("Above is sum")
print(tool[0] * tool[1])
print("slicing")
print(tool[0,   1:3])
print(tool[0:2, 2])#here it will output the second index number from each single matrix
print(">",tool[0:2, 1:3])
print("hello")
weapon = np.array([[[2,4,6,1,],[7,3,5,2]],[[2,5,2,8],[9,3,3,2]]])
print(weapon[0] + weapon[1])
print(weapon[0][1][0])