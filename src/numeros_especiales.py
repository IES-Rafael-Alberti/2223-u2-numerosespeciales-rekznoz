

def par_o_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def sumar_pares(numero_1, numero_2):
    suma = 0
    for numero in range(numero_1, numero_2 + 1):
        if par_o_impar(numero):
            suma += numero
    return suma

def sumar_impares(numero_1, numero_2):
    suma = 0
    for numero in range(numero_1, numero_2 + 1):
        if not par_o_impar(numero):
            suma += numero
    return suma

if __name__ == "__main__":

    numero_1 = 0
    numero_2 = 0

    try:
        numero_1 = int(input("Primero Numero "))
    except ValueError:
        if (numero_1 == None):
            print('Introduzce un numero')
        else:
            print('El Primer numero no es correcto')

    try:
        numero_2 = int(input("Segundo Numero "))
    except ValueError:
        if (numero_2 == None):
            print('Introduzce un numero')
        else:
            print('El Segundo numero no es correcto')

    verificacion = False
    while not verificacion:
        par_impar = input("¿Desea calcular la suma de pares o impares? (pares/impares) ")

        if par_impar == "pares" or par_impar == "impares":
            verificacion == True

    if verificacion:

        if par_impar == "pares":
            sumapares = sumar_pares(numero_1, numero_2)
            print("La suma de los números pares son", sumapares)
        else:
            sumaimpares = sumar_pares(numero_1, numero_2)
            print("La suma de los números impares son", sumaimpares)
    else:
        print("El programa tiene algun error de datos")