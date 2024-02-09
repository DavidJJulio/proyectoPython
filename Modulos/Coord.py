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
    3. SALIR



 
         """)

Administracion = ("""
- - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - -
- - - - - - - ADMINISTRACION - - - - - --
- - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - -
1. GESTION SALONES             2. FILTROS
3. SALIR



 
         """)

def sistemaco():
 bandera = True
 while bandera:
     os.system('clear')
     print(Coordinacion)
     try:
          opc = int(input("¿A que opcion desea ingresar?: "))
          match(opc):
               case 1: 
                    os.system('clear')
                    print(Rutas)
                    try:
                         opc1 = int(input("¿A que opcion desea ingresar?: "))
                         match(opc1):
                              case 1:
                                   os.system('clear')
                                   funciones.crearmodulos()
                              case 2:
                                   os.system('clear')
                                   funciones.crearrutas()
                              case 3:
                                   bandera = False
                    except:
                         print("")
               case 2: 
                    os.system('clear')
                    print(Administracion)
                    try:
                         opc2 = int(input("A que opcion desea ingresar?: "))
                         match(opc2):
                              case 1:
                                   os.system('clear')
                                   funciones.salon()
                              case 2:
                                   os.system('clear')
                                   funciones.filtros()
                              case 3:
                                   bandera = False
                    except:
                         print(ValueError)
               case 3:
                    os.system('clear')
                    pass
               case 4:
                    bandera = False
                    
     except:
          print(ValueError)
    




