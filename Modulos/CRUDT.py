import os
import json
os.system('clear')
Horarios = ("  ---- HORARIOS LABORALES ----\n1. ---- 6:00 AM - 10:00 AM ----\n2. ---- 10:00 AM - 1:00 PM ----\n3. ---- 2:00 PM - 6:00 PM  ----\n4. ---- 6:00 PM - 10:00 PM ----")
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
 bandera = True
 while bandera:
        os.system('clear')
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
        x = len(Lista)
        os.system('clear')
        Lista.append({
           "Nombre" : input("Ingrese el nombre del Trainer: "),
           "Apellido" : input("Ingrese el apellido del Trainer: "),
           "Edad" : int(input("Ingrese la edad del Trainer: ")),
           "Genero" : input("Ingrese el genero del Trainer: "),
           "Numero" : [
              {
                 f"{'fijo' if(int(input('1.Fijo  0.Celular: ')))else 'Celular'}":
                    input(f'Numero de contacto {x+1}: ')
              }
              for x in range(int(input("¿Cuantos numeros de contacto tiene?: ")))
           ],
           "Estado" : "",
           "id" : int(input("Ingrese el numero de identidad del Trainer: ")),
           "Horario" : [    
                            input("\n\n\n\n  ---- HORARIOS LABORALES ----\n1. ---- 6:00 AM - 10:00 AM ----\n2. ---- 10:00 AM - 1:00 PM ----\n3. ---- 2:00 PM - 6:00 PM  ----\n4. ---- 6:00 PM - 10:00 PM ----\n\n  Seleccione un horario: ") 
                            for i in range(int(input("Cuantas jornadas trabajará el trainer? (1 Jornada = 4 horas): ")))
           ]
        })


    with open('JsonTrainers.json', 'w') as file:
        json.dump(Lista, file, indent = 4)
        file.close()
def buscartrainer():
           with open('JsonTrainers.json', 'r') as f:
            Lista = json.loads(f.read())
            x = len(Lista)
            f.close()


           for i, item in enumerate(Lista):
            print(f"""
--------------
{Lista[i]["Nombre"]} {Lista[i]["Apellido"]}
{Lista[i]["Edad"]} Años, id {Lista[i]["id"]}
Genero {Lista[i]["Genero"]} 
Numero {Lista[i]["Numero"]}
--------------

""")
           i+=1


           busqueda = (input("Ingrese el id del trainer: "))
           if busqueda == Lista[x-1]["id"]:
            os.system('clear')
            for i,val in Lista[x-1].items():
              print(f"""
--------------
{Lista[i]["Nombre"]} {Lista[i]["Apellido"]}
{Lista[i]["Edad"]} Años, id {Lista[i]["id"]}
Genero {Lista[i]["Genero"]} 
Numero {Lista[i]["Numero"]}
--------------""")
              x = input("")
           else:
            print("No existe este trainer")
            x = input("")
    
def actualizartrainer():
           with open('JsonTrainers.json', 'r') as f:
            Lista = json.loads(f.read())
            x = len(Lista)
            f.close()


           for i, item in enumerate(Lista):
            print(f"""
--------------
{Lista[i]["Nombre"]} {Lista[i]["Apellido"]}
{Lista[i]["Edad"]} Años, id {Lista[i]["id"]}
Genero {Lista[i]["Genero"]} 
Numero {Lista[i]["Numero"]}
--------------

""")
           i+=1


           busqueda = int((input("Ingrese el id del trainer: ")))
           if busqueda == Lista[x-1]["id"]:
            os.system('clear')
            for i,val in Lista[x-1].items():
              print(f"""
--------------
{Lista[i]["Nombre"]} {Lista[i]["Apellido"]}
{Lista[i]["Edad"]} Años, id {Lista[i]["id"]}
Genero {Lista[i]["Genero"]} 
Numero {Lista[i]["Numero"]}
--------------""")
              x = input("")
           else:
            print("No existe este trainer")
def eliminartrainer():
    return 0
