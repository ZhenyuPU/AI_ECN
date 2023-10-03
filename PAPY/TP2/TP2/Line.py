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
    
    @classmethod
    def point_init(cls, origin, vector):
        obj = cls()
        obj.origin = origin
        obj.vector = vector
        return obj

class line(LineaireObject):
    def __str__(self):
        a = np.linalg.norm(self.vector)
        if a != 0:
            self.para_a = self.vector[0] / a
            self.para_b = - self.vector[1] / a
        self.para_c = -self.para_a * self.origin[0] - self.para_b * self.origin[1]
        self.para_ab = [self.para_b, - self.para_a]
        equation = f"Line object with equation : {self.para_a}x+{self.para_b}y+{self.para_c}=0"
        return f"{equation}\nwith vector:{tuple(self.para_ab)} and origin: {list(self.origin)}"
    

def lines_angle(line1, line2):
    cos = line1.vector.dot(line2.vector) / (np.linalg.norm(line1.vector)*np.linalg.norm(line2.vector))
    return np.arccos(cos)

def lines_intersect_point(line1, line2):
    x = (line2.para_a * line1.para_b - line1.para_c * line2.para_b) / (line1.para_a * line2.para_b - line2.para_a * line1.para_b)
    y = (line1.para_a*line2.para_c - line2.para_a*line1.para_c) / (line2.para_a*line1.para_b - line1.para_a*line2.para_b)
    return [x, y]

def rotate2d(angle, P: list[float]):
    x, y = P[0], P[1]
    r = math.sqrt(x**2 + y**2)
    cos = np.cos(angle)
    sin = np.sin(angle)
    return [r*(x*cos - y*sin), r*(y*cos + x*sin)]



   

