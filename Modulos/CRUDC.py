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
1. CREAR CAMPER                 2. ELIMINAR CAMPER
3. ACTUALIZAR CAMPER            4. SALIR
""")

def sistemac():
 bandera = True
 while bandera:
        os.system('clear')
        print(Campers)
        try:
            opc = int(input("¿A que opcion desea ingresar?: "))
            match(opc):
                  case 1: 
                     funciones.crearcamper()
                  case 2:
                     funciones.eliminarcamper()
                  case 3:
                     funciones.actualizarcamper()
                  case 4:
                     bandera = False

        except: 
         print("Ingrese un numero no un caracter.")


        


