import random as rd
import math
import numpy as np
import matplotlib.pyplot as ppl

def fonc(y):
    return (2*y - 1)

n = 1000
p = 0.4
lesRacines = []
ppl.figure(figsize=(10, 6))
for i in range(100):
    listeFinale = []
    for j in range(n):
        jeu = rd.choices([0,1], weights=[1-p, p])[0]
        résultat = 1 if jeu == 1 else -1
        listeFinale.append(résultat)
    cumul = np.cumsum(listeFinale)
    x = np.arange(1, len(cumul) + 1)
    ppl.plot(x, cumul, color = 'r', linestyle='-', alpha=0.3, linewidth=1)

écartType = np.sqrt(p*(1-p))
if p - (1-p) > 0:
    lesRacines = [2*écartType*np.sqrt(i) + (p - (1-p))*i for i in range(n)]
    lesRacines2 = [-(2*écartType*np.sqrt(i)) + (p - (1-p))*i for i in range(n)]
else:
    lesRacines = [-(2*écartType*np.sqrt(i) - (p - (1-p))*i) for i in range(n)]
    lesRacines2 = [-(2*écartType*np.sqrt(i)) + (p - (1-p))*i for i in range(n)]
ppl.plot(lesRacines, color = 'black', linestyle='-', alpha=1, linewidth=2)
ppl.plot(lesRacines2, color = 'black', linestyle='-', alpha=1, linewidth=2)

p = 1-p
for i in range(100):
    listeFinale = []
    for j in range(n):
        jeu = rd.choices([0,1], weights=[1-p, p])[0]
        résultat = 1 if jeu == 1 else -1
        listeFinale.append(résultat)
    cumul = np.cumsum(listeFinale)
    x = np.arange(1, len(cumul) + 1)
    ppl.plot(x, cumul, color = 'r', linestyle='-', alpha=0.3, linewidth=1)
écartType = np.sqrt(p*(1-p))

if p - (1-p) > 0:
    lesRacines = [2*écartType*np.sqrt(i) + (p - (1-p))*i for i in range(n)]
else:
    lesRacines = [-(2*écartType*np.sqrt(i) - (p - (1-p))*i) for i in range(n)]
ppl.plot(lesRacines, color = 'black', linestyle='-', alpha=1, linewidth=2)

ppl.axhline(y=0, color='r', linestyle='--', alpha=0.7)

ppl.show()