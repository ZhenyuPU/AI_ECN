"""
增加扩容函数: extend()

增加size(键值对数量----增加的)，哈希表容量capacity，扩容倍数: extend_ratio
哈希表数组用capacit创建
"""



class Node:
    def __init__(self, value):
        self.v = value
        self.n = None

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

def list_del(l, x):
    if l is None:
        return None
    if l.n.v == x:
        return l.n.n
    l.n = list_del(l.n, x)
    return l

def print_(l):
    if l is None:
        print('None for the list')
        return
    values = []
    while l:
        values.append(l.v)
        l = l.n
    print('->'.join(map(str, values)))
    return


table_size = 10
T = [None] * table_size

print(T)

for i in range(30):
    ht_insert(T, x = i)

for item in T:
    print_(item)



