#Activer le bon chemin d'accès
#setwd("C:/Users/thiba/Desktop/Cours/Modélisation Progra/Données enregistrées depuis R")
getwd()

#FONCTION GRAPHIQUE

graphF = function(vecDeDonnées){
  return(plot(ecdf(vecDeDonnées), 
              main = "Fonction de répartition",
              xlab = "Valeurs",
              ylab = "F(x)",
              do.points = FALSE,
              col = 'red'))
}

#Premières utilisations de commandes

mesNombres <- c(sample(1:126, 20))
mesNombres <- sort(mesNombres)
barplot(mesNombres)

graphF(mesNombres)

lEstimateur <- ((length(mesNombres) + 1) / length(mesNombres)) * max(mesNombres)
lEstimateur

#FONCTION TEST D'ESTIMATEUR A REPETITION

testEchantillon = function(b, nbDeFois){
  sommeDesEstimateurs <- 0
  for (i in 1:nbDeFois) {
    leVecteur <- c(runif(20, min=0, max=b))
    lEstimateur <- ((length(leVecteur) + 1) / length(leVecteur)) * max(leVecteur)
    sommeDesEstimateurs <- sommeDesEstimateurs + lEstimateur
  }
  return(sommeDesEstimateurs / nbDeFois)
}

testEchantillon(997, 400)


#FONCTION EXPONENTIELLE

maLoi <- rexp(300, 6)
maLoi
write.csv(maLoi, "loiExpoThibaut.csv", row.names = FALSE)

#RECUPERATION DU FICHIER D'UN AUTRE PUIS ESTIMATION DE LAMBDA

loiRecup <- as.vector(read.csv("loiExpoThibaut.csv"))
vecFinal <- c()
for (donnée in loiRecup) {
  vecFinal <- c(vecFinal, donnée)
}
#ESTIMATEUR
1/mean(vecFinal)

#PARTIE FONCTION DE REPARTITION
graphF(vecFinal)
fEmpirique <- ecdf(vecFinal)
valeursDeF <- fEmpirique(vecFinal)


#EXERCICE 3

maListeGeom <- rgeom(100, 1/6)
graphF(maListeGeom)

#EXERCICE 4

vecteurU = c(runif(1000))
vecteurV = c(runif(1000))
vecteurNorm = c(sqrt(-2*log(vecteurU, base = exp(1)))*cos(2*pi*vecteurV))
graphF(vecteurNorm)
hist(vecteurNorm)