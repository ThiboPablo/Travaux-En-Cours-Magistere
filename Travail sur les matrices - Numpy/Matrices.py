import numpy
import math
A=numpy.array([[1,2],[1,1]])
#print(A * 2)
#A=numpy.array([[1,2],[3,4]])
#print(A + A)
#B=numpy.array([[1,1]])

#print(A@B, B@A)

#n = 10
#p = 10
#id = numpy.identity(n)
#leZ = numpy.zeros((n,p))
#lesUns = numpy.ones((n,p))
#diagz = numpy.diag([1,2,3])

#maMat = numpy.array(2*id - lesUns)
#print(maMat, maMat.shape)
#print(maMat.reshape(20, 5))

#maMat.T #transposée
#print(numpy.linalg.inv([[1,1],[1,1]]))

#with open("C:/Users/thiba/Desktop/Cours/Modélisation Progra/Projet exo/Données brutes/Effectifs salariés/Bonnes données temp - E+MS - Grands secteurs - Régions - 98-24.csv") as f:
#    donnees=[l.split(";") for l in f.readlines()]
#A=numpy.array(donnees, dtype="str")
#with open("nouveaufichier.csv", "w") as f: #"w" pour "write"
#    f.write("".join(";".join(str(x) for x in l) for l in A))

with open("C:/Users/thiba/Desktop/Cours/Modélisation Progra/TD1 du S2/Pop.csv", encoding = "latin1") as f:
    donnees=[l.split(";") for l in f.readlines()]

table = {}
for l in donnees[1:]:
    if l[1] in table:
        table[l[1]][(l[3],l[4])] = l[5].strip()
    else: #nouvelle commune
        table[l[1]]={(l[3],l[4]):l[5].strip()}


for (c,valeurs) in table.items():
    table[c]=[valeurs.get((sexe,age),0) for age in ("00","03","06","11","18","25","40","55","65","80") for sexe in "12"]

matrix = numpy.array([table[c] for c in table.keys()], dtype=float)
matrix = matrix.astype(int)
codes_communes = list(table.keys())


monY = matrix[:, 0] + matrix[:, 1]
explicatives = ['03', '06', '11', '18', '25', '40', '55', '65', '80']

Ieuv = {f'Ieuv{wavelength}': matrix[:, i] + matrix[:, i+1]
        for wavelength, i in zip(explicatives, range(20 - 2*len(explicatives), 20, 2))}

Ieuv0 = numpy.ones(matrix.shape[0])

monX = numpy.column_stack([Ieuv0] + [Ieuv[f'Ieuv{wavelength}'] for wavelength in explicatives])

XTX = monX.T @ monX
XTY = monX.T @ monY
lesCoef = numpy.linalg.inv(XTX) @ XTY


finModèle = ''
for wavelength, i in zip(explicatives, range(1, len(explicatives) + 1)):
    finModèle += f' + {round(lesCoef[i], 3)}*X{wavelength}'
print(f"Le modèle nous donne l'équation suivante : Naissances = {lesCoef[0]}{finModèle}")
