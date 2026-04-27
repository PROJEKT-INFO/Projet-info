from turtle import *
from random import *
def error1():
    up()
    width(5)
    goto(-180,-200)
    left(90)
    down()
    forward(500)
    right(90)
    forward(400)
    up()
    goto(-100,300)
    down()
    goto(-180,220)
    up()
    goto(220,300)
    down()
    right(90)
    forward(80)
    up()
    goto(-230,-200)
    down()
    left(90)
    forward(500)
    up()

def error2():
    goto(40,300)
    down()
    right(90)
    forward(100)
    right(90)
    fillcolor('pink')
    begin_fill()
    circle(50)
    end_fill()

def error3():
    left(90)
    up()
    goto(40,100)
    down()
    forward(100)

def error4():
    right(30)
    forward(80)
    backward(80)

def error5():
    left(60)
    forward(80)
    right(30)
    up()

def error6():
    goto(40,70)
    down()
    right(130)
    forward(70)
    backward(70)

def error7():
    left(260)
    forward(70)
    backward(70)
    up()

def error8():
    goto(20,155)
    down()
    dot(12)
    up()
    goto(60,155)
    down()
    dot(12)
    up()
    goto(30,125)
    down()
    forward(12)
    right(80)
    forward(12)
    up()
    hideturtle()
    goto(-400,280)
    down()
    write("P E R D U !",align="center",font=("Verdana", 20, "bold"))
    mainloop()


#listes de mots
l5={"maison":"habitat pour les humains",
    "amour":"sentiment souvent représenté par un symbole",
    "danse":"sport qui s'accompagne souvent de musique",
    "sable":"ce qui tapisse le sol des lieux de vacances",
    "valse":"danse caractérisée par un mouvement de rotation"}
l6={"soleil":"qui éclaire la terre",
    "tortue":"animal à carapace",
    "puzzle":"jeu d'assemblage calme",
    "bateau":"permet de voyager sur les eaux",
    "cactus":"plante que l'on trouve dans les zones désertiques"}
l7={"banquise":"grande étendue de glace",
    "cartable":"sac utilisé pour l'école",
    "dessert":"plat sucré mangé à la fin du repas",
    "tornade":"vent très violent",
    "village":"petit groupe de maisons"}
l8 = {"aventure":"histoire avec des événements imprévus",
    "boussole":"objet qui aide à se repérer",
    "telescope":"objet pour observer les objets lointains",
    "grenouille":"animal qui saute et nage",
    "pyramide":"grand monument de forme triangulaire"}
ind="aucun"
#choix de la longueur du mot
length=numinput("Longueur du mot", "choisissez la longueur du mot allant de 5 à 8:")
if length<5 or length>8:
    length=numinput("Longueur du mot", "choix incorrect, choisissez la longueur du mot allant de 5 à 8:")
if length==5:
    mot=choice(list(l5.keys()))
    ind=l5[mot]
elif length==6:
    mot=choice(list(l6.keys()))
    ind=l6[mot]
elif length==7:
    mot=choice(list(l7.keys()))
    ind=l7[mot]
elif length==8:
    mot=choice(list(l8.keys()))
    ind=l8[mot]

mot=list(mot)
trouvés=[]
poubelle=[]
écrit=Turtle()
nb_erreurs=0
erreurs=[error1,error2,error3,error4,error5,error6,error7,error8]
indice=Turtle()
indice.hideturtle()
while len(mot)!=len(trouvés):
    trouvés.append("*")
while trouvés!=mot:
    lettre=textinput("LETTRE", "entrez la lettre ci dessous, ou:\n-tapez 'sortie' pour quitter le jeu\n-tapez 'indice' pour en obtenir 1")
    if lettre=="sortie":
        break
    if lettre=="indice":
        indice.clear()
        indice.up()
        indice.goto(0,-320)
        indice.down()
        indice.write(ind,align="center",font=("Verdana",14, "bold"))
        indice.hideturtle()
    elif lettre in mot:
        for i,j in enumerate(mot):
            if j==lettre:
                trouvés[i]=lettre
    elif lettre in poubelle or lettre in trouvés:
        textinput("INFORMATION", "Lettre déjà séléctionnée auparavent !\nClique sur OK pour continuer.")
    else:
        poubelle.append(lettre)
        erreurs[nb_erreurs]()
        nb_erreurs+=1

    affiche="".join(trouvés)
    écrit.reset()
    écrit.hideturtle()
    écrit.up()
    écrit.goto(0,-260)
    écrit.down()
    écrit.write(affiche,align="center",font=("Verdana",22, "bold"))
    écrit.hideturtle()

if trouvés==mot:
    écrit.reset()
    indice.reset()
    reset()
    write("G A G N É ! ! !",align="center",font=("Verdana",25, "bold"))
    hideturtle()
    écrit.hideturtle()
    indice.hideturtle()
    mainloop()