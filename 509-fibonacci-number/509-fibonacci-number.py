import numpy as np
class Solution:
    def fib(self, n: int) -> int:
        F1 = np.array([[1, 1], [1, 0]])
        eigenvalues, eigenvectors = np.linalg.eig(F1)
        Fn = eigenvectors @ np.diag(eigenvalues ** n) @ eigenvectors.T
        return int(np.rint(Fn[0, 1]))