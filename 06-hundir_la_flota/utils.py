import numpy 
import random

def crear_tablero(tamaño:int = 10) -> numpy.ndarray:
    
    tablero=numpy.full((tamaño,tamaño), "_", dtype='<U1')
    return tablero
  
    
def crear_barco (eslora:int) -> list:
    
    orientacion_barco= random.choice(("Horizontal","Vertical"))
    if orientacion_barco == "Horizontal":
        barco=[(0, H) for H in range(eslora)]
    else:
        barco=[(V, 0) for V in range(eslora)]
    return barco


def colocar_barco(tablero:numpy.ndarray) -> numpy.ndarray:
    barco_1 = crear_barco(2)
    barco_2 = crear_barco(2)
    barco_3 = crear_barco(2)
    barco_4 = crear_barco(3)
    barco_5 = crear_barco(3)
    barco_6 = crear_barco(4)

    barcos = [barco_1, barco_2, barco_3, barco_4, barco_5, barco_6]
    tamano_tablero = len(tablero)
    max_intentos = 500

    for barco in barcos:
        tamano_barco = len(barco)
       
        direccion_barco = "V" if ( barco[0][0] != barco[1][0]) else "H"

        if direccion_barco == "H":
            intentos = 0
            while intentos < max_intentos:
                fila = random.randint(0, tamano_tablero - 1)
                col0 = random.randint(0, tamano_tablero - tamano_barco)

                if all(tablero[fila, col0 + j] == "_" for i, j in barco):
                    for i, j in barco:
                        tablero[fila, col0 + j] = "O"
                    break  # colocado este barco; pasa al siguiente
                intentos += 1
            else:
                print(f"Error el colocaccion de los barcos.")

        else:  # "V"
            intentos = 0
            while intentos < max_intentos:
                col = random.randint(0, tamano_tablero - 1)
                fila0 = random.randint(0, tamano_tablero - tamano_barco)

                if all(tablero[fila0 + i, col] == "_" for i, _ in barco):
                    for i, _ in barco:
                        tablero[fila0 + i, col] = "O"
                    break
                intentos += 1
            else:
                print(f"Error el colocaccion de los barcos.")


    return tablero


def disparar(casilla:tuple , tablero: numpy.ndarray) -> numpy.ndarray:
    
    i, j= casilla
    if tablero [i,j] != "_":
        tablero[i,j]= "X"
    else:
        tablero[i,j]="A"
        
    

    return tablero
    
    


