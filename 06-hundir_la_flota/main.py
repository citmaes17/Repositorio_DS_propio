import utils
import random
import time


vidas= 10

tablero_juego= utils.crear_tablero(10)
print(tablero_juego)
print()
print()
tablero_juego= utils.colocar_barco(tablero_juego)
print(tablero_juego)
print()
print()
nfilas, ncols = tablero_juego.shape
disparos_hechos = set()

while vidas != 0:
    
    x=random.randint(0,nfilas-1)
    y=random.randint(0,ncols-1)
    if (x, y) in disparos_hechos:
        continue
    
    disparos_hechos.add((x, y))    
    
    tablero_juego= utils.disparar((x,y), tablero_juego)
    
    print(f"Disparo a ({x}, {y})")
    
    print(tablero_juego)
    print()
    print()
    vidas -= 1 
    time.sleep(5)