import os
import json
from Modulos import funciones
os.system('clear')
Campers = ("""

- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - CAMPERS - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
1. CREAR CAMPER                 2. BUSCAR CAMPER
3. ACTUALIZAR CAMPER            4. ELIMINAR CAMPER
5. SALIR
""")

def sistemac():
 bandera = True
 while bandera:
        os.system('clear')
        print(Campers)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 1: 
          funciones.crearcamper()
         # case 2:
         #  buscarcamper()
         # case 3:
         #  actualizarcamper()
         # case 4:
         #  eliminarcamper()
         # case 5: 
         #  bandera = False




        


