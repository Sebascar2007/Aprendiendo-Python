multi = int(input("ingrese un número: "))

while multi != 0:

    multi = multi % 7

    if multi != 0:
        multi = int(input("Ingrese otro número: "))
    else: 
        print("Tu número es multiplo de 7")  

while True:
    pin = int(input("Ingrese su pin: "))
    if pin == 1234:
        print("Pin correcto")
        break
    else:
        print("pin incorrecto, intente de nuevo")

nombres = ["Ana", "Beto", "Carlos", "Diana", "Elena"]

for nom in nombres:
    if nom == "Carlos":
        print(nom)
        break
    print(nom)


for i in range(1,16):
    if i % 3 == 0:
        continue
    else:
        print(i)

productos = ["Leche", "Pan", "Mantequilla", "Huevos"]

for nece in productos:
    if nece == "Mantequilla":
        print("La mantequilla ha sido encontrada")
        break
else:
    print("Mantequilla no esta en el inventario")


for x in range(10, 56):
    if x % 2 != 0 or x == 16 or x % 3 == 0:
        continue
    else:
        print(x) 


#estructura de control

#manejo de excepciones con try, except, finally

#el bloque try se utiliza para envolver el código que puede generar un error
#El bloque except se ejecuta solo si ocurre el error determinado ej: (ValueError)
#El bloque else se ejecuta si no ocurre ningun error 
#El bloque finally se ejecuta siempre, ocurra o no un error

while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        divi = num1 / num2
    except ValueError:
        print("Eso no es un numero")
        continue
    except ZeroDivisionError:
        print("No se puede dividir entre 0, ingrese otro número")
        continue
    else:
        print(f"la division fue exitosa, {divi} es tu numero")
        break
    finally:
        print("Operación finalizada")



frutas = ["manzana", "pera", "naranja", "uva"]
contador = 0

for fruta in frutas:
    contador += 1
    print("Numero de producto actual", contador)

    while True:
        try:
            produ = int(input("Ingrese el numero de su producto (entre el 1 y el 4): "))
        except ValueError:
            print("Eso no es un número")
            continue
        if produ > len(frutas) or produ < 1:
            print("esta fuera de rango")
            continue
        elif produ != contador:
            break
        else:
            print("Tu producto es: ", fruta)
            break

    if produ != contador:
        continue

    break











