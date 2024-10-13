import numpy as np

def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]):
    a = np.array(a)
    b = np.array(b)
    if a.shape[1] == b.shape[0]:
        res = a @ b
        return res.tolist()

    else:
        return -1

a = [[1, 2],
     [2, 4]]
b = [1, 2]  
print(matrix_dot_vector(a, b))