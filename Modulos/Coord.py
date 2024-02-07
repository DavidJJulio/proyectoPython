import os
import json
from Modulos import funciones
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
 bandera = True
 while bandera:
        os.system('clear')
        print(Coordinacion)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 1: 
              funciones.crearmodulos()
         case 2: 
              pass
            
    




