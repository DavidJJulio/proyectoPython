import os
import json
os.system('clear')
Trainers = ("""

- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - TRAINERS - - - - - - - - - --
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
1. CREAR TRAINER              2. BUSCAR TRAINER
3. ACTUALIZAR TRAINER         4. ELIMINAR TRAINER
5. SALIR
""")

def sistemat():
 os.system('clear')
 bandera = True
 while bandera:
        print(Trainers)
        opc = int(input("¿A que opcion desea ingresar?: "))
        match(opc):
         case 1: 
          creartrainer()
         case 2:
          buscartrainer()
         case 3:
          actualizartrainer()
         case 4:
          eliminartrainer()
         case 5: 
          bandera = False
    
    


def creartrainer():
    with open('JsonTrainers.json', 'r') as f:
        Lista = json.loads(f.read())
        print(type(Lista))
        Lista.append({
           "Nombre" : input("Ingrese el nombre del trainer: "),
           "Apellido" : input("Ingrese el apellido del trainer: "),
           "Edad" : input("Ingrese la edad del trainer: "),
           "Genero" : input("Ingrese el genero del trainer: "),
           "Numero" : input("Ingrese el numero telefonico del trainer: ")
        })
        
    with open('JsonTrainers.json', 'w') as file:
        json.dump(Lista, file, indent = 4)
        file.close()


def buscartrainer():
    return 0
def actualizartrainer():
    return 0
def eliminartrainer():
    return 0
