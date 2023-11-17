from copy import deepcopy
import numpy as np
from pulp import *

class Game:
    def __init__(self, m1, m2,):
        '''Crée un jeu à deux joueurs à partir des matrices de gain des deux joueurs'''
        # on transpose m2 de façon à ce que chaque joueur accède à sa matrice en étant
        # joueur ligne
        self.g = [m1, np.transpose(m2)]

    def delete_action(self, p, a):
        '''Supprime l'action a du joueur p'''
        if p == 0:
            self.g[0] = np.delete(self.g[0], a, axis = 0)
            self.g[1] = np.delete(self.g[1], a, axis = 1)
        else:
            self.g[0] = np.delete(self.g[0], a, axis = 1)
            self.g[1] = np.delete(self.g[1], a, axis = 0)

    def n_actions(self, p):
        '''Nombre d'actions du joueur p. On suppose que chaque joueur a toujours au moins une action'''
        return len(self.g[p])

    def print(self):
        '''Affiche la bimatrice'''
        for i in range(self.n_actions(0)):
            print('|', end = ' ')
            for j in range(self.n_actions(1)):
                print(f'{self.g[0][i][j]} / {self.g[1][j][i]}', end=' | ')
            print()

    def strictly_dominated(self, p, a):
        '''L'action a du joueur p est-elle dominée ?'''
    
        m = self.n_actions(p)
        n = self.n_actions(1 - p)
    
        problem = LpProblem("Strict_dominance", LpMaximize)
    
        # pour simuler une contrainte stricte: on voudra la valeur max d'epsilon != 0
        epsilon = LpVariable("epsilon", 0, 1)
    
        # on veut maximiser epsilon
        problem += epsilon
    
        # stratégie qui domine
        s = [ LpVariable(f'strategy{k}', 0, 1) for k in range(m)]
    
        # s est une distribution de probabilités
        c = 0
        for k in range(m):
            c += s[k]
    
        problem += c == 1
    
        # pour chaque stratégie pure de l'autre joueur
        for b in range(n):
            # On cherche une stratégie s de p dont l'utilité contre l'action b est 
            # strictement meilleure que celle de a
            c = 0
            for k in range(m):
                c += s[k] * self.g[p][k][b]
            problem += c >= self.g[p][a][b] + epsilon
                
        problem.solve(COIN_CMD(msg=0))
        #print(f'status: {LpStatus[problem.status]}')
        #print(value(problem.objective))
        #for v in problem.variables():
        #    print(f'{v.name} = {v.varValue}')
    
        return LpStatus[problem.status] == 'Optimal' and value(problem.objective) > 0

    def irsds(self):
        '''Iterated Removal of Strictly Dominated Strategies (IRSDS)'''
        finished = False
        while not finished:
            finished = True
            for p in range(2):
                m = self.n_actions(p)
    
                k = 0
                for a in range(m):
                    if self.strictly_dominated(p, a - k):
                        self.delete_action(p, a - k)
                        # comme on a supprimé des actions avant, l'indice dans la matrice  
                        # doit être corrigé
                        k += 1
                        finished = False

    def strictly_dominated_as(self, p, a, sup):
        '''Calcule si l'action a de p est strictement dominée par une autre action, 
        pas forcément dans sup[p], étant donné le support sup[1-p] de l'adversaire'''
        u1 = self.g[p]
        u2 = self.g[1-p]
        m = self.n_actions(p)
        n = self.n_actions(1-p)
        print(u1)
        print(u1[a][0])
        return (np.all(u1[a][0] > u2[a][0]) and np.all(u1[a][1] > u2[a][1]))

    
    def irsda_support(self, sup):
        '''Iterated Removal of Strictly Dominated Actions with a support'''
        for i in range(2):
            for a in sup:
                if self.strictly_dominated_as(p = i, a = a, sup = sup):
                    self.delete_action(i, a)
        
           

    def nash_support(self, sup):
        '''Calcule un équilibre de Nash utilisant toutes les actions de tous les joueurs
        (s'il y en a un)'''
        res = []
        for p in range(2):
            for a in sup[p]:
                print(a)
                if self.strictly_dominated_as(p, a, sup):
                    res.append(a)
                    # self.delete_action(p, a)
        return res

    def nash_equilibria(self, sup, mem, eqs):
        '''Calcule tous les équilibres de Nash de g'''
        key = (tuple(sup[0]), tuple(sup[1]))
    
        # Mémoisation: si on n'a pas déjà traité cette sous-(bi)matrice
        if key not in mem:
            # on élimine les actions strictement dominées étant donné le support
            self.irsda_support(sup)

            if sup[0] and sup[1]:
                # on cherche les équilibres utilisant les actions du support
                s = self.nash_support(sup)
                if s is not None:
                    # il y a un équilibre
                    print(s)
                    e = []
                    for p in range(2):
                        # on crée un profil de stratégies : un tuple pour chaque joueur 
                        # qui contient sa stratégie sous forme de couples 
                        # (numéro d'action, probabilité)
                        strat = []
                        for a in s[p]:
                            strat.append(a.varValue)
                        e.append(tuple(zip(sup[p], strat)))

                    # on ajoute le profil de stratégies à la liste des équilibres
                    eqs.add(tuple(e))
    
                # on rappelle la méthode récursivement en supprimant une action de 
                # l'un ou l'autre joueur (on fait toutes les possibilités)
                for p in range(2):
                    if len(sup[p]) > 1:
                        for a in range(len(sup[p])):
                            sup2 = deepcopy(sup)
                            del sup2[p][a]
                            self.nash_equilibria(sup2, mem, eqs)
    
            # Mémoisation
            mem.add(key)

# jeu sans équilibre pur
#game = Game(np.array([[1,2],[2,1]]), np.array([[2,1],[1,2]]))

# sortie musicale 
#game = Game(np.array([[1,0],[0,2]]), np.array([[2,0],[0,1]]))

# dilemme du prisonnier
#game = Game(np.array([[-8,0],[-10,-2]]), np.array([[-8,-10],[0,-2]]))

# matching pennies
#game = Game(np.array([[0,-1,1],[1,0,-1],[-1,1,0]]), np.array([[0,1,-1],[-1,0,1],[1,-1,0]]))

# chicken
game = Game(np.array([[-1,3],[0,2]]), np.array([[-1,0],[3,2]]))

game.print()

# suppression itérée des stratégies strictement dominées
# game.irsds()

done = set()
equilibria = set()

supports = [list(range(game.n_actions(p))) for p in range(2)]

game.nash_equilibria(supports, done, equilibria)

print(equilibria)
