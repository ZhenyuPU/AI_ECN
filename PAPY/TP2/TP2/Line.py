import numpy as np
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point{self.x}, {self.y}"

class LineaireObject:
    def __init__(self):
        pass

    @classmethod
    def vec_init(cls, vector, origin):
        obj = cls()
        obj.vector = np.array(vector)
        obj.origin = np.array(origin)
        return obj

class line(LineaireObject):
    def __str__(self):
        a = np.linalg.norm(self.vector)
        if a != 0:
            para_a = self.vector[0] / a
            para_b = self.vector[1] / a
        para_c = -para_a * self.origin[0] - para_b * self.origin[1]
        equation = f"Line object with equation : {para_a}x+{para_b}y+{para_c}=0"
        return f"{equation}\nwith vector:{tuple(self.vector)} and origin: {list(self.origin)}"
   

