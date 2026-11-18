import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    trans=[]
    rows = len(A)
    cols = len(A[0])

    for j in range(cols):
        arr = []
        for i in range(rows):
            arr.append(A[i][j])
        trans.append(arr)

    return np.array(trans)
        
    
