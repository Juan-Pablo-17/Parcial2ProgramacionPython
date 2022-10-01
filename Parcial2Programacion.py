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

#==============================================================
#Función Cos(x)
#==============================================================

#El acumulador comienza en CERO

cos_x = 0.0

#Ciclo para sumar los términos de la función Cos(x)

for k in range(n):
    b=Factorial(2*k)
    cos_x = cos_x + ((-1)**k * x**(2*k)) / b

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
#==============================================================
#Imprimir
#==============================================================

print("Para x= ", x_deg, " grados, ó x=", x, "radianes")
print("El sen(x) es: ", sen_x)
print("El cos(x) es: ", cos_x)
print("Para y=", y)
print("La exp(y) es: ", exp_x)
