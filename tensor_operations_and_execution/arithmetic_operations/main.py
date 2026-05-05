import tensorflow as tf

# 1. In-place addition of a 2x2 matrix
matrix = tf.Variable([[1, 2], [3, 4]])
addition_values = tf.constant([[5, 5], [3, 3]])
matrix.assign_add(addition_values)
print(matrix)  
print('-' * 80)

# 2. Subtraction using `tf.subtract` method for a 2x3 matrix
matrix = tf.constant([[1, 2, 3], [4, 5, 6]])
subtraction_values = tf.constant([[1, 2, 3], [4, 5, 6]])
result_subtraction = tf.subtract(matrix, subtraction_values)
print(result_subtraction)  
print('-' * 80)

# 3. Broadcasting multiplication of a 3x2 matrix with another 1x2 matrix
matrix_a = tf.constant([[1, 2], [3, 4], [5, 6]])
matrix_b = tf.constant([[2, 4]])
result_multiplication = matrix_a * matrix_b  # Broadcasting multiplication
print(result_multiplication)  
print('-' * 80)

# 4. Division using the `/ sign between a 2x3 matrix and a 2x1 matrix
matrix_a = tf.constant([[2, 4, 6], [4, 8, 12]])
matrix_b = tf.constant([[2], [4]])
result_division = matrix_a / matrix_b  # Broadcasting division
print(result_division) 