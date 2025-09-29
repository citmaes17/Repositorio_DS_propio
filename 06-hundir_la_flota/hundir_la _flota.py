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

def colocar_barco(barco:list, tablero:numpy.ndarray) -> None:
    
    tamaño_tablero= len(tablero)
    tamaño_barco= len(barco)
    
    
    
    
    
    
    
print(crear_tablero(7))
print(crear_barco(4))

#def colocar_barco(barco:list, tablero:list) -> None:
    
    


