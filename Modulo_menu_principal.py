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
        3. TRAINERS        

""")





def portada():
 os.system('clear')
 bandera = True
 while bandera:
        os.system('clear')
        print(Portada)
        try:
                opc = int(input("¿A que opcion desea ingresar?: "))
                match(opc):
                        case 2:
                                CRUDC.sistemac()
                        case 3:
                                CRUDT.sistemat()
                        case 1:
                                Coord.sistemaco()
                        case 4:
                                pass
        except:
                print(ValueError)

