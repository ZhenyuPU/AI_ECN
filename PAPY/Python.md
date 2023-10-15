# <center>Python</center>

## mutable et immutable

**不可变（immutable）**：int、字符串(string)、float、（数值型number）、元组（tuple)，None

优点：
这样可以减少重复的值对内存空间的占用。
缺点：
操作之后就开辟内存的特性。执行效率会有一定程度的降低。

**可变（mutable）变量**：字典型(dictionary)、列表型(list)
对于可变变量 ，创建一次就开辟一次地址，不会引用同一块内存; 而对同一个对象的操作。内存地址是不会改变的

## 读取文件



## 打印输出格式

```python
print("Plage de dates: de {} à {}".format(initial_date,final_date))
print(f"{}")
```

## class

```python
class Avion2:
    max_speed = 0
    Avions    = []
    def __init__(self):
        Avion2.Avions.append(self)
```
`Avion2.Avions.append(self)` 添加实例到类级别的 Avions 列表中，这意味着所有 Avion2 类的实例将共享同一个 Avions 列表。如果你创建多个 Avion2 对象，它们都会添加到同一个列表中。

`self.Avions.append(self)` 添加实例到实例级别的 Avions 列表中，这意味着每个 Avion2 实例都有自己的独立的 Avions 列表，不会共享。这样每个对象都有一个独立的列表来跟踪它们自己创建的对象。


### class里面的自定义函数
```python
class Class:
    def __init__(self):
        self._a
        self.b
    def __str__(self):
        return f"{self}"
    def __len__(self):
        return len(self)
    def __iter__(self):
        return self
    def __next__(self):
        if ():
            ...
        else:
            raise StopIteration
    def __repr__(self):
        # text representation of the object
        return f""
    # 我们可以使用@property装饰器来创建只读属性，
    # @property装饰器会将方法转换为相同名称的只读属性,可以与所定义的属性配合使用，这样可以防止属性被修改。
    @property  # 只读
    def fun(self):
        return ...
    @property
    def a(self):    # 私有属性
        return self._a 
    @property
    def x(self):
        return self._x
    @x.setter  # 可写
    def x(self, values):
        ...
        self_x = ...
    @classmethod
    def fun2(cls):
        ...
    

c = Class()
c.fun  # 如同属性一样，不用加()
A.fun2()  # 不需要实例化
```
__method__:

__abs__：用于定义绝对值操作，可以在类中实现该方法来支持内置函数 abs() 对对象的操作。

__len__：用于定义对象的长度，可以在类中实现该方法来支持内置函数 len() 对对象的操作。

__getitem__：用于支持通过索引或键访问对象的元素，可以在类中实现该方法来支持索引操作，如 obj[key]。

__setitem__：用于支持通过索引或键设置对象的元素，可以在类中实现该方法来支持索引操作，如 obj[key] = value。

__delitem__：用于支持通过索引或键删除对象的元素，可以在类中实现该方法来支持索引操作，如 del obj[key]。

```python
class CustomDictionary:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        # 获取键对应的值
        return self.data[key]

    def __setitem__(self, key, value):
        # 设置键值对
        self.data[key] = value

    def __delitem__(self, key):
        # 删除键值对
        del self.data[key]
```
__eq__ 和 __ne__：分别用于定义对象的相等和不相等比较操作，可以在类中实现这些方法来支持 == 和 != 操作。

__lt__、__le__、__gt__、__ge__：分别用于定义对象的小于、小于等于、大于和大于等于比较操作，可以在类中实现这些方法来支持 <、<=、> 和 >= 操作。
```python
    def __lt__(self, other):
        # 定义小于比较
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        # 定义小于等于比较
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        # 定义大于比较
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        # 定义大于等于比较
        return self.to_meters() >= other.to_meters()
```

__str__ 和 __repr__：用于定义对象的字符串表示形式，__str__ 用于提供用户友好的表示，而 __repr__ 用于提供开发者友好的表示。

__call__：用于将对象作为函数调用，可以在类中实现该方法以使对象具有可调用的行为。

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

==classmethod:==

`classmethod` 修饰符对应的函数不需要实例化，不需要` self` 参数，但第一个参数需要是表示自身类的 `cls` 参数，可以来调用类的属性，类的方法，实例化对象等。

==另外==， @classmethod的作用实际是可以在`class`内实例化`class`，一般使用在有**工厂模式**要求时。作用就是比如输入的数据需要清洗一遍再实例化，可以把清洗函数定义在class内部并加上`@classmethod`装饰器已达到减少代码的目的。总结起来就是：`@class method`可以用来为一个类创建一些预处理的实例。

```python
class Data_test2(object):
    day=0
    month=0
    year=0
    def __init__(self,year=0,month=0,day=0):
        self.day=day
        self.month=month
        self.year=year
    @classmethod
    def get_date(cls,data_as_string):
 
        #这里第一个参数是cls， 表示调用当前的类名
 
        year,month,day=map(int,data_as_string.split('-'))
        date1=cls(year,month,day)     #返回的是一个初始化后的类
        return date1
 
    def out_date(self):
        print("year :",self.year)
        print("month :",self.month)
        print("day :",self.day)

r=Data_test2.get_date("2020-1-1")
r.out_date()
```

迭代器定义:

1）通过在类中添加 __iter__函数，向系统说明这是一个可迭代对象。

2）通过在类中添加 __next__函数，向系统提供该可迭代对象的迭代算法

3）在代码执行过程中，for循环函数会自动检查系统信息，识别__iter__函数，然后自动调用对应的__next__函数，生成一个迭代器。

4）所以在定义一个可迭代类时，一般__iter__ 函数要与 __next__函数成对出现。__iter__函数向系统声明这个类可迭代，__next__定义了具体的迭代器。

5）__iter__ 与 __next__两个函数名不可改变，否则系统会不识别。

6）__next__函数的 return 在 if 判别命令的内部，每次执行__next__函数时，单次判别后直接输出。不满足判别条件时输出迭代终止。

生成器：

```python
L = [x*x for x in range(10)]
L
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x*x for x in range(10))
g
# <generator object <genexpr> at 内存地址>

```

生成器：在函数内使用 yield 关键字，每次调用函数类似于对迭代器执行 next() 方法，生成器实际是一种特殊的迭代器。

带`yield`关键字的函数可以看做是生成器对象，所以刚开始`obj = func()`的时候，并不会直接执行函数，而是调用`next`的时候才会逐步执行生成数据。

可迭代对象：

如果一个类中实现了__iter__方法，并且返回的是一个迭代器对象(生成器对象，因为生成器是特殊的迭代器)，可以称这个类实例化的对象为可迭代对象。

```python
# 迭代器对象类型 实例化成迭代器对象
class IT(object):
    def __init__(self):
        self.counter = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration()
        return self.counter
        
 
 # 可迭代对象类型，实例化成可迭代对象
 class Foo():
    def __iter__(self):
        return IT()  # 返回一个迭代器对象

obj = Foo()
# 循环可迭代对象，先从obj.__iter__获取迭代器对象
for item in obj:
    print(item)
```

range:
```python
r = range(100)  # 可迭代对象
dir(r) #[... '__iter__'...]
# 只有iter，没有next说明r是可迭代对象，不是迭代器对象

v = r.__iter__()  # r调用iter之后获取v为迭代器对象
dir(v) #[... '__iter__'...， '__next__']  # 有iter和next说明v是迭代器对象
```


__str__ 和 __repr__

__str__是一个对象的非正式的、易于阅读的字符串描述，当类str实例化（str(object)）时会被调用，以及会被内置函数format()和print()调用, 返回值必须是字符串对象，此方法通常被用于调试。内置类型 object 所定义的默认实现会调用 object.__repr__();

__repr__是一个对象的官方字符串描述，会被内置函数repr()方法调用，它的描述必须是信息丰富和明确的。也就是说__str__返回的结果可读性强，__repr__返回的结果更加准确。返回值必须是字符串对象，此方法通常被用于调试。内置类型 object 所定义的默认实现会调用 object.__repr__()

```python
>>> str(4) == str("4")
True
>>> repr(4) == repr("4")
False

>>> import datetime
>>> d = datetime.datetime.now()
>>> str(d)
'2020-04-04 20:47:46.525245'
>>> repr(d)
'datetime.datetime(2020, 4, 4, 20, 47, 46, 525245)'
>>> 
```



## python 常见函数整理

### isinstance(m, type)

Tyoe: 选择object类型，可能是`Iteration`, `DataFrame` e.g.

`return Bool`

### zip()

它将两个或多个数据集 “压缩” 到一起。这将返回一个包含从数据集衍生出来的成对项目的对象。它按照索引的顺序对这些项目进行分组。 `zip(dataSet1, dataSet2, ...)`

```python
names = ("John", "Jane", "Jade")
ages = (2, 4, 6)

zipped = zip(names, ages)

print(list(zipped))
# [('John', 2), ('Jane', 4), ('Jade', 6)]
```

### enumerate(iterable, start=0)

Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

### object.__dict__

它用于存储一个对象的命名空间（namespace），也就是该对象的属性和方法的字典。每个对象都有一个__dict__属性，它允许你访问和操作对象的属性和方法。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

# 查看对象的属性字典
print(person.__dict__)  # 输出: {'name': 'Alice', 'age': 30}

# 修改对象的属性
person.__dict__['name'] = "Bob"
print(person.name)  # 输出: Bob

# 添加新属性
person.__dict__['city'] = "New York"
print(person.city)  # 输出: New York

```


## Matplotlib
### Cartopy
ax.text:

```python
ax.text(long,lat,"✈" ,rotation =  orient, fontsize = 35*avion.normalize_speed(), transform=ccrs.Geodetic())

ax.text(x, y, s, fontdict, fontsize, color, verticalalignment, horizontalalignment, bbox, transform,
rotation, alpha, clip_on, linespacing, path_effects, backgroundcolor)
```
参数选择：

x 和 y：文本的 x 和 y 坐标位置。
s：要显示的文本内容。
fontdict：一个包含字体属性的字典，用于自定义文本的字体。
fontsize：文本的字体大小。
color：文本的颜色。
verticalalignment：文本垂直对齐方式，可选值包括 'top'、'bottom'、'center' 等。
horizontalalignment：文本水平对齐方式，可选值包括 'left'、'right'、'center' 等。
bbox：一个包含文本背景框属性的字典。
transform：指定坐标系的参数，用于确定文本坐标的参考坐标系。
rotation：文本的旋转角度。
alpha：文本的透明度。
clip_on：指定是否对文本进行剪切，以防止在图形外部显示。
linespacing：文本行间距。
path_effects：用于添加文本效果的参数。
backgroundcolor：文本背景颜色。

示例：
```python
import matplotlib.pyplot as plt
import cartopy.crs as ccrs  # 如果加上transform就需要

# 创建一个图形和坐标轴
fig, ax = plt.subplots()

# 设置文本坐标和内容
x = 0.5
y = 0.5
text = "Hello, Matplotlib!"

# 自定义文本属性
fontdict = {
    'family': 'serif',
    'color': 'blue',
    'size': 16,
}

# 添加文本标签到图形
ax.text(x, y, text, fontdict=fontdict, rotation=30, bbox=dict(facecolor='yellow', alpha=0.5))

# 设置坐标轴范围
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# 显示图形
plt.show()
```

## 魔术命令

### %load_ext autoreload 和 %autoreload 2

在Python中，%load_ext autoreload 和 %autoreload 2 是IPython魔术命令，用于自动重新加载（autoreload）已导入的模块，以便在代码发生更改时更新它们，而不需要重新启动Python解释器。

在Jupyter Notebook或IPython中，通常你需要在执行模块之前设置%load_ext autoreload和%autoreload 2，以确保自动重新加载已导入的模块。这是因为这些魔术命令将影响后续的代码执行，以便在模块发生更改时立即生效。

所以，按照以下顺序：

在Jupyter Notebook中打开或创建一个笔记本。

在笔记本的第一个单元格中输入以下命令：

```python
%load_ext autoreload
%autoreload 2
```


### time计时
`%%time`：记录一次执行花费时间
或者：
```python
import time
t1 = time.time()
...
t2 = time.time()
dt = t2 - t1
```

`%%timeit` 使用Python的timeit模块，它将会执行一个语句1000 000次(默认情况下)，然后给出运行最快3次的平均值


cpu 的运行机制：cpu是多任务的，例如在多进程的执行过程中，一段时间内会有对各进程被处理。一个进程从从开始到结束其实是在这期间的一些列时间片断上断断续续执行的。所以这就引出了程序执行的cpu时间（该程序单纯在cpu上运行所需时间）和墙上时钟wall time。

`time.time()`是统计的wall time(即墙上时钟)，也就是系统时钟的时间戳（1970纪元后经过的浮点秒数）。所以两次调用的时间差即为系统经过的总时间。

`time.clock()`是统计cpu时间 的工具，这在统计某一程序或函数的执行速度最为合适。两次调用`time.clock()`函数的插值即为程序运行的cpu时间。


## Pandas运用

### ==读取文件：==

1. 对于`dat`文件：  `AA_daily = pd.read_pickle("data/flights20220613/AA_daily.dat")`
   
2. 对于`csv`：`aircraft = pd.read_csv("data/flights20220613/aircraftDatabase-2022-06.csv")`

```python
import pandas as pd

# 读取CSV文件，跳过第一行作为标题，将"Date"列解析为日期，指定"ID"列为索引
df = pd.read_csv("data.csv", skiprows=1, parse_dates=['Date'], index_col='ID', sep=';', na_values=['N/A', 'NULL'], encoding='latin1')

# 选择要读取的列
selected_columns = ['ID', 'Date', 'Value']
df = df[selected_columns]

# 显示前几行数据
print(df.head())

```
skiprows=1：跳过第一行作为标题。
parse_dates=['Date']：将"Date"列解析为日期时间列。
index_col='ID'：将"ID"列指定为DataFrame的索引列。
sep=';'：指定分隔符为分号。
na_values=['N/A', 'NULL']：指定哪些值应该被视为缺失值。
encoding='latin1'：指定文件编码为Latin-1编码。
selected_columns：选择要读取的列，只保留了 'ID', 'Date', 'Value' 列。


### ==Pandas时间戳的转换：==

`AA_daily['time'] = pd.to_datetime(AA_daily['time'], unit='s')`的目的是将名为AA_daily的DataFrame中的某一列，通常是一个时间戳，从Unix时间戳（以秒为单位）转换为Pandas的datetime对象。

参数 `unit='s'` 中的 `'s'` 表示时间戳的单位是秒。Unix时间戳是一个整数，表示自1970年1月1日以来的秒数。通过指定`unit='s'`，你告诉`Pandas`将时间戳解释为秒数，然后将其转换为`datetime`对象，以便进行更多的日期和时间操作。这可以帮助你以更容易理解的方式处理时间数据。

```python
# 求最小最大时间段
initial_date = min(AA_daily['time'])
final_date   = max(AA_daily['time'])
```

### ==获取dataframe信息：==
```python
AA_daily.head(5)

AA_daily.info()
# 这个方法用于获取DataFrame的基本信息，包括列数、列名、非空值的数量、每列的数据类型等。
# 它通常用于检查数据的完整性，查看是否存在缺失值以及数据类型是否正确。
AA_daily.describe()
# 这个方法用于生成DataFrame中数值列的统计摘要。
# 它提供了关于这些数值列的统计信息，如均值、标准差、最小值、最大值等。
# 这对于了解数据的分布和大致特征非常有用。
```

### ==求值的方法==

#### 求某一列某一行信息

`.loc` 是Pandas DataFrame对象的索引器（indexer）之一，用于基于标签（label）来选择行和列。.loc 主要用于**标签索引**，而不是位置索引。

`.iloc` 是另一个用于`Pandas DataFrame`对象的索引器（indexer）。与 `.loc` 不同，`.iloc` 主要用于基于位置的整数索引来选择行和列，而不是标签。

`.iloc` 适用于那些使用整数位置来选择数据的情况，它不考虑行和列的标签，只关注它们在`DataFrame`中的位置。位置索引从`0`开始。

```python
# 某一列
pd['data']
# 所有列
df.columns
planes.columns = ['time', 'icao24', 'latitude', 'longitude', 'velocity', 'heading', 'callsign',
       'onground', 'geo_altitude']
# 选择单行
df.loc['row_label']

# 选择多行
df.loc['row_label1':'row_label2']

# 选择单列
df.loc[:, 'column_label']

# 选择多列
df.loc[:, ['column_label1', 'column_label2']]


# 选择单行
df.iloc[1]

# 选择多行
df.iloc[1:4]

# 选择单列
df.iloc[:, 2]

# 选择多列
df.iloc[:, [0, 2]]

aircraft_data_new = aircraft_data[['icao24','registration','operator','model','manufacturername']]
# 双[[]]代表列

```


#### 平均值
```python
AA_daily['velocity'].mean().round()
```
`round()`: 四舍五入的；转为浮点型：`.float()`



#### 时间的操作

Pandas的`.dt` 属性提供了许多操作，用于处理日期时间数据的各个方面。以下是一些常用的.dt 操作：

`.dt.year`：提取日期时间对象的年份部分。
`.dt.month`：提取日期时间对象的月份部分。
`.dt.day`：提取日期时间对象的日期部分。
`.dt.hour`：提取日期时间对象的小时部分。
`.dt.minute`：提取日期时间对象的分钟部分。
`.dt.second`：提取日期时间对象的秒部分。
`.dt.microsecond`：提取日期时间对象的微秒部分。
`.dt.date`：提取日期部分，即年、月和日，返回一个新的日期时间对象。
`.dt.time`：提取时间部分，即小时、分钟、秒和微秒，返回一个新的时间对象。
`.dt.day_name()`：获取日期对应的星期几的名称。
`.dt.dayofweek`：获取星期几，其中星期一为0，星期日为6。
`.dt.quarter`：获取日期所在季度。
`.dt.is_month_start`：检查日期是否是月的第一天。
`.dt.is_month_end`：检查日期是否是月的最后一天。
`.dt.is_year_start`：检查日期是否是年的第一天。
`.dt.is_year_end`：检查日期是否是年的最后一天。


#### 对数据的操作

`nb_flights_times[0:-1]`: 不包括倒数第一，直到倒数第二
`nb_flights_times[0:]`：包括倒数第一
`.Series` 是Pandas库中的一种数据结构，它代表一维数组（或列），可以存储各种数据类型，类似于Python的列表，但具有更丰富的功能和灵活性。Pandas Series 是DataFrame的构建块之一，DataFrame 是一种二维数据结构，可以看作是由多个Series组成的。

`.to_numpy()` 是Pandas DataFrame 和 Series 对象的一个方法，用于将其数据转换为NumPy数组。

```python
AA_daily_hour.drop_duplicates()  # 这是一个用于删除重复行的方法。基于所有行 ？
# 只想根据 "time" 列来删除重复行
AA_daily_hour.drop_duplicates(subset=['time'])
```

`.value_counts()` 是Series对象的一个方法，用于计算每个不同值的出现次数。它会返回一个包含唯一值和它们的计数的新Series，其中索引是唯一值，值是它们的出现次数。

```python
models = aircraft_data['model'].value_counts()
print("Types d'appareil le plus présentes :")
print(models[0:5])
```
Types d'appareil le plus présentes :
model
PA-28-140    3485
SR22         3295
PA-28-180    3042
172M         2985
172N         2774
Name: count, dtype: int64


`tolist()` 是Pandas和NumPy中常见的方法，用于将数据转换为Python列表（list）的形式。这在将数据从Pandas或NumPy数组提取为标准Python数据类型时非常有用。


==表格融合===
```python
concat = pd.merge(aircraft_data_new,AA_daily,on = 'icao24')
```

left：要合并的左侧DataFrame。

right：要合并的右侧DataFrame。

how：指定合并的方式，常见的选项包括：

'inner'（默认值）：内连接，保留两个DataFrame中都存在的行。
'outer'：外连接，保留所有行，缺失的值填充为NaN。
'left'：左连接，保留左侧DataFrame的所有行。
'right'：右连接，保留右侧DataFrame的所有行。
on：用于指定连接的列或列名。可以是一个列名的字符串，或多个列名组成的列表。

left_on 和 right_on：用于指定左侧DataFrame和右侧DataFrame中连接的列，当两个DataFrame的连接列具有不同的名称时使用。

suffixes：如果两个DataFrame具有相同名称的列，用于添加后缀以区分这些列的元组。

left_index 和 right_index：如果为True，表示使用DataFrame的索引作为连接键，而不是列。

sort：如果为True（默认值），则根据连接键进行排序。可以提高合并性能。

copy：如果为False，避免复制数据。

indicator：如果为True，将添加一个特殊列 _merge，用于指示每行的合并来源。

validate：用于检查合并操作的有效性。常见的选项包括 "one_to_one"、"one_to_many"、"many_to_one"、"many_to_many"。


==表格数据提取==

```python
one_plane = concat[concat['icao24'] == 'a7eff7'].reset_index(drop=True)
```
[concat['icao24'] == 'a7eff7'] 是一个条件索引，它选择了DataFrame中 'icao24' 列值等于 'a7eff7' 的行。这将创建一个新的DataFrame，其中只包含 'icao24' 列为 'a7eff7' 的行。

`.reset_index(drop=True)` 是一个操作，它将新DataFrame的索引重置为默认的整数索引，并丢弃旧索引。drop=True 参数用于删除旧的索引列，以避免在新DataFrame中出现重复的索引列。

所以，one_plane 是一个新的DataFrame，它包含了所有 'icao24' 列值为 'a7eff7' 的行，并且具有默认的整数索引。这可以用于从大型DataFrame中提取特定条件下的子集数据。

==表格聚合==

`df.groupby() `是Pandas库中的一个功能强大的方法，它用于对DataFrame对象进行分组和聚合操作。当你需要按某些列的值将数据分成不同组，然后对每个组执行汇总、统计或其他操作时，groupby() 非常有用。

```python
grouped = df.groupby('column_name')
result = grouped.mean()  # 以 'column_name' 列的值进行分组并计算每组的平均值
```

### 画图操作

```python
plt.bar(hours, planes_per_hour) 
# 是一个用于创建柱状图的Matplotlib代码。这行代码的目的是使用Matplotlib库绘制一个柱状图，
# 其中包括不同小时内飞机数量的数据。
```


