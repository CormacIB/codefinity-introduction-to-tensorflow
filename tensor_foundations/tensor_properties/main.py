import tensorflow as tf

# Create a tensor
tensor = tf.constant([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# 1. Retrieve the properties of the first tensor
print(f'Number of dimensions (rank): {tensor.ndim}')
print(f'Shape: {tensor.shape}')
print(f'Data type: {tensor.dtype}')
print('-' * 40)

# 2. Construct a tensor that meets the specified criteria
new_tensor = tf.constant([[[1.,1.,.1],[.1,.1,.1],[1.,1.,.1],[.1,.1,.1]],[[1.,1.,.1],[.1,.1,.1],[1.,1.,.1],[.1,.1,.1]]])


# Retrieve the properties of the new tensor
print(f'Number of dimensions (rank): {new_tensor.ndim}')
print(f'Shape: {new_tensor.shape}')
print(f'Data type: {new_tensor.dtype}')