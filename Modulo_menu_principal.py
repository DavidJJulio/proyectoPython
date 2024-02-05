import os
from Modulos import CRUDC, CRUDT, Coord
import json
os.system('clear')

Portada = ("""
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - CAMPUSLANDS - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
           

           
        1. COORDINACIÓN    2. CAMPERS     
        3. TRAINERS        4. GUIA DE USO

""")





def portada():
 os.system('clear')
 bandera = True
 while bandera:
        print(Portada)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 3: 
          CRUDC.sistemac()
         case 2:
          CRUDT.sistemat()
         case 1:
          Coord.sistemaco()
         case 4:
          pass


