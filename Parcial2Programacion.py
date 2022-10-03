#==============================================================

#La primera parte de este programa es para apróximar...
#...las funciones exponencial seno y coseno...
#...sin utilizar la librería math

#Parcial 2 Programación/Universidad del Quindío/...
#.../Profesor: Santiago Echeverri Arteaga/2022-2.

#Estudiante: Juan Pablo Cobo Trujillo.

#La segunda parte es graficar al menos una de las funciones de la...
#...primera parte y compararla con la función de la librería math

#==============================================================
#Gráficas
#==============================================================
#Librerías
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,AutoMinorLocator)

#==============================================================
#Variables y Objetos(Métodos)
#==============================================================
#Valor del argumento en grados(Según lo quiera el usuario) ->x

x_deg = float(input("¿Cuál es el valor del argumento(grados):? "))

#Convertir a radianes el ángulo

x = (x_deg*3.14159)/180

#Pedir el número de términos para la aproximación

n = int(input("¿De cuánto quiere que sea la aproximación?: "))

#El acumulador comienza en CERO

sen_x = 0.0
#==============================================================
#Función para calcular el factorial
#==============================================================
def Factorial(a):
    if a==0 or a==1:
        Resultado = 1
    elif a>1:
        Resultado = a*Factorial(a-1)
    return Resultado
#==============================================================
#Función Sen(x)
#==============================================================

#Ciclo para sumar los términos acumulativos, es decir la aproximación

for k in range(n):
    a=Factorial(2*k+1)
    sen_x = sen_x + (-1)**k * x**(2*k+1) / a
    
#Para la gráfica de todos los puntos de acuerdo con la aproximación

sen_p = 0.0

s=np.linspace(0,10, 100)

for k in range(n):
    a=Factorial(2*k+1)
    sen_p = sen_p + (-1)**k * s**(2*k+1) / a

#==============================================================
#Función Cos(x)
#==============================================================

#El acumulador comienza en CERO

cos_x = 0.0

#Ciclo para sumar los términos de la función Cos(x)

for k in range(n):
    b=Factorial(2*k)
    cos_x = cos_x + ((-1)**k * x**(2*k)) / b

#Para la gráfica de todos los puntos de acuerdo con la aproximación

cos_p = 0.0

for k in range(n):
    b=Factorial(2*k)
    cos_p = cos_p + ((-1)**k * s**(2*k)) / b

#==============================================================
#Función exp(x)
#==============================================================

#Definir una variable ya que la función exp no se calcula en ángulos
y = float(input("¿Cuál es el valor del argumento de la función exp(x)? "))
#El acumulador comienza en CERO

exp_x = 0.0

#Ciclo para sumar los términos de la función exp(x)

for k in range(n):
    c = Factorial(k)
    exp_x = exp_x + (y**k) / c
    
#Para la gráfica de todos los puntos de acuerdo a la aprox de exp

exp_p = 0.0

#Ciclo para sumar los términos de la función exp(x)

for k in range(n):
    c = Factorial(k)
    exp_p = exp_p + (s**k) / c

#==============================================================
#Imprimir
#==============================================================

print("Para x= ", x_deg, " grados, ó x=", x, "radianes")
print("El sen(x) es: ", sen_x)
print("El cos(x) es: ", cos_x)
print("Para y=", y)
print("La exp(y) es: ", exp_x)

#==============================================================
#Gráficas
#==============================================================

#Creando las figura

fig_1 = plt.figure("Gráfica del Sen(x)")

#Definiendo figura

ax1=fig_1.add_subplot()



#Funciones de la librería np

def h(z):
    return np.sin(z)

def g(z):
    return np.cos(z)

def j(z):
    return np.exp(z)

#Intervalos

z=np.linspace(0, 10, 100)

#Gráfica del Sen(x)

ax1.plot(z, h(z), "r", label="$Sen(x)$")     #Función Sin(x) de np
ax1.plot(x, sen_x, marker="o", color="b", label="$P$") #Punto de la aproximación
ax1.plot(s, sen_p, "g", label="$Sen'(\Theta)$")     #Función Sin(x) de la Aprox
ax1.set_xticklabels([r'$-\frac{\pi}{2}$',r'$0$',r'$\frac{\pi}{2}$',r'$\pi$',
                     r'$\frac{3\pi}{2}$', r'$2\pi$'])

#Acotamiento de la gráfica

v=[0,10,-1.5,1.5]

#Detalles de la gráfica Sen(x)

plt.subplot()
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Aproximación a la función $Sen(x)$")
plt.grid()
plt.axis(v)
plt.text(0.3,-0.5, "$sen'(\Theta)=$Aproximación")
plt.text(0.3,-0.7, "$P=$Argumento Ingresado")
plt.text(x + 0.2,sen_x + 0.2, "$Punto=P$", color="b")
plt.legend(loc=1)

#Gráfica del Cos(x)

#Creando las figura

fig_2 = plt.figure("Gráfica de la función Cos(x)")

#Definiendo figura

ax2=fig_2.add_subplot()

ax2.plot(z, g(z), "r", label="$Cos(x)$")     #Función Sin(x) de np
ax2.plot(x, cos_x, marker="o", color="b", label="$P$") #Punto de la aproximación
ax2.plot(s, cos_p, "g", label="$Cos'(\Theta)$")     #Función Sin(x) de la Aprox
ax2.set_xticklabels([r'$-\frac{\pi}{2}$',r'$0$',r'$\frac{\pi}{2}$',r'$\pi$',
                     r'$\frac{3\pi}{2}$', r'$2\pi$'])

#Detalles de la gráfica de Cos(x)

plt.subplot()
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Aproximación a la función $Cos(x)$")
plt.grid()
plt.axis(v)
plt.text(0.3,-0.5, "$cos'(\Theta)=$Aproximación")
plt.text(0.3,-0.7, "$P=$Argumento Ingresado")
plt.text(x + 0.2,cos_x + 0.2, "$Punto=P$", color="b")
plt.legend(loc=1)

#Para la función exp(x)

#Creando las figura

fig_3 = plt.figure("Gráfica de la función exp(x)")

#Definiendo figura

ax3=fig_3.add_subplot()

ax3.plot(z, j(z), "r", label="$exp(x)$")     #Función exp(x) de np
ax3.plot(y, exp_x, marker="o", color="b", label="$P$") #Punto de la aproximación
ax3.plot(s, exp_p, "g", label="$exp'(x)$")     #Función exp(x) de la Aprox

#Detalles de la gráfica de exp(x)

#Acotamiento de la gráfica

b=[0,10,-1,100]

plt.subplot()
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Aproximación a la función $exp(x)$")
plt.grid()
plt.axis(b)
plt.text(6,20, "$exp'(x)=$Aproximación")
plt.text(6,17, "$P=$Argumento Ingresado")
plt.text(y+1,2+exp_x, "$Punto=P$", color="b")
plt.legend(loc=1)

plt.tight_layout()
plt.show()
