import os
import json
os.system('clear')
Campers = ("""

- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - CAMPERS - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
1. CREAR CAMPER                 2. BUSCAR CAMPER
3. ACTUALIZAR CAMPER            4. ELIMINAR CAMPER
5. SALIR
""")

def sistemac():
 os.system('clear')
 bandera = True
 while bandera:
        print(Campers)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 1: 
          crearcamper()
         case 2:
          buscarcamper()
         case 3:
          actualizarcamper()
         case 4:
          eliminarcamper()
         case 5: 
          bandera = False



def crearcamper():
    with open('JsonCampers.json', 'r') as f:
        Lista = json.loads(f.read())
        print(type(Lista))
        x = len(Lista)
        Lista.append({
           "Nombre" : input("Ingrese el nombre del Camper: "),
           "Apellido" : input("Ingrese el apellido del Camper: "),
           "Edad" : int(input("Ingrese la edad del Camper: ")),
           "Genero" : input("Ingrese el genero del Camper: "),
           "Numero" : [
              {
                 f"{'fijo' if(int(input('1.Fijo  0.Celular: ')))else 'Celular'}":
                    input(f'Numero de contacto {x+1}: ')
              }
              for x in range((int(input("¿Cuantos numeros de contacto tiene?: "))))
           ],
           "Estado" : input("Ingrese el estado del Camper: "),
           "Codigo" : x + 1
        })
        if Lista[x]["Edad"] < 18:
           Lista[x].update({
              "Acudiente" : input("Ingrese el nombre de su acudiente: "),
              "CelAcudiente" : input("Ingrese el numero telefonico de el acudiente: ")
              })
        
    with open('JsonCampers.json', 'w') as file:
        json.dump(Lista, file, indent = 4)
        file.close()
        
def buscarcamper():
    return 0
def actualizarcamper():
    return 0
def eliminarcamper():
    return 0

