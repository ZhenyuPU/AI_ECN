# PAPY

## 读取文件与爬虫

```python

f = open('filename', 'r')
file = f.read()

import urllib.request as eq
url='https://fr.wikipedia.org/wiki/Python_(langage)'#抓取的网址
file=eq.urlopen(url).read()#读取信息

path = open('filename', 'wb')  # w--write, b--binaire

path.write(file)

path.close()

with open('filename', 'r') as file:
    content = file.read()

with open(output_filename, 'w') as file:
    file.write(content_without_e)

with open('fable.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
```

`.strip()`用于移除字符串开头和结尾的空白字符（空格、制表符、换行符等）


## Variables, mutable et immutable
`sorted`: `sorted(li, key, reverse = False)`
Dict: `sorted(dic.items(), key = lambda x: x[0/1], reverse = True/False)`: revoie une liste avec des tuples
`{k:v for k, v in dic_sorted}` peut revoyer une dict

`zip(a, b)`: 把两个列表联合起来，用list(map)可以得到列表带着tuple

raise  错误类型：

ValueError: les values sont erreurs
TypeError: le type est false
AssertionError: avec assert
Exception: generalement

浅拷贝会复制字典的键和值的引用，但对于嵌套的可变对象（如列表），它们仍然指向相同的对象。

`new_dic={**dictionnaire,**{"var":1.2}}`: c'est pour concaténer deux dictionnaires.


## Décoration
@décoration
Il permet de marquer la fonction pour modifier la comportement.
```python
from time import time
def timer(func:"fonction")->"fonction":
    name=func.__name__
    # 要引入args必须多写一个函数
    def timed_func(*args, **wargs):
        t1=time()
        arg_str=', '.join(repr(arg) for arg in args)
        resultat=func(*args)
        elapsed=time()-t1
        print(f"{name}({arg_str}) elapsed time [{elapsed:0.8f}s]")
        return resultat
    return timed_func
@timer
def factorielle(n: int)->int:
    res=1
    for i in range(1,n): 
        res*=i
    return res
```

## iteration et generateur

yield: renvoie la valeur courante et attend la prochaine boucle, reprend le programme ou il s'arrete

写了yield的函数，是一个generateur，相当于把list--iterable

functool

- map(func, sequence/list) appliquer une fonction a une sequence [paresseux]
- filter(func, list) appliquer une fonction a une sequence et renvoie la valeur de list vraie
- reduce(func, list) appliquer de facon commulative la fonc a list
```python
from functools import reduce
from operator import add
reduce(add, [1, 2, 3])
# renvoie 6
```


## Héritage de class (orientation de l'objet)

### class
`__init__`: est le constructeur de la classe. apple chaque fois que cette classe est instanciee

`__str__`: l'affichage renvoye par `print()`, renvoie `__repr__` sinon defini

`__repr__`: definit une representation de l'objet
`@property`: definit un raccourcis qui s'utilise comme variables
`var_name.setter`: pour pouvoir modifier la valeur de la variable
`@classmethod`: initialiser une instance de classe. ne necessite pas de definir une instance tout d'abord
`@staticmethod`: 静态方法是与类相关联的方法，而不与类的实例（对象）相关联。不需要接受任何隐式的 self 参数，因此它们无法访问或修改实例特定的属性或方法。静态方法通常用于执行与类有关的通用操作，而不需要访问实例级别的数据。

@classmethod（类方法）：

类方法也是与类相关联的方法，但它们接受一个隐式的 cls 参数，可以用于访问和修改类级别的属性和方法。
类方法通常用于执行与类有关的操作，可能需要访问或修改类级别的数据，但不需要访问实例级别的数据。


```python
class Calculator:
    def __init__(self):
        self.result = 0

    def __call__(self, x):
        # 将对象实例像函数一样进行调用，执行加法操作
        self.result += x
        return self.result

# 创建计算器对象
add_numbers = Calculator()

# 使用对象实例进行加法操作
print(add_numbers(5))  # 输出：5
print(add_numbers(10))  # 输出：15
print(add_numbers(7))  # 输出：22
```
__iter__ 和 __next__：用于定义对象的可迭代性，可以在类中实现这些方法以使对象可以迭代。

__add__、__sub__、__mul__、__truediv__: 加减乘除
```python
class CustomNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # 定义加法操作
        return CustomNumber(self.value + other.value)

    def __sub__(self, other):
        # 定义减法操作
        return CustomNumber(self.value - other.value)

    def __mul__(self, other):
        # 定义乘法操作
        return CustomNumber(self.value * other.value)

    def __truediv__(self, other):
        # 定义真除法操作
        if other.value == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return CustomNumber(self.value / other.value)

    def __str__(self):
        return str(self.value)

# 创建两个自定义数值对象
num1 = CustomNumber(5)
num2 = CustomNumber(2)

# 使用自定义的加、减、乘、除操作
result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2
result_div = num1 / num2

print("Addition:", result_add)  # 输出：Addition: 7
print("Subtraction:", result_sub)  # 输出：Subtraction: 3
print("Multiplication:", result_mul)  # 输出：Multiplication: 10
print("Division:", result_div)  # 输出：Division: 2.5
```

### heritage
une classe fille peut heriter les propriete de classe mere. facoriser efficacement le code
```python
class mere:
    def __init__（self, x, y):
        pass

class fille(mere):
    def __init__(self, x, y, a, b):
        super(fille, self).__init__(x, y)  # ()可以不写里面的
```

## programmation fonctionnelle

### print
`format:f"{arg:0.4f/0.4d}"`

### func(*args, **wargs)

### func_new(func)

## Module
### relative path:
```python
from .. import mymodule  # 本文件的上一个repertoire
from . import mymodule # 本文件所在repertoire
from ..folder import mymodule # 上一个repertoire 引用mymodule
```


### os, sys, path, lib
`os`: interagir avec le systeme d'exploitation, travailler avec les fichiers
```python
os.name
os.getcwd()   # path
os.mkdir('file')
os.listdir()
os.chdir()  # 转到
```

`sys`: interagir avec l'interpreteur python
`sys.version`, `sys.argv`, `sys.path`

### timer
```python
from time import time
t1 = time()
t2 = time()
```
`%time func`:CPU times: user 7.99 s, sys: 348 ms, total: 8.34 s
Wall time: 1min
`%timeit func`: loop
```python
%%timeit
def func:
    pass
```

### random
`random.randint(low, high)`: renvoie une valeur entre low et high--int
`random.random()`: renvoie v entre 0 et 1
`random.uniform(low, high)`: float comme randint
generer une liste:
`[random.randint(1, 5) for _ in range(10)]`

### numpy pour réducer le temps
- `np.array`: 可以把list转为array, l = np.array([matrix]), l[i, j] 第i行，第j列 从0开始
但是`list`: 只能这么引用--l[i][j]
- `np.ndarray(shape, dtype)`: 多维矩阵
如果一个三维数组的形状是 (2, 3, 4)，那么它表示一个包含两个二维矩阵的集合，每个矩阵都有 3 行和 4 列。这相当于一个 2x3x4 的立方体结构。

- `np.arange(n)`: array([0->n-1])
- `np.random`:
    `np.random.random(size)`:(0,1)产生n个点
    `np.random.randint(low, high, size)`:

- `np.linspace(low, high, size, endpoint=True)`: comme randint

- `np.linalg`:
    `np.linalg.det(A)`:det(A)
    `np.linalg.inv(A)`:inv(A)
    `np.linalg.norm(vecteur)`:norm(vecteur)
    `np.linalg.solve(a, b)`:解 $a * x = b$
- `np.log(x)`: 以e为底

- `np.vstack((a1, a2))`: 垂直联合

- `np.hstack((a1, a2))`:水平联合

- `np.vsplit(x, num)` et `np.hsplit(x, num)`

### math
- 基本数学运算：
    math.sqrt(x)：计算平方根。
    math.pow(x, y)：计算 x 的 y 次方。
    math.exp(x)：计算 e 的 x 次方。
    math.log(x)：计算 x 的自然对数。
    math.log(x, base)：计算 x 的以指定底数为底的对数。
    math.ceil(x)：向上取整。
    math.floor(x)：向下取整。
    math.trunc(x)：截断小数部分。
- 三角函数：
    math.sin(x)：计算正弦值。
    math.cos(x)：计算余弦值。
    math.tan(x)：计算正切值。
    math.asin(x)：计算反正弦值。
    math.acos(x)：计算反余弦值。
    math.atan(x)：计算反正切值。
    math.atan2(y, x)：计算给定 x 和 y 坐标的反正切值。

- 其他数学函数：

    math.factorial(x)：计算 x 的阶乘。
    math.gcd(x, y)：计算 x 和 y 的最大公约数。
    math.isfinite(x)：检查 x 是否是有限数。
    math.isnan(x)：检查 x 是否是 NaN（非数字）。
- 常数：
    math.pi：圆周率 (π) 的近似值。
    math.e：自然常数 (e) 的近似值。

### matplotlib
- plt.plot():
    ```python
    plt.plot(x, y, color = 'black', 
         linestyle = '--', label = 'ad',
         linewidth = 2,
         marker = 'o', markersize = 10, 
         alpha = 0.5)
    # 显示图例
    plt.legend()
    plt.xlabel('name')
    plt.xlim(low, high)
    plt.xticks(list)

    plt.grid()
    plt.title('filename')
    plt.savefig('filename', dpi = dpi)
    """
    dpi signifie la qualite de l'image et represente le pixel par pouce d'espace
    """
    plt.show()
    ```
- plt.subplot:
    `plt.subplot(num_rows, num_cols, plot_number)`
    num_rows：表示子图布局中的行数。
    num_cols：表示子图布局中的列数。
    plot_number：表示当前子图的位置
- plt.figure():
    figsize：指定图形的宽度和高度，以英寸为单位。它是一个包含两个浮点数的元组，例如 (8, 6)，表示宽度为 8 英寸，高度为 6 英寸。默认值为 (6.4, 4.8)。

    dpi：指定图形的分辨率，即每英寸的像素数。默认值为 100。

    facecolor：指定图形的背景颜色，可以是颜色名称（如 'white'、'lightgray'）或十六进制颜色代码（如 '#FF0000'）。

    edgecolor：指定图形的边框颜色，使用与 facecolor 相同的颜色格式。

    frameon：布尔值，控制是否显示图形的边框。默认为 True，显示边框。

    clear：布尔值，控制是否清除图形中的已有图形元素。默认为 False，即在图形中追加新图形。


#### objet
ax = plt.subplot(...):

1. 设置标题和标签：

    set_title(label, fontdict=None, loc='center', pad=None, **kwargs)：设置子图的标题。
    set_xlabel(xlabel, fontdict=None, labelpad=None, **kwargs)：设置 x 轴标签。
    set_ylabel(ylabel, fontdict=None, labelpad=None, **kwargs)：设置 y 轴标签。

1. 设置坐标轴范围：

    set_xlim(left=None, right=None, emit=True, auto=False, xmin=None, xmax=None)：设置 x 轴的范围。
    set_ylim(bottom=None, top=None, emit=True, auto=False, ymin=None, ymax=None)：设置 y 轴的范围。

1. 设置刻度和刻度标签：

set_xticks(ticks, minor=False)：设置 x 轴刻度的位置。
set_yticks(ticks, minor=False)：设置 y 轴刻度的位置。
set_xticklabels(labels, fontdict=None, minor=False, **kwargs)：设置 x 轴刻度的标签。
set_yticklabels(labels, fontdict=None, minor=False, **kwargs)：设置 y 轴刻度的标签。

1. 添加图例：

legend(labels, *args, **kwargs)：添加图例。
1. 绘图方法：

plt.plot(x, y, fmt, **kwargs)：绘制线图。
plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None, **kwargs)：绘制散点图。
1. 其他绘图方法，如 bar(), hist(), imshow(), 等。
1. 设置背景颜色和样式：

set_facecolor(color)：设置子图的背景颜色。
set_axis_off()：关闭子图的坐标轴。
1. 保存图形：

savefig(fname, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None, metadata=None)：保存图形为文件。


**Figure 对象 (fig)：**

1. 设置图形大小：

set_size_inches(w, h)：设置图形的宽度和高度，以英寸为单位。

1. 保存图形：

savefig(fname, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None, metadata=None)：保存图形为文件。
关闭图形：

close()：关闭图形窗口

fig, ax = plt.subplot('2',...)

#### mapcolor et cmap

`plt.imshow(array, cmap, norm, aspect,alpha, vmin, vmax, origin, extent)`
    array：要显示的二维数组，通常是图像数据。这可以是一个 NumPy 数组或其他支持的数据类型。

    cmap：颜色映射（Colormap），指定了如何将数据值映射到颜色。例如，'viridis'、'cividis'、'jet' 等。您可以使用 matplotlib 中提供的不同颜色映射。

    norm：用于规范化数据值的对象。默认情况下，它是 None，表示不进行规范化。规范化可以帮助将数据值映射到颜色映射的范围内。

    aspect：控制图像的长宽比。通常，设置为 'equal' 可以保持图像的纵横比，但也可以是其他字符串值或浮点数。

    alpha：控制图像的透明度，通常在 0 到 1 之间的浮点数。

    vmin 和 vmax：用于设置颜色映射的数据范围。例如，vmin=0 和 vmax=255 可以将图像的像素值范围映射到颜色映射的范围。

    origin：指定数据的原点位置。通常为 'upper'（默认）或 'lower'，决定了图像的坐标系原点。

    extent：指定图像的数据坐标范围，通常为四个浮点数元组，如 (left, right, bottom, top)。


#### normalize

```python
import matplotlib.pyplot as plt
import matplotlib.colors as color
import numpy as np
data = np.random.randint(0, 100, size=(10, 10))
norm = color.Normalize(vmin=0, vmax=100)
plt.imshow(data, cmap='viridis', norm=norm)
plt.colorbar()  # 添加颜色条
plt.show()

```




### pix
```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
""" La méthode plus rapide """
def plot_mandelbrot(zmin = -2-2j, zmax = 2+2j, 
                    pixel_size = 0.0005, max_iter = 50, 
                    figname = 'img/Mandelbrot.png'):
    w = int(1 / pixel_size)  # Nombre de points régulièrement espacés sur la pièce réelle
    h = int(1 / pixel_size)  # Nombre de points régulièrement espacés sur la partie imaginaire
    # définir l'arrière-plan
    bitmap = Image.new("RGB", (w, h), "white")
    pix = bitmap.load()
    
    # Créer des valeurs équidistantes sur les parties réelles et imaginaires
    real_values = np.linspace(zmin.real, zmax.real, w)
    imag_values = np.linspace(zmin.imag, zmax.imag, h)

    for x in range(w):
        for y in range(h):
            real_value = real_values[x]
            imag_value = imag_values[y]
            c = complex(real_value, imag_value)
            if is_in_Mandelbrot(c, max_iter = max_iter):
                # matrice de pixels
                pix[x, y] = (0, 0, 0)
    bitmap.save(figname)
    bitmap.show()
```

## test
pourquoi: s'assurer a la main que notre code fait ce que l'on souhaite lord du developpement.

**使用assert**
```python
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5    # erreur il faut 4

test_answer()
```
### automatiser avec pytest, inittest, doctest

#### pytest
si on l'execute a la racine d'un projet, il va effectuer tous les tests et publier un rapport

可以在ligne de cmd

#### unittest
il repose sur une classe de test
```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
# pour les fichiers  mais erreur:
if __name__ == '__main__': 
   unittest.main()

# succes
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```
#### doctest

il faut ecrire un docstring
```python
def func(x):
    """

    Calcule la moyenne d'une liste de valeurs.

    Args:
        valeurs (list): Une liste de nombres à partir desquels la moyenne est calculée.

    Returns:
        float: La moyenne des valeurs.

    Example:
    
    >>> func(x)
    res
    >>> func(y)
    Traceback (most recent call last)
    ...
    TypeError: can only concatenate...
    """
    pass
```

```python
import doctest
print(doctest.testmod(verbose=1))
```

### debug

`%debug` ou `python -m pdb script.py`

### reduction de la complexite
#### numba
user et abuser des bibliotheques
```python
import numba
@numba.jit(nopython=True) # just in time
def func():
    pass
```

#### concurrence et parallelisme
**concurrence**
```python
from threading import Thread
class Drapeau(Thread):
    def __init__(self, code):
        super().__init__()
        self.code = code

    def run(self):
        pass
```

**parallelisme**
```python
import cumpy as cp
```