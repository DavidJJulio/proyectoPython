import os
import json
os.system('clear')
Campers = ("""

- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - CAMPERS - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
1. CREAR CAMPER                 2. BUSCAR CAMPER
3. ACTUALIZAR CAMPER            3. ELIMINAR CAMPER
""")

def sistemac():
 os.system('clear')
 bandera = True
 while bandera:
        print(Campers)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 1: 
          crearcamper()
         case 2:
          buscarcamper()
         case 3:
          actualizarcamper()
         case 4:
          eliminarcamper()




def crearcamper():
    return 0
def buscarcamper():
    return 0
def actualizarcamper():
    return 0
def eliminarcamper():
    return 0

