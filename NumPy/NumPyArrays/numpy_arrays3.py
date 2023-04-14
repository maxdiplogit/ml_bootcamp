import numpy as np


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
arr = np.arange(0, 11)
print(arr)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



print()



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# If we want to add, subtract, multiply, divide and to-the-power elements from two arrays element by element, python provides us a way to do so as follows
print('ADD: ', arr + arr)
print('ADD 100 to each element in array: ', arr + 100)
print()
print('SUBTRACT: ', arr - arr)
print('SUBTRACT 100 from each element in array: ', arr - 100)
print()
print('MULTIPLY 100 to each element in array: ', arr * 100)
print('MULTIPLY: ', arr * arr)
print()
print('DIVIDE: ', arr / arr)
print('DIVIDE 100 to each element in array: ', arr / 100)
print()
print('SQUARED: ', arr ** arr)
print('SQUARED BY 2 : ', arr ** 2)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



print()



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Some useful methods in numpy
print(np.sqrt(arr))
print()
print(np.exp(arr))
print()
print(arr.max())
print()
print(np.sin(arr))
print()
print(np.log(arr))
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------