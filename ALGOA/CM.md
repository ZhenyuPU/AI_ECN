# CM1

## Invariant de boucle:

Invariants de boucles (Loop Invariants) :

Les invariants de boucle sont **des assertions logiques** qui sont vraies **avant et après chaque itération** d'une boucle dans un programme. Ils servent à `<mark>`garantir que le comportement de la boucle est correct`</mark>` et qu'elle **termine correctement**. Les invariants de boucle sont généralement prouvés mathématiquement pour chaque boucle d'un programme.

initial: 循环开始前该变量为真
itération：循环过程不断迭代，变量值更改，但是性质保持不变
fini：循环终止，该变量能够判断结果是否为真

Il s'agit de déterminer quelle expression est utilisée pour définir le début, la progression et la fin de la boucle.

循环不变式：在循环过程中，迭代前这个式子保持为真，下一次迭代前仍然为真，终止时便可以说明结果为真。

比如：插入排序中，子数列A[1,..., n-1]已经排序好，对于初始A[0]为真，排序好；迭代中，下一次前为真；终止时j=n+1，然后A[1,...,n]为(A[j-1])，已经排序好，证明算法正确

这些循环不变式帮助确保循环的正确性，因为它们描述了每次迭代后程序应该满足的条件。在循环结束时，这些条件应该保持为真。这对于验证算法的正确性非常有帮助。不过，请注意，为了确保这些循环不变式的正确性，还需要进行适当的数学证明。

precondition: assumer au début quelle condition est vraie

postcondition: guarantir à la fin la correction du résultat

```python

def sort (A, n):
  for i = 1 to n − 1:
    insert ( i , A)
# assumer x dans [1, n-1]
def insert (x, A):
    key = A[x]
    j = x − 1
    while j ≥ 0 and A[j] > key:
        [j + 1] = A[j]
        j = j − 1
    A[j+1] = key
```

## indécidable

### PCP问题：不可判定(indécidable)

**停机问题(Problème de l'arrêt)**

```C++
bool halts(char *f_code, char *t);

void modified_halts(char *f_code) {
  if (halts(f_code, f_code)) {  // 当halts(f_code, f_code)返回true
    while (true) { /*empty*/ }  // 死循环
  }
  else {                        // 当halts(f_code, f_code)返回false
    return;                     // 立即停止运行
  }
}

```

其中f_code是我们要进行测试的函数f的ASCII源代码, 我们可以认为对f_code进行编译得到了函数f.

当f对t停机时, `halts(f_code, t)`返回true; 当f对t不停机, `halts(f_code, t)`返回false. 反过来我们可以说，`halts(f_code, t)`返回true，f对t停机;  `halts(f_code, t)`返回false，f对t不停机。

假设 `modified_halts`这个函数的ASCII源代码是 `modified_halts_code``, 如果我们把`modified_halts_code `作为`modified_halts`的输入会是什么情况?

如果 `modified_halts`对 `modified_halts_code`停机, 说明 `halts(modified_halts_code, modified_halts_code)`返回false(针对 `modified_halts`函数而言), 然而 `halts(f_code, f_code)`为false说明 `modified_halts`对 `modified_halts_code`不停机;

如果 `modified_halts`对 `modified_halts_code`不停机, 说明 `halts(modified_halts_code, modified_halts_code)`返回true, 然而 `halts(f_code, f_code)`为true说明 `modified_halts`对 `modified_halts_code`停机.

综合以上两种情况, "`modified_halts`对 `modified_halts_code`停机"当且仅当"`modified_halts`对 `modified_halts_code`不停机", 这是一个矛盾, 说明不存在这样一个halts函数可用于判断任意函数的可停机性.

Le Théorème de Rice dit (informellement) que toute propriété non-triviale(非平凡) sur les programmes est indécidable："任何非平凡（non-trivial）的关于程序的性质都是不可判定的（undecidable）。"

"性质" 指的是一个关于程序行为的特征或特点，如程序是否会停止（停机问题）、程序是否会输出某个特定值、程序是否满足某种规范等。

"非平凡" 表示性质**不是对所有程序都成立或都不成立的情况**。也就是说，这个性质对于某些程序是真实的，而对于其他程序是假的。非平凡性质是有趣的性质，因为它们涉及到程序的不同行为。

"不可判定" 意味着无法编写一个通用算法来判断任何给定程序是否满足这个性质。换句话说，对于非平凡性质，没有一种方法可以对所有情况进行判定，存在一些情况下无法得出结论。

这个定理的要点是，对于许多有趣的、非平凡的程序性质，我们不能期望编写一个计算机程序来确定所有情况下是否成立。这些问题被称为不可判定的问题，**它们在计算理论和计算机科学中起着重要的作用，强调了计算机的局限性和复杂性**。

Par exemple, le 10e problème de Hilbert: "Décider si une éequation diophantienne (quelconque) a une solution";  Problème de correspondance de Post (PCP)

## Complexité

### La machine de Turing

Une machine déterministe à deux compteurs (M2C):

L'état initial est 1.

Tous les valeurs des compteurs sont initiallement 0.

• qui contient des symboles issus d'un alphabet fini A ;
• A contient un symbole spécial □ indiquant qu'une case est vide ;
• une tête de lecture cur ∈ Z désigne la case courante M[cur] ∈ A de la m´emoire ;
• M contient des données d'éntrée : un mot sur A \ {□} commençant à la case 0.

• un ´etat correspond `a une instruction sp´eciale accept qui arrˆete la machine et r´epond ≪ oui ≫ ; • un ´etat correspond `a une instruction sp´eciale reject qui arrˆete la machine et r´epond ≪ non ≫ ;
• la machine peut bloquer (deadlock) si la case courante ne correspond pas `a l’instruction courante.

![image1](https://cdn.staticaly.com/gh/ZhenyuPU/picx-images-hosting@master/20230910/image.1gklcxdewskg.webp)

![image2](https://cdn.staticaly.com/gh/ZhenyuPU/picx-images-hosting@master/20230910/image.7g5tkoezfjw0.webp)

![image](https://cdn.staticaly.com/gh/ZhenyuPU/picx-images-hosting@master/20231002/image.5gjjhvxw6tk0.webp)

La Complexité d’une machine de Turing:

1. Complexité temporelle : nombre d'instructions réalisées avant arrêt ;
2. Complexité spatiale : nombre maximal de cases non vides simultanément(同时地).
   x

#### Quelques classes de complexité des problèmes de décision

PTIME（P）：可以在多项式时间内解决的问题。这意味着问题的解决方案可以在输入规模n的多项式时间内找到，通常表示为O(n^k)。例如，线性规划中判断是否存在一个解就属于P类问题。

PSPACE：可以在多项式空间内解决的问题。这指的是问题的解决方案可以在多项式空间（相对于输入规模）内找到。例如，在类似Rush Hour或Sokoban的问题中，确定是否可以从一个状态过渡到另一个状态就属于PSPACE问题。

EXPTIME：可以在指数时间内解决的问题。这意味着问题的解决方案的运行时间以2^n的指数形式增长，其中n是输入规模。例如，在围棋中确定在给定的棋盘大小上第一个玩家是否能赢，就属于EXPTIME问题。

EXPSPACE：可以在指数空间内解决的问题。这指的是问题的解决方案需要指数级的存储空间。例如，在比较两个简单正则表达式（如(a∗b∗ + c)∗和(a + b + c)∗）是否具有相同的语言时，这就是一个EXPSPACE问题。

![image3](https://cdn.staticaly.com/gh/ZhenyuPU/picx-images-hosting@master/20230910/image.5et0lxcag3g0.webp)

### problème de NP, SAT, ILP

SAT是指给定一个逻辑表达式，我们可以让其值为true。合取范式：由交连接的子句。
![image4](https://cdn.staticaly.com/gh/ZhenyuPU/picx-images-hosting@master/20230910/image.96ycn7pvopc.webp)

k-SAT: k指的是每个子句中包含k个文字
SAT属于NP-compete问题

### Complexité moyenne : variables aléatoires indicatrices

![image5](https://cdn.staticaly.com/gh/ZhenyuPU/picx-images-hosting@master/20230910/image.2bxkxq77olj4.webp)

$ X = \sum_{2}^{n-1} X_i $

## Algorithmes Probalistes

Ce qui utilise une source de hasard. Plus précisément le déroulement de l’algorithme fait appel à des données tirées au hasard.

Un algorithme est dit probabiliste si son comportement dépend à la fois des données du problème et de valeurs produites par un générateur de nombres aléatoires.

Par exemple, Monte Carlo, Las Vegas et Atlantic City

* Monte Carlo

```python
import random

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return 4 * inside_circle / num_samples
    # 为了求pi，这里采用的是单位圆面积与正方形比值方式

num_samples = 1000000
estimated_pi = monte_carlo_pi(num_samples)
print(f"Estimated Pi: {estimated_pi}")

```

* Las Vegas
  Donne toujours un résultat exact, mais le temps de calcul est petit avec une très forte probabilité.

```python
# 随机排序一个列表
import random

def las_vegas_shuffle(arr):
    while True:
        shuffled = random.sample(arr, len(arr))
        if shuffled != arr:
            return shuffled

my_list = [1, 2, 3, 4, 5]
shuffled_list = las_vegas_shuffle(my_list)
print("Shuffled List:", shuffled_list)

```

* Atlantic City

Donne une réponse avec une très forte probabilité sur l'exactitude de la réponse pour un temps de calcul faible en moyenne probabiliste.

#### Classes de complexité des algorithmes probabilistes

![image6](https://cdn.staticaly.com/gh/ZhenyuPU/picx-images-hosting@master/20230910/image.2foo9r6ywsu8.webp)

# CM 2 Conception d'algorithme

Définition (Relaxation):

P'est `<mark>`une relaxation`</mark>` de P si toute solution de P est une solution de P'. On note P ⇒ P'

Relaxation = supprimer des contraintes

即P的解决方法是普适的，相对于P'而言。P的限制条件更多,更复杂，我们需要通过简化问题得到简单条件下的解，从而得出P'是他的松弛(Relaxation)

## Enumération exhaustive

On considère une relaxation P′ du problème P ;
On énumère ces solutions jusqu’à trouver une solution de P ;

![image7](https://cdn.staticaly.com/gh/ZhenyuPU/picx-images-hosting@master/20230913/image.3nrtcv1ix2s0.webp)

```python
# T 是一个布尔值列表，用于跟踪数字是否已经被使用。
# T 的目的是记录从 1 到 n 的数字哪些已经在构建拉丁方阵的过
# 程中被使用了，以确保每个数字只被使用一次。
def carre(C, T, k, n):   # C是存放矩阵数值， k是判定到哪一步了，是否在维度内， n是矩阵维度n*n
    if k == n * n:       # 判定是否填完所有空格
        return C

    for i in range(1, n^2):
        if not T[i]:
            T[i] = True
            C[k // n][k % n] = i    # k//n表示row，k%n是colomn
            result = carre(C, T, k + 1, n)
            if result:
                return result
            T[i] = False

    return None  # 如果没有找到解，则返回 None

n = 4  # 您可以将 'n' 更改为所需的拉丁方阵大小。
C = [[0] * n for _ in range(n)]  # 使用零初始化拉丁方阵网格。
T = [False] * (n^2)  # 初始化用于跟踪已使用数字的列表。

latin_square = carre(C, T, 0, n)
if latin_square:
    for row in latin_square:
        print(row)
else:
    print("未找到给定 'n' 的拉丁方阵。")

```

## Backtracking

## Diviser pour régner

## Programmation dynamique

## Algorithmes gloutons

## Transformations de problèmes

## Structure de Données

```
x = 2;
&x = adresse;
p -> x;
p = adresse;
*p est une variable dont l'adresse est dans p
```

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231004/image.2gmua84vzwbo.webp)

上述描述提到了关于计算均摊成本的一种方法，使用了一个称为 "函数势"（potential function）的概念。下面我将详细解释这个方法：

函数势（Potential Function）：这是一个函数 ϕ，它接受系统状态的配置向量⃗v作为输入，并返回一个实数值。它用来表示系统状态的某种度量或 "势"，可以视为一种潜在的能量。这个函数的选择是关键的，因为它决定了如何为每个操作分配均摊成本。

均摊成本（Amortized Cost）：对于一系列的操作（例如，i1, i2, ..., in），每个操作都有一个实际成本（ck，例如，执行时间），以及一个与函数势相关的潜在成本（ϕ(⃗vk) - ϕ(⃗vk-1)）。

Potentiel Function的变化：对于每个操作ik，它的潜在成本pk是实际成本ck和函数势ϕ(⃗vk)与ϕ(⃗vk-1)之差的和。这意味着我们在执行操作时，不仅要考虑实际成本，还要考虑函数势的变化。

均摊成本与总成本关系：均摊成本是一系列操作的平均成本。通过选择适当的函数势，我们可以确保均摊成本的总和不会超过实际成本的总和。具体地，如果 ϕ(⃗vn) ≥ ϕ(⃗v0)，则可以保证：

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231004/image.988flcnxf1w.webp)

均摊成本总和不超过实际成本总和

这意味着我们可以为某些操作付出更高的成本，但总体上，均摊成本不会超过实际成本。这有助于分析数据结构和算法的性能，尤其在涉及动态数组或队列等数据结构时，均摊分析是一种有用的工具。

需要注意的是，选择适当的函数势对于正确的均摊分析至关重要，因为它决定了如何分配潜在成本。不同的函数势可以导致不同的分析结果，因此选择合适的函数势需要一定的洞察力和分析技巧。

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231004/image.eeq3p8fnmi0.webp)

### Liste Chainée

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231004/image.546oiuka5w80.webp)
