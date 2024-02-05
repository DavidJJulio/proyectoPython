import os
import json
os.system('clear')
Coordinacion = ("""

-- - - - - - - - - - - - - - - - - - - - - - - --
-- - - - - - - - - - - - - - - - - - - - - - - --
- - - - - - - - - COORDINACION - - - - - - - - --
-- - - - - - - - - - - - - - - - - - - - - - - --
-- - - - - - - - - - - - - - - - - - - - - - - --
        1. RUTAS            2. ADMINISTRACION
        3. INFORMES         4. SALIR


""")

def sistemaco():
 os.system('clear')
 bandera = True
 while bandera:
        print(Coordinacion)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 1: 
          rutas()
         case 2:
          administracion()
         case 3:
          informes()
         case 4: bandera = False
    




def rutas():
    return 0
def administracion():
    return 0
def informes():
    return 0

