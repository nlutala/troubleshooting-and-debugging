"""
problems/troubleshoot_7.py

Troubleshoot the issue 7: (created by Generative AI)

Author: Nathan Lutala (nlutala)

Nothing to debug here, the code is correct
"""

import numpy as np

def matrix_multiplication(A, B):
    result = np.zeros((len(A), len(B[0])))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    print(matrix_multiplication(A, B))
