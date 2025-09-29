import math


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def area_cuadrado(lado: float) -> float:
    return lado ** 2

def area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

def area_circulo(radio: float) -> float:
    return math.pi * (radio ** 2)

def contar_letras(texto: str, letra: str) -> int:
    texto = texto.lower()
    letra = letra.lower()
    return texto.count(letra)

def contar_todas_letras(texto: str) -> dict:
    dic = {}
    for caracter in texto:
        dic[caracter] = dic.get(caracter, 0) + 1
    return dic

def numeros_a_dias(numero):
    match numero:
        case 1:
            return  "Lunes"
        case 2:
            return  "Martes"
        case 3:
            return  "Miercoles"
        case 4:
            return  "Jueves"
        case 5:
            return  "Viernes"
        case 6:
            return  "Sabado"
        case 7:
            return  "Domingo"

def piramide_invertida(filas: int) :
    for i in range(filas, 0, -1):        
        for j in range(i, 0, -1):        
            print(j, end=" ")
        print()  
        
def comparar_numeros(a: int, b: int) -> str:
    if a == b:
        return "Los números son iguales"
    elif a > b:
        return "El primero es mayor que el segundo"
    else:
        return "El segundo es mayor que el primero"
    
def modificar_lista(lista: list, comando: str, elemento=None) -> list:
    if comando == "add":
        if elemento is not None:
            lista.append(elemento)
    elif comando == "remove":
        if elemento in lista:
            lista.remove(elemento)
    else:
        print("Comando no válido. Usa 'add' o 'remove'.")
    return lista

def formar_frase(*palabras) -> str:
    return " ".join(palabras)