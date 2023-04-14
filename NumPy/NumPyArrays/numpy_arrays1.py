import numpy as np


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
my_list = [1, 2, 3]
my_array = np.array(my_list)
print(my_list)
print(my_array)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



print()



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
my_matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_matrix_array = np.array(my_matrix_list)
print(my_matrix_list)
print(my_matrix_array)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



print()



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating an array using 'arange' function
np_arange_array = np.arange(0, 10, 2)
print(np_arange_array)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



print()



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating an array that includes of all zeros using `zeros` (or 'ones' for all ones) function
np_zeroes_array = np.zeros(10)
print(np_zeroes_array)

# We can also create 2-D matrix of all zeroes by passing in a tuple to 'zeroes' (or 'ones' for all ones) function as '(<no. of rows>, <no. of columns>)'
np_ones_matrix_array = np.ones((2, 3))
print(np_ones_matrix_array)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



print()



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# We can use np.linspace(start_value, end_value, how_many_evenly_spaced_points) to return a 1-D vector of evenly spaced numbers
np_evenly_spaced_numbers = np.linspace(0, 5, 10)
print(np_evenly_spaced_numbers)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



print()



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating an identity matrix using NumPy
# Identity matrices are useful when dealing with linear algebra problems, which is basically a 2-D square matrix which has a diagonal of ones and everything else in the matrix is zeroes
np_identity_matrix = np.eye(4)
print(np_identity_matrix)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



print()



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# NumPy has a lot of ways to create random number arrays

# np.random.rand(number_of_values) will generate a random vector of numbers
np_random_array = np.random.rand(5)
print(np_random_array)

print()

# We can also use np.random.rand(number_of_rows, number_of_columns) to create a random 2-D matrix
np_random_matrix = np.random.rand(5, 5)
print(np_random_matrix)

print()

# We use np.random.randn(number_of_values) to generate a random numbers array based on standard distribution (or Gaussian Distribution) instead of a uniform distribution which is between 0 to 1, which we get by using np.random.rand(number_of_values)
np_random_standard_distribution_array = np.random.randn(5)
print(np_random_standard_distribution_array)

print()

# We can also use np.random.randn(number_of_rows, number_of_columns) to create a 2-D matrix
np_random_standard_distribution_matrix = np.random.randn(4, 4)
print(np_random_standard_distribution_matrix)

print()

# We use np.random.randint(low_value, high_value, number_of_values) to get a random integers array
np_random_integers_array = np.random.randint(0, 100, 10)
print(np_random_integers_array)

print()

# We can use the arr.reshape(no. of rows, no. of columns) method, which will return the same data but rearranged into a new shape(dimensions)
arr = np.arange(25)
print(arr.shape)        # This will return us the shape of the array, whether its 1D or 2D basically this kind of info about the array
random_arr = np.random.randint(0, 50, 10)
x = arr.reshape(5, 5)       # Here we are reshaping 1D 'arr' into a 5x5 matrix
print(x, x.shape)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



print()



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# To know what kind of datatype is being used in an array, we can use the arr.dtype attribute to know so
arr_1 = np.arange(10)
print(arr_1.dtype)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------