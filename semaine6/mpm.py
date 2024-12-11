dico = {}

class Tache:
    def __init__(self, valeur, predecesseur):
        self.valeur = valeur
        self.predecesseur = predecesseur
        self.successeur = []
        self.dateAuPlusTot = None
        self.dateAuPlusTard = None
        self.margeLibre = None

# retourne une liste deux dimention
# des sommets
# ordonnÃ© par niveaux d'ordonancement
def ordonancement():
    # oÃ¹ est stockÃ© la liste de liste
    result = []
    # oÃ¹ sont sockÃ© les sommets deja ordonnÃ©e
    visite = []
    queute = [key for key in dico.keys()]
    while len(queute):
        # oÃ¹ sont stockÃ© les sommets visitÃ© lors du tour 
        passage = []
        for element in queute:
            # si tous les prÃ©dÃ©cesseur ont Ã©tÃ© visitÃ©, ou qu'il n'y en a pas
            if not len([1 for pred in dico[element].predecesseur if pred not in visite]):
                passage += [element]
                # on fixe les successeurs
                for predecesseur in dico[element].predecesseur:
                        dico[predecesseur].successeur += [element]
        # les elements ajoutÃ© lors du passage sont ajouter au resultat
        result += [passage]
        visite += passage
        if passage == []:
            return None
        # on supprime les elements visitÃ© en dehors de la boucle
        for element in passage:
            del(queute[queute.index(element)])
    return result

# valorise niveau par niveau
# dans le sens croissant
# la dateAuPlusTot des taches
def dateAddAuPlusTot(listeOrd):
    for tour, elements in enumerate(listeOrd):
        for element in elements:
            if tour == 0 :
                dico[element].dateAuPlusTot = 0
            else:
                dico[element].dateAuPlusTot = max([dico[k].valeur + dico[k].dateAuPlusTot for k in dico[element].predecesseur]) 

# valorise niveau par niveau
# dans le sens decroissant
# la dateAuPlusTard des taches
def dateAddAuPlusTard(listeOrd):
    for tour, elements in enumerate(listeOrd[::-1]):
        for element in elements:
            if tour == 0 :
                dico[element].dateAuPlusTard = dico[element].dateAuPlusTot
                dico[element].margeLibre = 0
            else:
                dico[element].dateAuPlusTard = min([ dico[k].dateAuPlusTard - dico[element].valeur for k in dico[element].successeur])
                dico[element].margeLibre =  min([ dico[k].dateAuPlusTot - dico[element].valeur for k in dico[element].successeur]) - dico[element].dateAuPlusTot

#nom du sommet  predecesseur
dico["A"]= Tache(1, [])
dico["B"]= Tache(1, ["A"]) 
dico["C"]= Tache(1, ["A"]) 
dico["D"]= Tache(2, ["C"]) 
dico["E"]= Tache(2, ["B", "D"]) 
dico["F"]= Tache(1, ["D"]) 
dico["G"]= Tache(6, ["F"]) 
dico["H"]= Tache(10, ["E", "F"])
dico["I"]= Tache(2, ["G", "H"]) 
#dico["J"]= Tache(11, []) 
#dico["K"]= Tache(6, ["A", "B", "D"])
#dico["L"]= Tache(2, ["A", "B", "D", "K"])
#dico["M"]= Tache(6, ["A", "B", "D"]) 
#dico["N"]= Tache(1, ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"])
# set de tous les predecesseurs avec sum pour passer la liste a une dimention
predSet = set(sum((dico[k].predecesseur for k in dico.keys()), []))
# si le sommets n'est devant aucun autre il est devant la fin
dico["fin"] = Tache(0, [key for key in dico.keys() if key not in predSet])

listeOrdonnee = ordonancement()
if listeOrdonnee:
    dateAddAuPlusTot(listeOrdonnee)
    dateAddAuPlusTard(listeOrdonnee)
    for rank ,liste in enumerate(listeOrdonnee):
        print("Hauteur : " + str(rank))
        for element in liste: print("Element : " + element + " ,Valeur :" + str(dico[element].valeur) + ", Date au plus tot : " + str(dico[element].dateAuPlusTot) 
        + ", Date au plus tard :"  + str(dico[element].dateAuPlusTard) + ", Marge Libre :"  + str(dico[element].margeLibre)
        + ", Successeur : " + "-".join(dico[element].successeur) + ", Predecesseur : " + "-".join(dico[element].predecesseur))
else:
    print("Erreur d'ordonnancement")
