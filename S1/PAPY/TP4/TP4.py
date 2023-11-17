
import numpy as np
import random
import sys

class MatCooPure:
    def __init__(self, m, n, n_non_nul):
        # coordinate list
        self.row = m
        self.column = n
        mat = np.array([np.array([0 for _ in range(n)]) for _ in range(m)])
        for _ in range(n_non_nul):
            row = random.randint(0, self.row-1)
            column = random.randint(0, self.column-1)
            if mat[row][column] == 0:
                mat[row][column] = random.randint(1, 1)
        self.mat = mat
    
    def __str__(self):
        return (self.mat[i][j] for j in range(self.column) for i in range(self.row))

    # def identity_init_pur(self):
    #     if self.row == self.column:
    #         for i in range(self.row):
    #             for j in range(self.column):
    #                 if i == j:
    #                     self.mat[i][j] = 1
    #         return 
    #     else:
    #         raise ValueError("Ne pas etre carre")
    
    def dot_pur(self, vector):
        dot = [0] * self.row
        for i in range(self.row):
            for j in range(self.column):
                dot[i] += self.mat[i][j] * vector[j]
        return np.array(dot)

class MatCooNumpy:
    def __init__(self, m, n, n_non_nul):
        # coordinate list
        self.row = m
        self.column = n
        mat = np.zeros((m, n))
        for _ in range(n_non_nul):
            row = random.randint(0, self.row-1)
            column = random.randint(0, self.column-1)
            if mat[row][column] == 0:
                mat[row][column] = random.randint(1, 1)
        self.mat = mat

    def __str__(self):
        return (self.mat[i][j] for j in range(self.column) for i in range(self.row))
    
    def dot_np(self, vector):
        return np.dot(self.mat, vector)

def identity_init_np(mat):
    if len(mat) == len(mat[0]):
        return np.identity(len(mat))
    else:
        raise ValueError("Ne pas etre carre!")

def choix_dot(class_, vector):
    if isinstance(class_, MatCooPure):
        return class_.dot_pur(vector)

    elif isinstance(class_, MatCooNumpy):
        return class_.dot_np(vector)

if __name__ == '__main__':
    m = 10000
    purMat = MatCooPure(m = 10000, n = 10000, n_non_nul = 10000)
    # print(purMat.mat)
    npMat = MatCooNumpy(m = 10000, n = 10000, n_non_nul = 10000)
    # print(npMat.mat)

    # extrait
    pur_ext = purMat.mat[:4, :4]
    np_ext = npMat.mat[:4, :4]
    # dimension
    pur_m, pur_n = len(purMat.mat), len(purMat.mat[0])

    np_m, np_n = len(npMat.mat), len(npMat.mat[0])

    # memory
    pur_memory = sys.getsizeof(purMat.mat)
    np_memory = npMat.mat.nbytes

    # affichage
    print(f"l'extrait est \n{pur_ext}\n{np_ext}\n"
          f"pur de la dimension est{(pur_m, pur_n)}\n"
          f"np de la dimension est {(np_m, np_n)}\n"
          f"pur_memory est {pur_memory}\n"
          f"np_memory est {np_memory}")
    
    # vector
    vector = np.random.randint(1, m+1, size = m)
    # pur_vec = purMat.dot_pur(vector)
    # np_vec = npMat.dot_np(vector)
    # print(f"pur_vec est\n{pur_vec}\n"
    #       f"np_vec est \n{np_vec}")

    # choix
    print(choix_dot(purMat, vector))
    






