import numpy as np

class FiboMatrix:

    def __init__(self, matrix):
        self.matrix = np.array(matrix, dtype=int)
        self.memo = {}  # Mémoire pour optimisation
    
    def solve_matrix(self):
        """
        Calcule la matrice avec les éléments remplacés par leurs équivalents de Fibonacci.
        """

        if self.matrix.size == 0:  # Matrices vides
            return self.matrix

        # Taille de la matrice
        n_rows, n_cols = self.matrix.shape
        
        result_matrix = np.zeros_like(self.matrix, dtype=int)
        
        for i in range(n_rows):
            for j in range(n_cols):
                result_matrix[i][j] = self.calculate_fibo(self.matrix[i][j])

        return result_matrix

    
    def calculate_fibo(self, number):
        """
        Calcule la valeur de Fibonacci pour un entier donné avec mémorisation.
        """
        if number in self.memo:
            return self.memo[number]
        if number <= 0:
            self.memo[number] = 0
            return 0
        elif number == 1:
            self.memo[number] = 1
            return 1
        else:
            self.memo[number] = self.calculate_fibo(number - 1) + self.calculate_fibo(number - 2)
            return self.memo[number]



if __name__ == "__main__":
    matrix = [
        [1, 4, 6],
        [8, 12, 22],
        [33, 43, 50]
    ]
    
    fibo_matrix = FiboMatrix(matrix)
    result = fibo_matrix.solve_matrix()
    print("Matrice originale :")
    print(np.array(matrix))
    print("Matrice Fibonacci :")
    print(result)
