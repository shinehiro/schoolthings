# On importe une librairie en lui donnant un nom raccourci
import numpy as np
import sympy as sy
import matplotlib as plt    

# Création des variables dans les fonctions
t = sy.Symbol('t') # Le temps
w = sy.Symbol('w') # Variable w (je ne sais pas comment la mettre...) (π/3,00 rad/s)
vx0 = sy.Symbol('vx0') # Vitesse initiale
x0 = sy.Symbol('x0') # Position initiale
A = sy.Symbol('A') # Variable A 
m = sy.Symbol('m') # Masse (0,100 kg)

# Fonction définissant l'accélération en fonction du temps (obtenue en divisant la fonction de force par m)
ax = (A*t*sy.sin(w*t))/m

#Création des fonctions vx et x
vx = sy.Function('vx') (t)
x = sy.Function('x') (t)

# On intègre
vx = sy.simplify(sy.integrate(ax, (t, 0, t)) + vx0)
x = sy.simplify(sy.integrate(vx, (t, 0, t)) + x0)

#on affiche les résultat
print("ax = ", ax)
print("vx = ", vx)
print("x = ", x)
