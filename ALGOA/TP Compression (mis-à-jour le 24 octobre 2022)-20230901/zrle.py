

import math

zrle_one = 257
zrle_two = 258


def bijective(n):
    q0 = n
    q1 = math.ceil(q0 / 2) - 1
    a = []
    while q1 > 0:
        a.append(q0 - 2 * q1)
        q1 = math.ceil(q0 / 2) - 1
    return a


def zrle_encode(text):
    # eliminer les sequences de 0 dans le texte
    # trouver le longeur de sequence
    # remplace par la numeration bijective de base 2 (1, 2)
    t = []
    for i in range(len(text)):
        fin = False
        longeur = 0
        if text[i] == 0:
            longeur += 1
            fin = True
        # if fin is True, ne pas ajouter juste continuer la boulce.
        if not fin:
            if longeur == 0:
                t.append(text[i])
                continue
            elif longeur > 0:
                b = bijective(longeur)
                # ajouter b dans le tableau
                for j in b:
                    t.append(j)
    return t


def zrle_decode(codes):
    



