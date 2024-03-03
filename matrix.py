import numpy as np
import sys

matriks = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]        
print(matriks)

matriks = np.array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])          
print(matriks)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate((a, b)))

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= np.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(sys.getsizeof(var_list))
print(len(var_list))
print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print()
print(var_array.size)
print(var_array.itemsize)
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)
print()

matriks = np.array([[0 for j in range(4)] for i in range(3)])
print(matriks)

for i in range(3):
    for j in range(4):
        matriks[i][j] = i*j
print(matriks)

var_mat = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]
print(var_mat[2][1])


matriks = np.array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])          
print(matriks*2)

print()
print('gabunging list')
var_mat = [[5, 0,2],
            [1, -2,3]]
print(np.array(var_mat))
def_mat = [[0 for j in range(3)] for i in range(2)]
print(np.array(def_mat))

for i in range(len(var_mat)):
    for j in range(len(var_mat[i])):
        def_mat[i][j] = var_mat[i][j]*2

print(np.array(def_mat))


print('gabunging list')
var_mat = [[5, 0],
            [1, -2],
            [2,4]]
print(np.array(var_mat))
def_mat = [[0 for j in range(2)] for i in range(3)]
print(np.array(def_mat))

for i in range(len(var_mat)):
    for j in range(len(var_mat[i])):
        def_mat[i][j] = var_mat[i][j]*2

print(np.array(def_mat))