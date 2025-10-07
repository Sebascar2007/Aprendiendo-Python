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


#------------------------------------- Ejercicios

"""
Ejercicio 1: 

Mensaje de Créditos
Instrucción: Define una función llamada mostrar_creditos que simplemente imprima en la consola tres líneas 
con información ficticia del desarrollador 
(ej: "Desarrollado por [Tu Nombre]", "Versión 1.0", "Fecha: 2025"). Llama a la función una vez.
"""
#sebastian
def mostrar_creditos():
    print("--------------------------------------------------------------------")
    print("Desarrollado por Sebastián Cardona, Version 1.0, fecha: 2025).")
    print("--------------------------------------------------------------------")

mostrar_creditos()