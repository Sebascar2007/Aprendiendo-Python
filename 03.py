#------------------------Estructuras de datos basicas de Python

#------------cadenas string(str)

mensaje = "Hola Mundo"
print(mensaje)
#Se usan para representar texto, estas son inmutables, es decir, no se pueden modificar una vez creadas

#------------Listas (list)

frutas = ["manzana", "banana", "cereza"]
print(frutas)
frutas.append("naranja") #agregar elemento
print(frutas)

#Son colecciones ordenadas y mutables de elementos. Permniten elementos duplicados y de distintos tipos.

#------------Tuplas (tuple)

coordenadas = (10, 20)
print(coordenadas)

#Son colecciones ordenadas e inmutables. Se usan cuando no quieres que los datos cambien 

#------------Conjuntos (set)
numeros = {1, 2, 3, 3, 2}
print(numeros)
numeros.add(4)
print(numeros)
#Son colecciones desordenadas sin elementos duplicados. Muy útiles para eliminar duplicado
# y hacer operaciones matemáticas (unión, intersección, etc.)

#------------Diccionarios(dict)
persona = {
    "nombre": "sebas", 
    "edad": 25, 
    "ciudad": "Medellín"
    }

print(persona["nombre"])
persona["edad"] = 26
print(persona)

#Son colecciones de pares clave: valor. Parecido a un JSON. Muy usado para almacenar datos estructurados.

#------------Booleanos (bool)
activo = True
print(activo)

if activo:
    print("El usuario esta activo")

#Solo pueden tener dos valores: True o False.

#------------Números (int, float, complex)
entero = 10 #int
decimal = 3.14 #float
complejo = 2 + 3j #complex

print(entero, decimal, complejo)

#------------NoneType

resultado = None
print(resultado)
#Representa la ausencia de valor (similar a null en otros leguajes)
