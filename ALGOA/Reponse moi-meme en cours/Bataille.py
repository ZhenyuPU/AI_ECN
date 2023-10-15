'''

'''

def Bataille(L1: list, L2: list):
    # la condition de la fin
    if not L1:
        print(f"L1 perd et L2 gagne")
        return
    elif not L2:
        print(f"L1 gagne et L2 perd")
        return
    elif not (L1 and L2):
        print(f"Egalite")
    
    L1_carte = L1.pop(0)
    L2_carte = L2.pop(0)

    
    if L1_carte > L2_carte:
        L1.append(L1_carte)
        L1.append(L2_carte)
    elif L1_carte < L2_carte:
        L2.append(L2_carte)
        L2.append(L1_carte)
    
    Bataille(L1, L2)

import random

L1 = [random.randint(1, 26) for _ in range(26)]
L2 = [random.randint(1, 26) for _ in range(26)]

Bataille(L1, L2)
