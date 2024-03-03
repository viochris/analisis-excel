from array import array
from numpy import average

x = array("i",[1, 2, 3, 4, 5])
print(x)
print(type(x))

# import array
# x = array.array("i",[1, 2, 3, 4, 5])
# print(x)
# print(type(x))

var_arr = [0 for i in range(10)]
print(var_arr)

for i in range(10):
    var_arr[i] = i
print(var_arr)

var_arr = []
for i in range(10):
    var_arr.append(i)
print(var_arr)


var_arr = [1, 2, 3, 4, 5]
for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")
    
    
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]
for i in range(1, len(var_arr)):
    # print(i) from 1 to 4
    right_pointer = var_arr[i]
    if left_pointer < right_pointer:
        left_pointer = right_pointer
print(left_pointer)


var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]
for i in range(len(var_arr)):
    # print(i) from 0 to 4
    right_pointer = var_arr[i]
    if left_pointer < right_pointer:
        left_pointer = right_pointer
print(left_pointer)

var_array = [i for i in range(101)]
print(average(var_array))