#Exo1:

def is_leap_year(annee):
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                print(f'Lannée {annee} est bissextile')
            else:
                print(f'Lannée {annee} n est pas bissextile')
        else:
            print(f'Lannée {annee} est bissextile')
    else:
        print(f'Lannée {annee} n est pas bissextile')

annee = int(input(" entrer une année"))
print(is_leap_year(annee))

print("####-------------------------------------#############")
print("####-------------------------------------#############")


#Exo2:
#question1

def lancer():
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    som = de1 + de2
    return som
resul = lancer()
print("Résultat du lancer de deux dés :", resul)

#question2
print("####-------------------------------------#############")

def lancer_des(nb_des):
    som = 0
    for _ in range(nb_des):
        som += random.randint(1, 6)
    return som

result = lancer_des(2)
print("Résultat du lancer de deux dés :", result)
result = lancer_des(3)
print("Résultat du lancer de trois dés :", result)

print("####-------------------------------------#############")
print("####-------------------------------------#############")


#Exo3:

def afficherSuiteCarres(n):
    lescarres = ""
    for i in range(n+1):
        carre = i ** 2
        lescarres += str(carre) + " - "
    print(lescarres)

n = int(input("Entrez un entier n : "))

afficherSuiteCarres(n)

print("####-------------------------------------#############")
print("####-------------------------------------#############")


#Exo4:

def produit(n1, n2):
    result = 1
    if n1 < n2 :
        for i in range(n1, n2+1):
            result *= i
        return result
n1 = int(input("Entrez n1 : "))
n2 = int(input("Entrez n2 : "))
pr = produit(n1, n2)
print("Le produit des entiers entre", n1, "et", n2, "est de :", pr)

print("####-------------------------------------#############")
print("####-------------------------------------#############")

#Exo5:

def nbPairImpair(tableau):
    pair = 0
    impair = 0
    for nb in tableau:
        if nb % 2 == 0:
            pair += 1
        else:
            impair += 1
    return pair, impair

tab= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pair, impair = nbPairImpair(tab)
print("Nombre d'éléments pairs :", pair)
print("Nombre d'éléments impairs :", impair)

print("####-------------------------------------#############")
print("####-------------------------------------#############")

#Exo6:

def decaleCircDroite(tableau):
    dernier_element = tableau[-1]  # Stocker le dernier élément
    for i in range(len(tableau)-1, 0, -1):
        tableau[i] = tableau[i-1]  # Déplacer chaque élément vers la droite
    tableau[0] = dernier_element  # Placer le dernier élément au début

tab = [12, 21, 10, 11, 0, 1, 6, 8]
print("Avant décalage circulaire à droite :", tab)
decaleCircDroite(tab)
print("Après décalage circulaire à droite :", tab)

print("####-------------------------------------#############")
print("####-------------------------------------#############")


#Exo7:
#QUESTION 7.1

def bin2Dec(nBin):
    nDec = int(nBin, 2)
    return nDec
nBin = input ("entrez un nombre binaire")
nDec = bin2Dec(nBin)
print('Le nombre binaire ' + nBin + ' se convertit en base 10 : ' + str(nDec))

print("####-------------------------------------#############")

#QUESTION 7.2

def dec2Bin(nDec):
    nBin = bin(nDec)[2:]
    return nBin
nDec = int(input ("entrez un nombre décimal"))
nBin = dec2Bin(nDec)
print('Le nombre décimal ' + str(nDec) + ' sécrit en base 2 : ' + nBin)

print("####-------------------------------------#############")
print("####-------------------------------------#############")

#Exo8:
def Somme(n):
    if n == 1:
        return 1
    else:
        return n + Somme(n - 1)
n = int(input("Entrez un entier n : "))
somme = Somme(n)
print("La somme des", n, "premiers entiers est :", somme)

print("####-------------------------------------#############")
print("####-------------------------------------#############")


#Exo9:

def Puissance(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        puissance = Puissance(x, n//2)
        return puissance * puissance
    else:
        return x * Puissance(x, n-1)
x = float(input("Entrez la valeur de x : "))
n = int(input("Entrez la valeur de n : "))
resultat = Puissance(x, n)
print(x, "élevé à la puissance", n, "est égal à :", resultat)

print("####-------------------------------------#############")
print("####-------------------------------------#############")

#Exo10:

def Fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
n = int(input("Entrez un entier n : "))
result = Fibonacci(n)
print("Le", n, "ème terme de la suite de Fibonacci est :", result)

print("####-------------------------------------#############")
print("####-------------------------------------#############")

#Exo11:

chiffres = list(range(1, 11))
chiffres_str = list(map(str, chiffres))
resultat = ";".join(chiffres_str)
print(result)

print("####-------------------------------------#############")
print("####-------------------------------------#############")

#Exo12:

import random

def echanger(tab, idx1, idx2):
    tab[idx1], tab[idx2] = tab[idx2], tab[idx1]

def triSelection(tab):
    taille = len(tab)
    for i in range(taille-1):
        minIndex = i
        for j in range(i+1, taille):
            if tab[j] < tab[minIndex]:
                minIndex = j
        if minIndex != i:
            echanger(tab, i, minIndex)
chiffres = [random.randint(1, 100) for _ in range(10)]
triSelection(chiffres)
chiffres_str = list(map(str, chiffres))
resultat = ', '.join(chiffres_str)
print(resultat)

print("####-------------------------------------#############")
print("####-------------------------------------#############")

#Exo13:

def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n-1)
resultat = factorielle(20)
print("La factorielle de 20 est :", resultat)

print("####-------------------------------------#############")
print("####-------------------------------------#############")

#Exo14:

import random

def phrase(mots):
    random.shuffle(mots)
    phrases = ' '.join(mots)
    print(phrases)
mots = ["mange", "dormir", "travailler", "marcher", "chanter", "et"]
phrase(mots)





