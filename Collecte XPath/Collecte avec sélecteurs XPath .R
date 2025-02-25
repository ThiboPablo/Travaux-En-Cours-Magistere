library(httr)
perdu <- GET("https://perdu.com")
content(perdu)
###Ici, je parse la page (càd j'explique à R ce dont il s'agit)
lecontenuDeperdu=read_html(x = "perdu.html")

#je veux charger dans R une page prétéléchargée

library(rvest)
cperdu <- read_html("C:\\Users\\thiba\\Desktop\\Cours\\Collecte de données\\perdu.html")


###Extraction avec XPath.
###XPath permet de sélectionner des "noeuds" (constitués de 2 balises, type, contenu, attributs)
###d'une page web en s'appuyant sur la structure HTML d'un site.


##4 symboles à utiliser en XPath pour naviguer à travers un site :
## / pour les enfants directs, // pour trouver une balise n'importe où dans la page,
## @ pour les attributs, [] pour la condition.

#Exemples:  "//div/a :prend tous les liens présents au sein de chacune des balises div.

#exemple concret : sur le site https://www.meteociel.fr/previsions/25059/strasbourg.htm,
#le sélecteur XPath //i/b amène à "St Modeste"

#enregistrer la page via R
laMétéo <- GET("https://www.meteociel.fr/previsions/25059/strasbourg.htm")
#vérifier que c'est bien du HTML
content(laMétéo)
#appliquer le sélecteur
html_elements(content(laMétéo), xpath = "//i/b") %>% html_text2()