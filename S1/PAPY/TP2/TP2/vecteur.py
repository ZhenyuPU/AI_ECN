from math import pi
from array import array  # On évite ainsi de recourrir à numpy en utilisant un built-in
from numbers import Real
import math  # bien utile pour tout un tas d'opérations


class Vecteur:
    def __init__(self, x, y):
        self._x = None
        self._y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, Real):
            self._x = value
        else:
            raise ValueError(f"val='{self._x}' must be a real")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if isinstance(value, Real):
            self._y = value
        else:
            raise ValueError(f"val='{self._y}' must be a real")

    @property
    def norme(self):
        return math.sqrt(self.x**2 + self.y**2)
    

    def angle(self, other):
        if isinstance(other, Vecteur):
            return math.acos(self * other/(self.norme * other.norme))

    def __repr__(self):
        """Représentation textuelle de l'objet"""
        return f"Vecteur({self.x}, {self.y})"
    
    def __len__(self):
        return 2

    def __iter__(self):
        """Iterateur sur les élements du vecteur, utilise yield"""
        yield self.x
        yield self.y

    def __str__(self):
        """Appelé par print()"""
        return f"({str(self.x)}, {str(self.y)})"
    # '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        """Surcharge de l'opérateur =="""
        if isinstance(other, Vecteur):
            return self.x == other.x and self.y == other.y
        return False

    def __abs__(self):
        """surcharge du built-in abs()"""
        return (self.x**2 + self.y**2)**0.5

    def __neg__(self):
        return (-self.x, -self.y)

    def __add__(self, others):
        if isinstance(others, Vecteur):
            return Vecteur(x=self.x + others.x, y=self.y + others.y)
        elif isinstance(others, list):
            return [self.x + others[0], self.y + others[1]]
        else:
            raise TypeError(
                "Unsupported operand type for +: Vecteur and {}".format(type(others)))

    def __radd__(self, other):
        if isinstance(other, list):
            # 如果other是列表，则将向量的x和y分别加到列表中的元素
            return [self.x + other[0], self.y + other[1]]
        else:
            raise TypeError(
                "Unsupported operand type for +: {} and Vecteur".format(type(other)))
        

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vecteur(x=self.x * other, y=self.y * other)
        elif isinstance(other, Vecteur):
            if len(self) != len(other):
                raise ValueError("Vectors must have same length")
            return sum(a * b for a, b in zip(self, other))
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector' and '{}'".format(type(other).__name__))
    
    def __rmul__(self, other):
        return Vecteur(x=self.x * other, y=self.y * other)




    @classmethod
    def from_iterable(cls, it):
        x, y = it
        return cls(x, y)

    @classmethod
    def from_polar(cls, r: float, theta: float):
        x = r*math.cos(theta)
        y = r*math.sin(theta)
        return cls(x, y)
    


