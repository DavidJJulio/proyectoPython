import os
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

Coordinacion = ("""

-- - - - - - - - - - - - - - - - - - - - - - - --
-- - - - - - - - - - - - - - - - - - - - - - - --
- - - - - - - - - COORDINACION - - - - - - - - --
-- - - - - - - - - - - - - - - - - - - - - - - --
-- - - - - - - - - - - - - - - - - - - - - - - --
        1. RUTAS            2.ADMINISTRACION
        3. INFORMES


""")

Campers = ("""

- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - CAMPERS - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
1. CREAR CAMPER                 2. BUSCAR CAMPER
3. ACTUALIZAR CAMPER            3. ELIMINAR CAMPER
""")

Trainers = ("""

- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - TRAINERS - - - - - - - - - --
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
1. CREAR TRAINER              2. BUSCAR TRAINER
3. ACTUALIZAR TRAINER         4. ELIMINAR TRAINER
""")
def portada():
 os.system('clear')
 bandera = True
 while bandera:
        print(Portada)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 1: 
          coordinacion()
         case 2:
          campers()
         case 3:
          trainers()
         case 4:
          pass



def campers():
 os.system('clear')
 bandera = True
 while bandera:
        print(Campers)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 1: 
          pass

def trainers():
 os.system('clear')
 bandera = True
 while bandera:
        print(Trainers)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 1: 
          pass

def coordinacion():
 os.system('clear')
 bandera = True
 while bandera:
        print(Coordinacion)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 1: 
          pass
    
       

