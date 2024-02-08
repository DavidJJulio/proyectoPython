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
Rutas = ("""
- - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - RUTAS - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - -
    1. CREAR MODULO     2. CREAR RUTA



 
         """)

def sistemaco():
 bandera = True
 while bandera:
        os.system('clear')
        print(Coordinacion)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 1: 
              os.system('clear')
              print(Rutas)
              opc1 = int(input("¿A que opcion desea ingresar?: "))
              match(opc1):
                   case 1:
                        funciones.crearmodulos()
                   case 2:
                        funciones.crearrutas()
         case 2: 
              funciones.asignarsalon()
            
    




