'''
Transformee de Burrows-Wheeler

1. 移位操作

2. 计数排序和基数排序

3. 

'''
# fin de valeur
bwt_marker = 256
block_size = 500000

def get_element(t, n, T):
    return T[(t + n) % len(T)]

def counting_sort(T):
    # compter le nombre d'occurence d'un element
    counter = [0] * (bwt_marker + 1)
    for item in T:
        counter[ord(item)] += 1
    
    # l'indice est la valeur de T et le tri est fini
    # mettre les valeurs dans T
    new_table = []
    for i in range(bwt_marker + 1):
        if counter[i] != 0:
            for _ in range(counter[i]):
                new_table.append(chr(i))
    return new_table

def double_table_tri(T, n):
    # supposer que chaque tableau de tableaux contient plus de n elements
    # Choisir n^e element comme consigne
    # min_count = ord(max(T, key=lambda x: x[n-1]))
    # max_count = ord(min(T, key = lambda x: x[n-1]))
    '''
    quick sort to do it
    '''
    counter = [0] * (bwt_marker + 1)
    for i in range(len(T)):
        counter[ord(T[i][n-1])] += 1
    
    new_table = []
    for i in range(bwt_marker + 1):
        for _ in range(counter[i]):
            for item in T:
                if item[n-1] == chr(i) and n < len(item):
                    new_table.append(item)
                    
    return new_table

def sort_rotations(text, trier, n, start, end):
    # Créez une fonction pour extraire le nième symbole d'une rotation
    def get_nth_symbol(rotation, n):
        return text[(trier[rotation] + n) % len(text)]

    # Utilisez la fonction personnalisée comme clé de tri pour la fonction sorted
    sorted_rotations = sorted(range(len(trier)), key=lambda rotation: get_nth_symbol(rotation, n))

    # Triez les rotations en fonction de leur nième symbole
    sorted_text_rotations = [trier[i] for i in sorted_rotations]

    R = []

def rotation_sort():
    '''
    用上面的double_sort选定n=1，并且先通过get_element让
    '''

def radix_sort_rec(T, trier, n, start, end):
    if n < len(T):
        R = custom_sort_rotations(T, trier, n, start, end)
        for s, e in R:
            radix_sort_rec(T, trier, n + 1, s, e)
        

# derecursifier:
# def radix_sort(T):

def bwt_code(T, bs):
    R = []
    while T:
        txt = T[:bs]
        T = T[bs:]

        txt.append(bwt_marker)
        size = len(txt)
        trier = list(range(size))   # Attention list !
        s = 0
        e = size
        radix_sort_rec(txt, trier, n, s, e)

        R.extend()
        txt.pop()
    
    return R



def find_nth(T, n):
    dic = {}
    for item in T:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    for item in dic:
        if dic[item] == n:
            return item
    
    return -1


# 二分查找 ？
def find_rank(T, i):
    r = 0
    
    

        

if __name__ == '__main__':
    T = ['exemple', 'rotation', 'bonjour']
    # T = 'exemple'
    # print(double_table_tri(T, n=3))
    # Texte initial
    texte_initial = "banana"

    # Tableau des indices de début de chaque rotation
    tableau_trier = [1, 3, 0, 5, 2, 4]

    # Tri des rotations en fonction du 2ème symbole
    n = 2
    rotations_triees = custom_sort_rotations(texte_initial, tableau_trier, n)

    print(rotations_triees)

    #def rotation_text_sort(T):
    

