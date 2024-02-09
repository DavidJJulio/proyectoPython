import json
import os
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
           "id" : int((input("Ingrese el numero de identidad del Trainer: "))),
           "Horario" : {
               "1" : True,
               "2" : True,
               "3" : True,
               "4" : True
           },
           "Salon" : "",
           "Ruta" : ""
        })


    with open('JsonTrainers.json', 'w') as file:
        json.dump(Lista, file, indent = 4)
        file.close()
def crearcamper():
    with open('JsonCampers.json', 'r') as f:
        Lista = json.loads(f.read())
        x = len(Lista)
        os.system('clear')
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
           "Estado" : "",
           "id" : int(input("Ingrese el numero de identidad del Camper: ")),
           "Salon" : "",
           "Trainer" : "",
           "Horario" : {
               "1" : True,
               "2" : True,
               "3" : True,
               "4" : True},
           "Ruta" : "",
           "Estado" : {
               "1" : False,
               "2" : False,
               "3" : False,
               "4" : False,
               "5" : False
           }
        })
        x = len(Lista)
        if Lista[x-1]["Edad"] < 18:
           Lista[x-1].update({
              "Acudiente" : input("Ingrese el nombre de su acudiente: "),
              "CelAcudiente" : input("Ingrese el numero telefonico de el acudiente: ")
              })

    with open('JsonCampers.json', 'w') as file:
        json.dump(Lista, file, indent = 4)
        file.close()
def eliminartrainer():
    bandera = True
    with open('JsonTrainers.json', 'r') as f:
        Lista = json.loads(f.read())
        os.system('clear')
        f.close()
        for i, item in enumerate(Lista):
            print(f"""
    ------------------
    {Lista[i]['Nombre']}, {Lista[i]['Apellido']}
    Edad {Lista[i]['Edad']}, {Lista[i]['id']}
    ------------------
    """)
        identificacion = int(input("Ingrese el id del trainer que desea eliminar: "))
        for i, item in enumerate(Lista):
            if(Lista[i]["id"] == identificacion):
                print(f"""
------------------
{Lista[i]['Nombre']}, {Lista[i]['Apellido']}
Edad {Lista[i]['Edad']}, {Lista[i]['id']}
------------------
""")
                try:
                    x = int(input("Desea eliminar este trainer?  1.Si  2.No: "))
                    if(x == 1):
                        del Lista[i]
                        print("Se ha eliminado correctamente")
                        x = input("Ingrese enter para continuar")
                    elif(x == 2):
                        bandera = False

                except:
                    print("No ingresó un numero valido.")
                    n = input("")
        
            else:
                    print("No existe este trainer")
                    n = input("")
                    bandera = False
    with open('JsonTrainers.json', 'w') as file:
            json.dump(Lista, file, indent=4)
            file.close()
def eliminarcamper():
    bandera = True
    with open('JsonCampers.json', 'r') as f:
        Lista = json.loads(f.read())
        os.system('clear')
        f.close()
        for i, item in enumerate(Lista):
            print(f"""
------------------
{Lista[i]['Nombre']}, {Lista[i]['Apellido']}
Edad {Lista[i]['Edad']}, {Lista[i]['id']}
------------------
""")
        identificacion = int(input("Ingrese el id del camper que desea eliminar: "))
        for i, item in enumerate(Lista):
            if(Lista[i]["id"] == identificacion):
                print(f"""
------------------
{Lista[i]['Nombre']}, {Lista[i]['Apellido']}
Edad {Lista[i]['Edad']}, {Lista[i]['id']}
------------------
""")
                try:
                    x = int(input("Desea eliminar este camper?  1.Si  2.No: "))
                    if(x == 1):
                        del Lista[i]
                    elif(x == 2):
                        bandera = False

                except:
                    print("No ingresó un numero valido.")
                    n = input("")
        
            else:
                    print("ok")
                    n = input("")
                    bandera = False
    with open('JsonCampers.json', 'w') as file:
            json.dump(Lista, file, indent=4)
            file.close()
def actualizartrainer():
    bandera = True
    with open('JsonTrainers.json', 'r') as f:
        Lista = json.loads(f.read())
        os.system('clear')
        f.close()
        for i, item in enumerate(Lista):
            print(f"""
    ------------------
    {Lista[i]['Nombre']}, {Lista[i]['Apellido']}
    Edad {Lista[i]['Edad']}, {Lista[i]['id']}
    ------------------
    """)
        identificacion = int(input("Ingrese el id del trainer que desea actualizar: "))
        for i, item in enumerate(Lista):
            if(Lista[i]["id"] == identificacion):
                print(f"""
------------------
{Lista[i]['Nombre']}, {Lista[i]['Apellido']}
Edad {Lista[i]['Edad']}, {Lista[i]['id']}
------------------
""")
                try:
                    x = int(input("Desea actualizar este Trainer?  1.Si  2.No: "))
                    if(x == 1):
                        del Lista[i]
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
           "id" : int((input("Ingrese el numero de identidad del Trainer: "))),
           "Horario" : {
               "1" : True,
               "2" : True,
               "3" : True,
               "4" : True
           },
           "Salon" : "",
           "Ruta" : ""
        })
                    elif(x == 2):
                        bandera = False

                except:
                    print("No ingresó un numero valido.")
                    n = input("")
        
            else:
                    print("ok")
                    n = input("")
                    bandera = False
    with open('JsonTrainers.json', 'w') as file:
            json.dump(Lista, file, indent=4)
            file.close()
def actualizarcamper():
    bandera = True
    with open('JsonCampers.json', 'r') as f:
        Lista = json.loads(f.read())
        os.system('clear')
        f.close()
    for i, item in enumerate(Lista):
            print(f"""
------------------
{Lista[i]['Nombre']}, {Lista[i]['Apellido']}
Edad {Lista[i]['Edad']}, {Lista[i]['id']}
------------------
""")
    identificacion = int(input("Ingrese el id del camper que desea actualizar: "))
    for i, item in enumerate(Lista):
            if(Lista[i]["id"] == identificacion):
                print(f"""
------------------
{Lista[i]['Nombre']}, {Lista[i]['Apellido']}
Edad {Lista[i]['Edad']}, {Lista[i]['id']}
------------------
""")
                try:
                    x = int(input("Desea actualizar este Camper?  1.Si  2.No: "))
                    if(x == 1):
                        del Lista[i]
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
           "Estado" : "",
           "id" : int(input("Ingrese el numero de identidad del Camper: ")),
           "Salon" : "",
           "Trainer" : "",
           "Horario" : {
               "1" : True, 
               "2" : True,
               "3" : True,
               "4" : True},
           "Ruta" : "",
           "Estado" : {
               "1" : False,
               "2" : False,
               "3" : False,
               "4" : False,
               "5" : False
           }
        })
                    elif(x == 2):
                        bandera = False

                except:
                    print("No ingresó un numero valido.")
                    n = input("")
        
            else:
                    print("ok")
                    n = input("")
                    bandera = False
    with open('JsonCampers.json', 'w') as file:
            json.dump(Lista, file, indent=4)
            file.close()
def crearmodulos():
            with open('JsonModulos.json', 'r') as f:
                Lista = json.loads(f.read())
                f.close()
                x = len(Lista)
                Lista.append({
                 "Nombre del modulo" : input("Ingrese el nombre del modulo: ").upper().replace(" ",""),
                 "Temas del modulo" : [
                           input(f"Ingrese el tema {i+1}: ")
                           for i in range(int(input("¿Cuantos temas tendra el modulo?: ")))
                 ],
                 "Codigo" : (x+1)
            })
            with open('JsonModulos.json', 'w') as file:
                 json.dump(Lista, file, indent=4) 
def crearrutas():
     n = 0
     with open('JsonModulos.json', 'r') as f:
         Modulos = json.loads(f.read())
         f.close()
         
     with open('JsonRutas.json', 'r') as f:
         Rutas = json.loads(f.read())
         f.close
     x = len(Rutas)
     print("""
---------------------------
----MODULOS DISPONIBLES----
---------------------------
           """)
     for i,item in enumerate(Modulos):
         n+=1
         print(f"""---------------------------
{n}.{Modulos[i]['Nombre del modulo']}""")
     Rutas.append(
         {
             "Nombre de la ruta" : 
input("""---------------------------
Ingrese el nombre de la ruta: """).upper().replace(" ",""),
             "Modulos" : [],
             "Codigo" : x+1
         }
     )
     z = 0
     for i in range(int(input("Cuantos modulos añadirá a la ruta?: "))):
        z +=1
        mod = int(input(f"Modulo n{z}: "))
        for i,item in enumerate(Modulos):
            if(mod == Modulos[i]["Codigo"]):
                Rutas[x]["Modulos"].append(Modulos[i])
     
     with open('JsonRutas.json', 'w') as file:
         json.dump(Rutas, file, indent=4)
     print(type(Rutas))
def salon():
     with open('JsonSalones.json', 'r') as f:
          Salones = json.loads(f.read())
          f.close()
     with open('JsonCampers.json', 'r') as f:
          Campers = json.loads(f.read())
          f.close()
     with open('JsonRutas.json', 'r') as f:
          Rutas = json.loads(f.read())
          f.close()
     with open('JsonTrainers.json', 'r') as f:
          Trainers = json.loads(f.read())
          f.close()
    
     

def filtros():
     pass
def notas():
     pass




