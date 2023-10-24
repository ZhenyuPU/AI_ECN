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


if __name__ == '__main__':
    L = SimpleList()
    L.insert_front(value=1)
    for i in range(10):
        L.append_(value=i)
    L.insert(pos=5, x=100)
    alist = L.travel()
    print(alist)


    node = Node(2)
    # node.n.n = Node(5)
    # node2 = node.n
    # nodenew = node2.n
    # nodenewnew = Node(10)
    # node2.n = nodenewnew
    # nodenew.n = node.n
    # print(node.d)
    # print(nodenew.n.n.d)
    nodenew = node
    node.d = None
    print(nodenew.d)



    # print_(L._head)
    # print(L.search(111))
    # L.delete(x=7)
    # print(id(cur) == id(L._head))
    # for _ in range(5):
    #     cur = cur.n
    # insert(cur, x=55)
    # cur = L._head
    # L.print_(cur)
    # print(id(cur) == id(L._head))
    # L.print_(L._head)

    # L.print_(L._head)
    # print(L._head.d)