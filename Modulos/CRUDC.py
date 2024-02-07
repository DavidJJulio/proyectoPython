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
            if(4 >= opc > 0):
               match(opc):
                  case 1: 
                     funciones.creartrainer()
                  case 2:
                     funciones.eliminartrainer()
                  case 3:
                     funciones.actualizartrainer()
                  case 4:
                     bandera = False

        except: 
         print("Ingrese un numero no un caracter.")
         x = input("Enter para continuar...")



        


