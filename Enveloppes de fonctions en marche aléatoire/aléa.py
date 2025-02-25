import random as rd
import math
import numpy as np
import matplotlib.pyplot as ppl

def fonc(y):
    return (2*y - 1)

lesRacines = []
ppl.figure(figsize=(10, 6))
for i in range(300):
    listefinale = []
    lancers = []
    lancers = [rd.randint(0,1) for i in range(1000)]
    for éléments in lancers:
        listefinale.append(fonc(éléments))
    cumul = np.cumsum(listefinale)
    x = np.arange(1, len(cumul) + 1)
    ppl.plot(x, cumul, color = 'r', linestyle='-', alpha=0.3, linewidth=1)

lesRacines = [2 * np.sqrt(i) for i in range(1000)]
lesRacNeg = [-x for x in lesRacines]
ppl.plot(lesRacines, color = 'black', linestyle='-', alpha=1, linewidth=2)
ppl.plot(lesRacNeg, color = 'black', linestyle='-', alpha=1, linewidth=2)

ppl.axhline(y=0, color='r', linestyle='--', alpha=0.7)

ppl.grid(True, alpha=0.3)

ppl.savefig('Résultat.png')
ppl.show()