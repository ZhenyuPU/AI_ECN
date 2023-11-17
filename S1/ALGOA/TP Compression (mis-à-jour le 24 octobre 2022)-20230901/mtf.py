

class ListNode:
    def __init__(self, symbol = None):
        self.symbol = symbol
        self.n = None
    
    def insert_front_node(self, l, node):
        node.n = l
        l = node
        return l
    
    def insert_front_symbol(self, l, x):
        new_node = ListNode(x)
        new_node.n = l
        l = new_node
        return l
    
    def delete_next(self, l):
        next = l.n.n
        l.n = next
        return l
    
    def find_npi(self, l, x):
        parent = ListNode()
        indice = 0
        while l.n.symbol != x and l.symbol != x:
            indice += 1
            parent = l
            l = l.n
        return (indice+1, parent.n)
    
    def find_np(self, l, indice):
        parent = ListNode()
        while indice > 0:
            parent = l
            l = l.n
            indice -= 1
        return (l.symbol, parent)
    
def mtf_encode(l, text):
    # text contient les symboles et on va choisir un des ceux puis chercher l'indice, 
    # ce qui consiste le code
    node = ListNode()
    codes = []
    for item in text:
        indice, parent= node.find_npi(l, item)
        # indice c'est l'indice de item
        new_node = ListNode(item)
        node.delete_next(parent)    # au debut on supprime le noeud
        node.insert_front_node(l, new_node) # puis mettre au debut
        codes.append(indice)    # ajouter le code

    return codes

def mtf_decode(codes, l):
    # on va commencer par la derniere valeur de codes
    # qui est l'indice de la derniere symbol
    text = []
    node = ListNode()
    n = len(codes)
    for i in range(n, -1, -1):
        indice = codes[i]   # c'est l'indice de la symbole qui necessite de bouger et maintenant il est au debut
        # petit a petit bouger
        j = 0
        alist = l.copy()
        symnol, parent = node.find_np(l, 0)
        text.insert(0, symbol)
        while indice > 0:
            indice -= 1
            j += 1
            symbol, parent = node.find_np(l, j)
            new_node = alist.n.n
            alist.n = parent
            parent.n = new_node
            alist = alist.n
        
    return text


        
    

            




    
    