#-------------------------------------Operadores Aritméticos
#suma de dos números
num1 = 4
num2 = 5

resultado = num1 + num2

print("El resultado de la suma es:", resultado)

#resta de dos números
num1 = 10
num2 = 3

print("El resultado de la resta es:", num1 - num2)

#multiplicación de dos números
num1 = 7
num2 = 6
print("el resultado de la multiplicación es:", num1 * num2)

#división de dos números que puede dar como resultado un número decimal
num1 = 8
num2 = 2
num3 = num1 / num2
print("El resultado de la división es:", num3)
print(type(num3))

#division entera (no da decimales)
num1 = 8
num2 = 5
print("El resultado de la división entera es:", num1 // num2)

#módulo (residuo de una división)
num1 = 8 
num2 = 5
print("El resultado del modulo de reciduo es:", num1 % num2)

#potencia de un numero
num1 = 2
num2 = 3
print("El resultado de la potencia es:", num1 ** num2)

#-------------------------------------Operadores de asignación
x = 5
print("El valor de x es:", x)

x += 3 #es igual a que x = x + 3
print("El nuevo valor de x es:", x)

x -= 2 #quiere decir que x = x - 2
print("El nuevo valor despues de la asignacion de resta es de:", x)

x *= 4 #Esto quiere decir que x = x * 4
print("El nuevo valor despues de la asignacion de multiplicacion es de:", x)

x /= 2 #Lo cual quiere decir que x = x / 2
print("el nuevo valor despues de la asignacion de division es de:", x)

x %= 3 #Esto quiere decir que x = x % 3
print("el nuevo valor despues de la asignacion de modulo o resto es de:", x)

x **= 2 #Esto quiere decir que x = x ** 2
print("El nuevo valor después de la asignacion de potencia es de:", x)

x //= 3 #Esto quiere decir que x = x // 3
print("el nuevo valor despues de la asignacion de division entera es de:", x)

#---------------------------------operadores de comparación

#estos operadores nos ayudan a comparar dos valores y nos devuelven un valor booleano (true p False)

#igual que 
print(3 == 6) #esto nos devuelve false
print(5 == 5) #esto nos devuelve true

#diferente que o no es igual que 
print(3 != 6)# esto nos devuelve true
print(5 != 5) #esto nos devuelve false

#mayor que >
print(7 > 4) #esto nos devuelve true
print(2 > 5) #esto nos devuelve false

#menor que <
print(3 < 8) #esto nos devuelve true
print(9 < 4) #esto nos devuelve false

#mayor o igual que >= 
print(6 >= 6) #esto nos devuelve true
print(10 >= 2) #esto nos devuelve true
print(5 >= 9) #esto nos devuelve false

#menor o igual que <=
print(4 <= 7) #esto nos devuelve true
print(4 <= 4) #esto nos devuelve true
print(8 <= 3) #esto nos devuelve false

#---------------------------------Operadores lógicos
#estos operadores nos ayudan a combinar expresiones booleanas y nos devuelven un valor booleano (true o false)

#operador and
print(5 > 3 and 8 < 5) #el and solo nos devuelve true si ambas expresiones son true, en este caso nos devuelve false
print(7 >= 2 and 4 != 1) #en este caso las dos expresiones se cumplen por lo tanto es true

#operador or
print(6 < 2 or 9 == 9) #el or nos devuelve true si al menos una de las expresiones es true, en este caso nos devuelve true
print(3 > 5 or 4 < 1) #en este caso ambas expresiones son falsas por lo tanto nos devuelve false

#operador not
#ivierte el resultado devuelve false si el resultado es verdadero y viceversa
print(not(5 > 2)) #en este caso la expresión es verdadera pero el not la invierte y nos devuelve false

#---------------------------------Operadores de identidad
#Comparan si dos objetos son el mismo objeto en memoria 

#operador is
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y) #esto nos devuelve false por qeu aunque las dos variables tienen el mismo contenido no son el mismo objeto en memoria
print(x is z) #esto nos devuelve true por que z es una referencia a x, por lo tanto sone el mismo objeto en memoria

# no se puede confundircon el operador de igualdad (==) que compara los valores de los objetos

#operador is not
print (x is not y) #esto nos devuelve true por que y y x no son el mismo objeto en memoria
print(x is not z) #esto nos devuelve false por que x y z son el mismo objeto en memoria

#---------------------------------Operadores de pertenencia
#se utiliza para comprobar si una secuencia (como lista, tupla o cadena) conteine un valor especifico

#operador in
frutas = ["manzana", "banana", "cereza"]
print("banana" in frutas) #esto nos devuelve true por que banana esta en la lita de frutas
print("pera" in frutas) #esto nos devuelve false por que pera no esta en la lista de frutas

#operador not in 
print("pera" not in frutas) #esto nos devuelve true por que pera no esta en la lista de frutas
print("manzana" not in frutas) #esto nos devuelve false por que manzana si esta en la lista de frutas

#---------------------------------Operadores bit a bit
#estos operadores trabajan a nivel de bits y se utilizan principalmente en operaciones de bajo nivel
a = 60 # en binario es 0011 1100
b = 13 # en binario es 0000 1101
#operador AND (&)
#compara cada bit de dos números y devuelve 1 si ambos bits son 1, de lo contrario devuelve 0
print("El resultado de a & b es:", a & b, bin(a & b)) #esto nos devuelve 12 que en binario es 0000 1100

#operador OR (|)
#compara cada bit de dos números y devuelve 1 si al menos uno de los bits es 1, de lo contrario devuelve 0
print("el resultado de a | b es:", a | b, bin(a | b)) #esto nos devuelve 61 que en binario es 0011 1101

#operador XOR (^)
#compara cada bit de dos números y devuelve 1 si los bits son diferentes, de lo contrario devuelve 0
print("el resultado de a ^ b es:", a ^ b, bin(a ^ b)) #esto nos devuelve 49 que en binario es 0011 0001

#operador NOT (~)
#ivierte todos los bits de un número, convirtiendo los 1 en 0 y los 0 en 1
print("el resultado de ~a es:", ~a, bin(~a)) #esto nos devuelve -61 que en binario es -0011 1101

#operador de desplazamiento a la izquierda (<<)
#desplaza los bits de un número hacia la izquierda un número espcificado de posiciones, llenando los bits vacíos con 0
print("el resultado de a << 2 es:", a << 2, bin(a << 2)) #esto nos devuelve 240 que en binario es 1111 0000
#operador de desplazamiento a la derecha (>>)
#desplaza los bits de un número hacia la derecha un número especificado de posiciones, llenando los bits vacíos con 0
print("el resultado de a >> 2 es:", a >> 2, bin(a >> 2)) #esto nos devuelve 15 que en binario es 0000 1111

#----------------------------------------------estructuras condicionales
#las estructuras condicionales nos permiten ejecutar diferentes bloques de código en función de si una condición es verdadera
# o falsa

#estructura if
#si la condición es verdadera (true) se ejecuta el bloque de código indentado
edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("eres mayor de edad") 

#estructura if-else
#si la condicion es verdadera (true) se ejecuta el primer bloque de código indentado
#si la condición es flasa (false) se ejecuta el segundo bloque de código indentado
if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")

#estructura if-elif-else
#si la primera condición es verdadera (true) se ejecuta el primer bloque de codigo indentado 
#si la primera condicion es false (false) se evalua la segunda condición
#si la segunda condicion es verdadera (true) se ejecuta el segundo bloque de código indentado
#si la segunda condición es falsa (false) se ejecuta el bloque de codigo indentado del else
if edad < 0:
    print("la edad no puede ser negativa")
elif edad < 18:
    print("eres menor de edad")
else:
    print("eres mayor de edad")


# ahora creare un ejemplo que dira si un numero es positivo, negativo o cero
num = float(input("introduce un número:"))

if num > 0:
	print("El Número es positivo")
elif num < 0:
	print("El Número es negativo")
else:
 	print("El Numero es cero")

#----------------------------------------------estructuras repetitivas
#las estructuras repetitivas nos permiten ejecutar un bloque de código varias veces mientras una condición sea verdadera (true)

#estructura for

#El bucle for se utiliza para iterar sobre una secuenca (listas, tuplas, diccionarios , cadenas de texto o  rangos) 
#y ejecutar el bloque de codigo una vez por cada elemento de esa secuencia 

frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
     print(f"me gusta la {fruta}")

#estructura for con la funcion range()
#Si se necesita repetir una accion un numero fijo de veces pero no estas recorriendo una lista usas la funcion range()

for i in range(1, 4):
     print(f"repeticion numero {i}")

#ejercicios for

#1
numeros = [12, 45, 23, 67, 34, 89, 90]

suma = 0

for num in numeros:
     suma = suma + num

print("el resultado de la suma es:", suma)

#2

frase = str(input("escribe una frase:"))

contador = 0

for voca in frase:
    if voca == "a":
        contador += 1

    elif voca == "e":
        contador += 1

    elif voca == "i":
        contador +=1

    elif voca == "o":
        contador += 1

    elif voca == "u":
        contador += 1

print("el numero de vocales es:", contador)

for i in range(1, 11):
     print(i * 3)

#estructura while
contador = 1
while contador <= 5:
    print(f"contador es igual a: {contador}")
    contador += 1
#el bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera (true)

#ejemplo entrada de usuario

password = ""

while password != "hola123":
    password = input("introduce tu contraseña:")
    if password != "hola123":
        print("contraseña incorrecta")

print("acceso concedido")

#while 1

tiempo = 6

while tiempo != 1:
    tiempo -= 1
    print(tiempo)

print("lanzamiento")

#control avanzado de bucles
#break
#la instruccion break se utiliza para salir de un bucle antes de que la condición del bucle sea falsa (false)

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for num in numeros:
    if num > 50:
        print("Se ha encontrado un numero mayor a 50 que es:", num)
        break
    print("procesando", num)

#continue
#la instruccion continue se utiliza para saltar a la siguiente iteración del bucle sin ejecutar el código restante en la iteración actual

entrada = input("Escribe una lista de números separados por comas: ")
numeros = list(map(int, entrada.split(',')))
print(numeros)


for num in numeros:
     if num % 2 != 0:
        continue
     print("El numero es par", num)


"""Ejercicio 4: Cuenta Regresiva
Concepto: Bucle while simple y modificación de la variable de control.

Instrucción: Inicializa una variable tiempo = 5. 
Usa un bucle while para hacer una cuenta regresiva que imprima los números 5, 4, 3, 2, 1, y luego imprima ¡Lanzamiento!. """
tiempo = 5 
while tiempo != 1:
     tiempo -= 1
     print(tiempo)
if  tiempo == 1: 
         print("TU CULO EXPLOTO")
    




#Validación de Pin

pin = ""

while pin != "1234":
    pin = input("ingrese su pin:")
    if pin == "1234":
        print("PIN correcto")
        break
    else:
        print("Pin incorrecto, Intentalo de nuevo")

#Adivinar Multiplos

"""Concepto: Controlar la repetición hasta que se cumple un criterio numérico.


Instrucción: Pide al usuario que ingrese números repetidamente. 
El bucle debe continuar mientras el número ingresado no sea un múltiplo de 7. 
Una vez que ingrese un múltiplo de 7, el bucle debe terminar."""
# Miguel el genio g
  

#Sebastián

multi = 0

while multi == 0:
    multi = int(input("ingrese su numero"))

    if multi % 7 == 0:
        print("su numero es multiplo de 7")
        break
    
     
print("penes a domicilio ")