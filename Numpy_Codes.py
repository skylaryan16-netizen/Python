# %%
import numpy as np

# %% [markdown]
#  Q1. Create the first numpy array of 1-D with values (1,2,3,0).
#  Create a second numpy array of 1-D with values (4,1,0,
#  6). Perform following simple arithmetic operations on
#  these two numpy arrays:
#  • Addition
#  • Subtraction
#  • Multiplication
#  • Division

# %%
#creating two 1 Dimension array
a1 = np.array([1,2,3,0])
a2 = np.array([4,1,0,6])

print("\nThe two arrays are:\n",a1,a2)

# %%
type(a1), type(a2)

# %%
print("\nAddition of given two arrays:\n",a1+a2)
print("\nSubtraction of given two arrays:\n",a1-a2)
print("\nMultiplication of given two arrays:\n",a1*a2)
print("\nDivision of given two arrays:\n",a1/a2)

# %% [markdown]
# Q2. Create the first numpy array of random integers
#  between 1-100 of 5 elements in 1-D. Create second
#  numpy array of 2-D for the same range of integers of
#  shape 4*5. Now perform following simple arithmetic
#  operations on these two numpy arrays:
#  • Addition
#  • Subtraction

# %%
#creating two arrays with random integers and different shapes
a1 = np.random.randint(1,101,5)
a2 = np.random.randint(1,101,(4,5))

print("The first array a1 is:\n",a1)
print("\nThe second array a2 is:\n",a2)

print("\nAddition of two arrays:\n",a1+a2)
print("\nSubtraction of given two arrays:\n",a1-a2)

# %% [markdown]
# Q3. Create a 3-D array of 27 random elements using random
#  function of shape 3*3*3. Now pull the following
#  elements using indexing/slicing
#  • Third column of second 2-D array
#  • First and third row of first 2-D array
#  • Intersection of first row and third column in
#  third 2-D aray

# %%
#creating a 3D array with 27 random elements of shape 3*3*3
a_3d = np.random.random((3,3,3))
a_3d

# %%
# Seperating elements of formed 3D array into 3 different 2D arrays
a_2d_1 = a_3d[0]
a_2d_2 = a_3d[1]
a_2d_3 = a_3d[2]

print("\nThird column of second 2-D array:\n",a_2d_2[0:,2])

# %%
print("\nFirst row of the first 2-D array:\n",a_2d_1[0,:])
print("\nThird row of the first 2-D array:\n",a_2d_1[0,:])
print("\nIntersection of first row and third column in third 2-D array:", a_2d_3[0,2])

# %% [markdown]
# Q4. Create a 2-D numpy array of random integers between
#  1 to 100 with shape 5*4. Now perform following
#  operations:
#  • Print only the even numbers from this array
#  • Print only the odd numbers from this array
#  • Print row wise sum of all elements
#  • Print column wise sum of all elements
#  • Convert this 2-D array into 3-D array of shape
#  2*2*5 

# %%
# Generate a 2-D array of shape 5x4 with random integers between 1 and 100 (inclusive)
array_2d = np.random.randint(1, 101, size=(5, 4))

# Print the generated 2-D array
print("Original 2-D Array:\n", array_2d)

# Print only the even numbers from this array
even_numbers = array_2d[array_2d % 2 == 0]
print("\nEven Numbers:\n", even_numbers)

# Print only the odd numbers from this array
odd_numbers = array_2d[array_2d % 2 != 0]
print("\nOdd Numbers:\n", odd_numbers)

# Print row-wise sum of all elements
row_wise_sum = array_2d.sum(axis=1)
print("\nRow-wise Sum:\n", row_wise_sum)

# Print column-wise sum of all elements
column_wise_sum = array_2d.sum(axis=0)
print("\nColumn-wise Sum:\n", column_wise_sum)

# Convert this 2-D array into a 3-D array of shape 2x2x5
array_3d = array_2d.reshape(2, 2, 5)
print("\nConverted 3-D Array:\n", array_3d)

# %% [markdown]
# Q5. Create a 2-D numpy array of random integers between
#  1 to 100 with shape 5*4. Now perform following
#  operations:
#  • Swap first row with third row
#  • Swap second column with fourth column.
#  • Replace the values less than 50 with zero.
#  • Convert this 2D array into 1-D array

# %%
# Generate a 2-D array of shape 5x4 with random integers between 1 and 100 (inclusive)
array_2d = np.random.randint(1, 101, size=(5, 4))

# Print the original 2-D array
print("Original 2-D Array:\n", array_2d)

# Swap first row with third row
array_2d[[0, 2]] = array_2d[[2, 0]]
print("\nArray after swapping first row with third row:\n", array_2d)

# Swap second column with fourth column
array_2d[:, [1, 3]] = array_2d[:, [3, 1]]
print("\nArray after swapping second column with fourth column:\n", array_2d)

# Replace values less than 50 with zero
array_2d[array_2d < 50] = 0
print("\nArray after replacing values less than 50 with zero:\n", array_2d)

# Convert the 2-D array into a 1-D array
array_1d = array_2d.flatten()
print("\nConverted 1-D Array:\n", array_1d)

# %% [markdown]
# Q6. Explain the concept of stacking in numpy with examples.
#  How is it different from concatenation. Give any 3
#  differences between them.

# %% [markdown]
# Stacking in NumPy refers to the process of joining multiple arrays along a new axis. 
# The primary functions used for stacking are np.stack, np.hstack, np.vstack, and np.dstack.
# 
# 
# Functions used in stacking
# 
# 1. np.stack: Adds a new axis, stacking along that new axis.
# 2. np.hstack: Stacks arrays horizontally (column-wise).
# 3. np.vstack: Stacks arrays vertically (row-wise)
# 4. np.dstack: Stacks arrays depth-wise (along the third axis)

# %%
#Examples for the fucntions used in Stacking

# np.stack

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

stacked = np.stack((a, b), axis=0)  # Stacks along a new axis (0th axis)
print("\nOutput of np.stack\n",stacked)


#np.hstack
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

hstacked = np.hstack((a, b))
print("\nOutput of np.hstack\n",hstacked)

#np.vstack

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vstacked = np.vstack((a, b))
print("\nOutput of np.vstack\n",vstacked)

#np.dstack

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

dstacked = np.dstack((a, b))
print("\nOutput of np.dstack\n",dstacked)

# %% [markdown]
# Concatenation in NumPy refers to the process of joining a sequence of arrays along an existing axis. 
# The primary function used for concatenation is np.concatenate.
# 
# In NumPy, both stack and concatenate functions are used to combine arrays, 
# but they do so in different ways and serve different purposes. 
# Here's a detailed explanation of the functional differences between np.stack and np.concatenate:
# 
# np.stack
# 
# Purpose: Combines a sequence of arrays along a new axis.
# 
# Functionality: It requires all input arrays to have the same shape. np.stack adds a new dimension (axis) to the arrays and then stacks them along that axis.
# 
# Use Case: When you need to create a higher-dimensional array by combining arrays along a new axis.
# 
# 
# np.concatenate
# 
# Purpose: Joins a sequence of arrays along an existing axis.
# 
# Functionality: It combines arrays without adding a new axis. The arrays must have compatible shapes except in the dimension corresponding to the axis along which they are concatenated.
# 
# Use Case: When you need to join arrays along an existing axis, maintaining the number of dimensions of the arrays.
# 



