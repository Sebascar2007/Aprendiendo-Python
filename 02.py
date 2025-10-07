# Aprendiendo sobre las funciones en python

# ---------------------------------------Funciones sin parametros ni retorno

""" Este tipo de fncion es el mas simple, solo ejecuta una tarea o un conjunto de instrucciones predefinidas
y no necesita ninguna informacon externa para operar."""

#sintaxis, se define con la palabra clave def, seguida del nombre de la funcion en parentesis
# su funcion solo realiza una accion

def dar_bienbenida():
    # El código dentro de la función dse ejecuta cuando se llama la funcion
    print("-----------------------------")
    print("hola, bienbenido a mi programa")
    print("-----------------------------")

#llamado a la funcion
dar_bienbenida()

# --------------------------------------Funcion con uno o vario parametros (argumentos)

""" Una funcion con parametros necesita informacion externa para realizar su trabajo.
los parametros son variables definidas en la funcion que actuan como (contenedores) para los datos que les pasaras 
cuando la llames 

sintaxis: los nombres de las bariables se colocan dentro de los parantesis ()

funcion: utiliza los datos proporcionados para personalizar su accion.

"""
def saludar_persona(nombre):
    #esta funcion saluda a la persona usando el nombre proporcionado
    print("hola,", nombre ,"! es un placer verte.")

saludar_persona("Miguel")

#ejemplo de funcion con varios parametros

def sumar_numeros(a, b):
    #suma dos números e imprime resultado.
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")

sumar_numeros(15, 45)

#-------------------------------------------Funcion con retorno (Retorno de valor)
"""Las funciones con retorno no solo ejecutan código, sion que también devuelven un valor a la parte del código que las 
llamo. ESto se hace usando la palabra clave (return). Esto permite usar el resultado de la funcion 
en otras partes del programa.

sintaxis: Se la palabra calve return seguida del valor o expresion que se desea devolver

funcion: La funcion actua como una formula o calculo, y el valor de retorno es el resultado de esa formula
"""

def calcular_area_rectangulo(largo, ancho):
    area = largo * ancho
    return area
     #el valor de area se devuelve

#1. llamaar la funcion y guardar el valor retornado en una variable
area_sala = calcular_area_rectangulo(10, 5)

#2. Usar el valor retornado en otro calculo o impresion
costo_total = area_sala * 50 #50 es el costo por metro cuadrado

print(f"el area de la sala es: {area_sala}")
print(f"el costo de la sala es: ${costo_total}")


#------------------------------------- Ejercicios sin parametros ni retorno

"""
Ejercicio 1: 

Mensaje de Créditos

Instrucción: Define una función llamada mostrar_creditos que simplemente imprima en la consola tres líneas 
con información ficticia del desarrollador 
(ej: "Desarrollado por [Tu Nombre]", "Versión 1.0", "Fecha: 2025"). Llama a la función una vez.

Ejercicio 2: 

Dibujar un Separador

Instrucción: Define una función llamada dibujar_separador que imprima una línea de guiones o asteriscos 
(ej: ***********) para separar secciones de texto.
 Llama a la función antes y después de un mensaje de bienvenida simple.

"""
#sebastian
def mostrar_creditos():
    print("--------------------------------------------------------------------")
    print("Desarrollado por Sebastián Cardona, Version 1.0, fecha: 2025).")
    print("--------------------------------------------------------------------")

mostrar_creditos()

def dibujar_separador():
    print("************************************************")

dibujar_separador()
#Miguel

#------------------------------------- Ejercicios Función con Parámetros (Sin Retorno)

"""

Ejercicio 3: 

Imprimir Ficha

Instrucción: Define una función llamada imprimir_ficha que acepte dos parámetros: nombre y puesto. 
La función debe imprimir un mensaje formateado usando ambos datos.

Ejemplo de llamada: imprimir_ficha("Ricardo", "Gerente de Ventas")

Ejercicio 4: 

Verificador de Límite

Instrucción: Define una función llamada verificar_limite que acepte un parámetro valor
y otro limite. La función debe imprimir si el valor es mayor que el limite o no.

Ejemplo de lógica: Si valor > limite, imprime "Valor excede el límite". Si no, imprime "Valor dentro del límite".

"""

#Sebastián 

def imprimir_ficha(nombre, puesto):
    print(f"Nombre:{nombre} | Su puesto es: {puesto}")

imprimir_ficha("Sebastián", "Gerente")

def verificar_limite(valor, limite):
    if valor > limite:
        print("valor excede el limite")
    elif valor < limite:
        print("El valor esta dentro del limite")
    else:
        print("El valor es igual al limite")

verificar_limite(32, 62)
#Miguel

#------------------------------------- Ejercicios Función con Retorno

"""

Ejercicio 5: 

Cálculo de IVA
Instrucción: Define una función llamada calcular_iva que acepte un parámetro precio_base. 
La función debe calcular el 21% de ese precio y retornar el monto del IVA.

Uso del resultado: Llama a la función y guarda el resultado en una variable llamada monto_iva.
Luego, suma precio_base y monto_iva para obtener el precio final e imprímelo.

Ejercicio 6: 

Longitud de Palabra
Instrucción: Define una función llamada obtener_longitud que acepte un parámetro palabra. 
La función debe usar la función incorporada len() y retornar la longitud de esa palabra.

Uso del resultado: Llama a la función pasando una palabra (ej: "Python")
e imprime un mensaje que diga si la palabra es "larga" (si la longitud es mayor a 5) 
o "corta" (si es 5 o menos), usando el valor de retorno.

Ejercicio 7: 

Conversor de Temperatura (Múltiples Parámetros y Retorno)
Instrucción: Define una función llamada celsius_a_fahrenheit que acepte un parámetro celsius. 
La función debe convertir la temperatura a Fahrenheit usando la fórmula:
F=(C x 9/5)+32
Retorno: La función debe retornar el valor de F.
Llama a la función con el valor 25 y guarda el resultado para imprimirlo.

"""
#Sebastián

def calcular_iva(precio_base):
    iva = precio_base * 0.21
    return iva

monto_iva = calcular_iva(21000)

produ_iva = monto_iva + 21000

print("tu producto con iva tiene un costo de: ", produ_iva)
#Miguel

