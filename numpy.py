import numpy as np
arr = np.array([[1 , 2], [3 , 4], [5 , 6], [7 , 8], [9 , 10], [11 , 12]])
print(arr)
newarr = np.array_split(arr , 3)
print(newarr)
print("first = \n", newarr[0])
print("second = \n", newarr[1])
print("third = \n", newarr[3])
