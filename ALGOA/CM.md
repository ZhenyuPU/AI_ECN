# ALGOA

## Invariant de boucle:

Invariants de boucles (Loop Invariants) :

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


## La machine de Turing

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


La Complexité d’une machine de Turing:

1. Complexité temporelle : nombre d'instructions réalisées avant arrêt ;
2. Complexité spatiale : nombre maximal de cases non vides simultanément(同时地).

## Complexité

排序算法复杂度分析：
![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231015/image.6htb6i96q0k0.webp)

冒泡、选择、直接排序需要两个for循环，每次只关注一个元素，平均时间复杂度为O(n²)）（一遍找元素O(n)，一遍找位置O(n)）

快速、归并、希尔、堆基于二分思想，log以2为底，平均时间复杂度为O(nlogn)（一遍找元素O(n)，一遍找位置O(logn)）

稳定性记忆-“快希选堆”（快牺牲稳定性） 

排序算法的稳定性：排序前后相同元素的相对位置不变，则称排序算法是稳定的；否则排序算法是不稳定的。

### Quelques classes de complexité des problèmes de décision

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


### La Complexité de Amorti


#### Classes de complexité des algorithmes probabilistes

![image6](https://cdn.staticaly.com/gh/ZhenyuPU/picx-images-hosting@master/20230910/image.2foo9r6ywsu8.webp)



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


## Structure de Données

### 存储
大端序存储方式（Big-Endian）是一种将多字节数据的最高有效字节（MSB）存储在内存地址最低的存储方式，也就是字节序的高位字节在前，低位字节在后。这与我们的阅读习惯相似，比如一个十进制数1234，我们从左到右阅读，高位在前，低位在后。

例如，一个32位的整数0x12345678，在大端序存储方式下，会被存储在内存中如下：

内存地址：0x00 0x01 0x02 0x03
存储内容：0x12 0x34 0x56 0x78

其中，0x12是最高有效字节，被存储在内存地址最低的位置（0x00），而0x78是最低有效字节，被存储在内存地址最高的位置（0x03）。

```
x = 2;
&x = adresse;
p -> x;
p = adresse;
*p est une variable dont l'adresse est dans p
```

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231004/image.2gmua84vzwbo.webp)



### Liste Chainée

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231004/image.546oiuka5w80.webp)

Chaque cellule C contient la donnée C.d et un pointeur vers la cellule suivante C.n

accès: O(n)
insertion/suppression: O(n)
insertion/suppression avec pointeur: O(1)

Le début de la liste est un pointeur vers la première cellule

```python
cur = self._head
while cur.n is not None:
    cur = cur.n
cur.n = new_node
```

cur 是一个指向链表头的指针，而 self._head 也指向链表头。当你执行 cur = self._head 时，实际上是将 cur 设置为指向与 self._head 相同的节点，即链表的头节点。**地址都是一样的！**

然后，你使用 while 循环遍历链表，==移动 cur 到链表的最后一个节点==，即倒数第二个位置。在循环结束时，cur 指向了链表中最后一个节点，而 self._head 仍然指向链表的头节点。这里是移动指针指向，地址仍然是原链表的各节点地址，而不会产生新的。

当你执行 cur.n = new_node 时，你实际上是将链表的最后一个节点的 n 属性（指向下一个节点的指针）设置为新节点 new_node。这会使链表的最后一个节点指向新节点，因此新节点成为了链表的最后一个节点。

但是，self._head 仍然指向链表的头节点，它没有发生变化。所以，self._head 仍然指向链表的头部，而 cur 指向链表的最后一个节点。

在 Python 中，链表通常由头指针（self._head）来引领整个链表的访问，而 cur 只是一个临时指针，用于遍历链表，不会影响头指针的位置。

```python
class Node:
   def __init__(self, value):
        self.d = value
        self.n = None

class SimpleList:
    def __init__(self):
        self._head = None
    # creer une liste self._head
    def insert_front(self, value):
        NewNode = Node(value)
        NewNode.n = self._head
        self._head = NewNode
  
    def append_(self, value):
        new_node = Node(value)
        if self._head is None:
            self._head = new_node          # pointer vers une nouvelle cellule
            return
        cur = self._head
        while cur.n is not None:
            cur = cur.n
        cur.n = new_node
        return

    def travel(self) -> list:
        liste = []
        cur = self._head
        while cur is not None:
            liste.append(cur.d)
            cur = cur.n
        return liste
  
    # ajouter au debut ce qui est l'insertion de l’´el´ement x apr`es la cellule point´ee par L
    # consigner un emplacement
    # L est une liste ce qui est head._head non head
    def insert(self, pos, x):
        cur = self._head
        # deplacer jusqu'a pos
        for _ in range(pos-1):
            cur = cur.n
        # créer une nouvelle cellule
        L_new = Node(x)
        L_new.n = cur.n
        cur.n = L_new

    def delete(self, x):
        cur = self._head
        # deplacer
        while cur.n.d != x:
            cur = cur.n
        # delete
        cur.n = cur.n.n
  
    def search(self, item) -> bool:
        cur = self._head
        while cur is not None:
            if cur.d == item:
                return True
            cur = cur.n
        return False

def print_(L):
    if L is not None:
        print(L.d)
        print_(L.n)
```

### Listes doublement chainée

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231010/image.5r62o7vf6xg0.webp)

```python
# Creer une liste doublement chainee
class Double_List:
  def __init__(self, item):
    self.d = item
    self.prev = None
    self.n = None
  
  def is_empty():
    return self.d == None or self.n ==None
  
  def insert_after(x, L):
    L_x = Double_List(x)
    if L.n == None:
      L.n = L_x.prev
      L_x.n = None
      return
    insert_after(x, L.n)
  
  def insert_before(x, L):
    L_x = Double_List(x)
    L_x.n = L.n
    L = L_x
  
  def delete_end(fin, L):

```

==**"Accéder à la fin d'une liste simplement chaînée en O(1) : ajouter juste un pointeur"**==

在普通的单链表中，要访问链表的末尾，你需要从链表的头部开始遍历链表，直到达到最后一个节点。这样的操作的时间复杂度是线性的，即O(n)，其中n是链表的长度。

然而，如果你在链表中添加一个额外的指针，指向链表的末尾节点，那么你可以直接通过这个指针访问链表的末尾，而不需要遍历整个链表。这样，你可以在常数时间复杂度内访问链表的末尾，因为你可以直接跳到末尾节点，而不需要遍历。

这个方法的实现非常简单：每当你在链表中添加一个新节点时，同时更新这个指向链表末尾的指针，以保持它指向新的末尾节点。这样，你就可以随时以O(1)的时间复杂度访问链表的末尾。

这种技巧对于需要频繁访问链表末尾的应用程序非常有用，因为它可以显著提高访问效率。

### Files et piles

File: First in First Out(FIFO)

Pile: Last in First Out(LIFO)

Opération:

• insérer / empiler (enqueue / push)
• supprimer / dépiler (dequeue / pop)
• prochain élément / dessus de pile (next / top)
• vide

不理解
![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231015/image.7gsykwwxc8o0.webp)

### Files de priorité

• Toujours sortir le plus petit élément de la file
ex. plus courts chemins, arbres couvrants, codage de Huffman, qualité de service, etc.

• On peut trier la file (typiquement) O(n log2 n)) mais il faut recommencer à chaque insertion (O(n)) ;

• Pour faire mieux : passer de la liste/tableau à l’arbre.

#### L'arbre

• La hauteur de l’arbre est la longueur du plus long chemin de la racine à une feuille (ici 4).
• Un arbre est équilibré en hauteur si les hauteurs de ses sous-arbre diffèrent d’au plus 1 ;
• Un arbre n-aire équilibré avec m nœuds a une hauteur d’au plus $log_n m$;
• On construit une structure avec des op´erations en O(hauteur).

#### Tas binaire

Un tas binaire (binary heap) est un arbre binaire tel que :

1. seul le dernier niveau n’est pas rempli
   donc il est équilibré
2. dans chaque sous-arbre ==la racine est plus petite que les racines de ses sous-arbres==
   donc plus petite que tous les ´el´ements de ces sous-arbres

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231015/image.1w0mayn4j4g0.webp)

Pour une file de priorités, il nous faut trois opérations :

1. test du vide (trivial)
2. insertion d’un élément
3. extraction du minimum

##### Tas binaire : insertion

remonter à sa place.

```python

```

##### Tas binaire : extraction du minimum

1 Le minimum est la racine ;
2 On le remplace par le dernier ´el´ement de l’arbre
le plus `a droite dans le niveau le plus profond 3 On fait descendre cet ´el´ement `a sa place le cas ´ech´eant
on ´echange avec le plus petit successeur

##### Tas implicites

Si on a un acc`es en O(1) au parent et aux successeurs, insertion et extraction sont en O(log2 n) ;

En fait, le tas implicite est ==une liste==. Mais il **enregistre sa valeur de facon tas binaire**.

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231015/image.zp62w0n7a40.webp)

Pour un indice i donnée :   

1. indice du nœud parent : $\frac{i-1}{2}$
2. indice du nœud successeur (fils) gauche : 2i + 1 et droit : 2i + 2

个数上来看是，第j个的沿着方向过去的子节点是第2j个

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231015/image.5u0rsrxxhmw0.webp)


```python
def heap_insert(A, x, n):
  if n == len(A) - 1:
    raise ValueError('heap is full')
  else:
    A[n] = x   # n est l'indice
    n = n + 1   # nouveau n est le longueur
    heap_fix_up(A, n-1)

# i est l'indice de element
def heap_fix_up(A, i):
  p = (i - 1) // 2
  while p >= 0 and A[p] > A[i]:
    swap(A[p], A[i])
    i = p
    p = (i - 1) // 2
  
```

**==Delete==**

```python
def heap_del(A, x):
  n = len(A)
  index = A.index(x)
  A[index] = A[n-1])
  heap_fix_down(A, index, n)

def heap_fix_down(A, i, n):
  p = 2 * i + 1
  while p <= n:
    # seulement s'il y a un fils
    if A[p] and not A[p+1]:
      if A[i] > A[p]:
        swap(A[i], A[p])
      break
    elif not (A[p] and A[p+1]):
      break
    else:
      if A[i] > A[p] or A[i] > A[p+1]:
        swap(A[i], min(A[p], A[p+1]))
        i = p
        p = 2 * i + 1
```

#### Tri par tas (heapsort)

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231015/image.2ccn9zwiy0sg.webp)


==Lemme:==
Si A est un tas binaire implicite `a n ´el´ements alors les feuilles sont au indices ⌊n/2⌋ . . . (n − 1).

• on construit un tas **pour le maximum** au lieu du minimum
• chaque maximum extrait est **remis à la place du dernier élément** du tas qui l’a remplacé.
• **le coût est toujour**s $O(nlog_2n)$, mieux que merge sort qui nécessite un peu de mémoire supplémentaire et quick sort qui est en $O(n^2)$.

```python
def heatsort(A):
  for i in range(n // 2 - 1, -1, -1):
    # remettre la max a la place de debut
    heat_fix_down_max(A, i, n)
  
  for i in range(n-1, -1, -1):
    swap(A, 0, i)
    heap_fix_down_max(A, 0, i+1)

```
![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231015/image.e9zygq5duig.webp)

### Ensembles et tableaux associatifs

#### Arbres binaires de recherche (ABR)

Definition:

La racine du fils gauche plus petite que la racine

La racine du fils droite plus grande que la racine

```python
class BinaryTreeNode:
  def __init__(self, value=None):
    self.parent = None
    self.left = None
    self.right = None
    self.value = value
  
def abr_search(A, x)：
  if A == None:
    return False
  elif x == A.value:
    return True
  elif x < A.value:
    abr_search(A.left, x)
  elif x > A.parent:
    abr_search(A.right, x)


def abr_insert(A, x):
  if A == None:
    new_node = BinaryTreeNode(x)
    return new_node
  else:
    if x < A.value:
      abr_insert(A.left, x)
    elif x > A.value:
      abr_insert(A.right, x)
    return A

```

Pour supprimer le noeud N, il existe deux possibilités:

- Si le noeud N à supprimer a zéro ou un successeur, il juste faut remplacer *N par *Y(successeur sole) et supprimer Y.
- Sinon, il faut remplacer par Y plus grand que lui ou le plus grand le plus petit

```python
def abr_del(A, x):
  if A is None:
    return A

  if A.valeur == x:
    if A.left is None:
      return A.right
    elif A.right is None:
      return A.left

    A.value = find_min(A.right).value
    A.right = abr_del(A.right, A.value)
  elif x < A.value:
    abr_del(A.left, x)
  elif x > A.value:
    abr_del(A.right, x)
  return A


def find_min(A):
  if A is None:
    return A
  
  if not A.left:
    return A
  else:
    return find_min(A.left)

#  trouver le parent du nœud r´ealisant le minimum
def find_parent_min(A):
  if A is None:
    return None
  
  parent = None

  while A.left:
    parent = A
    A = A.left
  return parent
```


#### Arbre auto-equilibrant

自平衡二叉搜索树，它是一个二叉树，故满足二叉树的性质，并且它能够在插入或删除时自动保持平衡。

根据满足平衡条件的严格程度可以划分种类：

红黑树(Arbres rouges et noirs)，AVL

##### AVL

Un arbre AVL(Adelson-Velsky & Landis):

Pour tout noeud x, les **sous-arbre** enraciné en x est **équilibrant(en haut)**.

它是平衡二叉树，同一个节点的两个子树的高度差不超过1。 并且它的两个子树也是平衡二叉树。

高度为$O(long_2n)$.

##### AVL rotation

Pour équilibrer l'arbre il faut faire des rotations qui préserve l'invariant de l'ABR.

```python
# initial: (A, x, None, 0)
def avl_insert(A, x, p, bfu):
  retrace = (p != None)

  if A is None:
    new_node = AVL_node()
    new_node.value = x
    new_node.b = 0
  else:
    if x < A.value:
      A.left = avl_insert(A.left, x, A, -1)
    else:
      A.right = avl_insert(A.right, x, A, 1)
    
    B = avl_balance(A)
    if B.b == 0:
      retrace = False

  if retrace:
    p.b = p.b + bfu
  
  return B



def balance(A):
  R = A
  if A is not None:
    if A.b == 2:
      if A.right.b < 0:
        A.right = avl_rotate_right(A.right)
      
      R = avl_rotate_left(A)
    
    elif A.b = -2:
      if A.left.b > 0:
        A.left = avl_rotate_left(A.left)
      
      R = avl_rotate_right(A)
    
  return R
```


On peut aussi d´efinir des opérations efficaces $(O(n_1 log( n_1/n_2+ 1)))$ et parallélisables d’union intersection, diff´erence d'ensemble.

$$recherche: O(log_2 n)\\
insertion: O(log_2 n)\\
supression: O(log_2 n) \\$$

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231016/image.2kr85j1y64s0.webp)

Reponse:
```python

```


#### Tables de hachage

Pour **indiquer l'absence** d'un élément: Utiliser une **valeur spéciale**(Comme `None`)

Il équivaut à ==une liste==.

Insertion, suppression et recherche sont en $O(1)$

Chaque élément pointe vers l'indice.

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231016/image.20h467bao71c.webp)

Reponse:

```python

```
##### 链地址

哈希表加上链表：

T 表示一个哈希表，这是一个数组，每个元素是一个链表，访问某一个元素所在的位置需要我们用哈希函数获取索引。，这只能找到链表对应头指针的位置。要想找到元素需要在链表中寻炸。

![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231017/image.442k90h98pm0.webp)

L'opération de table de hachage

```python
def h(x, T):
    # hash(x),x = key
    return x % len(T)

def ht_search(T, x):
    return list_search(T[h(x, T)], x)   
    # h(x): 哈希函数找到x所在的索引i,然后通过list_search()函数找到T[i]这个链表和x所在的地方

def ht_insert(T, x):
    T[h(x, T)] = list_insert_front(T[h(x, T)], x)

def ht_del(T, x):
    list_del(T[h(x, T)], x)

def list_search(l, x):
    if l is None:
        return False

    if x == l.v:
        return True
    return list_search(l.n, x)

def list_insert_front(l, x):
    new_node = Node(x)
    if l is None:
        return new_node
    new_node.n = l
    return new_node
```
![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231017/image.2zixk0m99tu0.webp)

$$O(n), O(1), O(n)$$

##### Adresse ouverte

##### La complexité de Hachage  

Pire cas:

complexité moyenne:


![image](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231017/image.29b5kehzjt0k.webp)




## Trier
### Bubble



### Selection

### Quick sort

### Merge sort

### Counting sort
