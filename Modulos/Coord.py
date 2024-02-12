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
1. ASIGNAR SALON CAMPER             2. PRUEBAS DE ADMISION
3. ASIGNAR SALON TRAINER            4. FILTROS
5. CAMPERS RIESGO                   5. SALIR



 
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
                                   funciones.saloncamper()
                              case 2:
                                   os.system('clear')
                                   funciones.prueba_admision()
                              case 3:
                                   funciones.salontrainer()
                              case 4:
                                   funciones.filtros()
                              case 5:
                                   funciones.campersriesgo()
                              case 6:
                                   bandera = False
                    except:
                         print(ValueError)
               case 3:
                    os.system('clear')
                    funciones.rep1()
                    funciones.rep2()
                    funciones.rep3()
                    funciones.rep4()
                    funciones.rep5()
                    funciones.rep6()
                    
               case 4:
                    bandera = False
                    
     except:
          print(ValueError)
    




