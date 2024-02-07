import os
import json
from Modulos import funciones 
os.system('clear')
Horarios = ("  ---- HORARIOS LABORALES ----\n1. ---- 6:00 AM - 10:00 AM ----\n2. ---- 10:00 AM - 1:00 PM ----\n3. ---- 2:00 PM - 6:00 PM  ----\n4. ---- 6:00 PM - 10:00 PM ----")
Trainers = ("""

- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - TRAINERS - - - - - - - - - --
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
1. CREAR TRAINER              2. ELIMINAR TRAINER
3. ACTUALIZAR TRAINER         4. SALIR
""")

def sistemat():
 bandera = True
 while bandera:
        os.system('clear')
        print(Trainers)
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
            
    
