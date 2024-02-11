import json
import os
def creartrainer():
    with open('JsonRutas.json', 'r') as f:
        Rutas = json.loads(f.read())
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
           "Salon" : [],
           "Ruta" : []
        })
    print(""")
-------------------------
----RUTAS DISPONIBLES----
-------------------------
           """)
    n=0
    for i,item in enumerate(Rutas):
         n+=1
         print(f"""---------------------------
{n}.{Rutas[i]['Nombre de la ruta']}""") 
    z = int(input("Ingrese el codigo de la ruta: "))
    for i, item in enumerate (Rutas):
        if Rutas[i]["Codigo"] == z:
            Lista[x-1]["Ruta"].append(z)
        else:
            print("Esta ruta no existe")
    with open('JsonTrainers.json', 'w') as file:
        json.dump(Lista, file, indent = 4)
        file.close()
def crearcamper():
    with open('JsonCampers.json', 'r') as f:
        Lista = json.loads(f.read())
        f.close()
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
        "id" : int(input("Ingrese el numero de identidad del Camper: ")),
        "Salon" : [],
        "Trainer" : [],
        "Horario" : {
            "1" : False,},
        "Ruta" : 0,
        "Estado" : {
            1 : False,
            2 : False,
            3 : False,
            4 : False,
            5 : False,
            6 : False,
            7 : False
        },
        "Riesgo" : 0
    })
    x = len(Lista)
    if Lista[x-1]["Edad"] < 18:
        Lista[x-1].update({
            "Acudiente" : input("Ingrese el nombre de su acudiente: "),
            "CelAcudiente" : input("Ingrese el numero telefonico de el acudiente: ")
            })
    n = int(input
("""
-------------
1. Inscrito
2. Aprobado
3. Cursando
4. Graduado
5. Expulsado
6. Retirado
-------------
Ingrese el estado del camper: 
"""))
    for i in Lista[x-1]["Estado"]:
        if n == i:
            Lista[x-1]["Estado"][i] = True
        
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
---------------------
{Lista[i]['Nombre']}, {Lista[i]['Apellido']}
Edad {Lista[i]['Edad']}, id {Lista[i]['id']}
---------------------
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
    os.system('clear')
    with open('JsonCampers.json', 'r') as f:
        Lista = json.loads(f.read())
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
---------------------
{Lista[i]['Nombre']}, {Lista[i]['Apellido']}
Edad {Lista[i]['Edad']}, id {Lista[i]['id']}
---------------------
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
                    print("Este camper no existe")
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
    with open('JsonRutas.json', 'r') as f:
        Rutas = json.loads(f.read())
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
---------------------
{Lista[i]['Nombre']}, {Lista[i]['Apellido']}
Edad {Lista[i]['Edad']}, id {Lista[i]['id']}
---------------------
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
           "Salon" : [],
           "Ruta" : []
        })
                        print(""")
                    -------------------------
                    ----RUTAS DISPONIBLES----
                    -------------------------
                            """)
                        n=0
                        for i,item in enumerate(Rutas):
                            n+=1
                            print(f"""---------------------------
                    {n}.{Rutas[i]['Nombre de la ruta']}""") 
                        z = int(input("Ingrese el codigo de la ruta: "))
                        for i, item in enumerate (Rutas):
                            if Rutas[i]["Codigo"] == z:
                                Lista[x-1]["Ruta"].append(z)
                            else:
                                print("Esta ruta no existe")
            
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
---------------------
{Lista[i]['Nombre']}, {Lista[i]['Apellido']}
Edad {Lista[i]['Edad']}, id {Lista[i]['id']}
---------------------
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
           "id" : int(input("Ingrese el numero de identidad del Camper: ")),
           "Salon" : [],
           "Trainer" : [],
           "Horario" : {
               "1" : False,},
           "Ruta" : 0,
           "Estado" : {
               1 : False,
               2 : False,
               3 : False,
               4 : False,
               5 : False,
               6 : False
           },
           "Riesgo" : 0
        })
                        x = len(Lista)
                        if Lista[x-1]["Edad"] < 18:
                            Lista[x-1].update({
                                "Acudiente" : input("Ingrese el nombre de su acudiente: "),
                                "CelAcudiente" : input("Ingrese el numero telefonico de el acudiente: ")
                                })
                        n = int(input
("""
 -------------
 1. Inscrito
 2. Aprobado
 3. Cursando
 4. Graduado
 5. Expulsado
 6. Retirado
 -------------
 Ingrese el estado del camper: 
 """))
                        for i in Lista[x-1]["Estado"]:
                            if n == i:
                                Lista[x-1]["Estado"][i] = True
        
        elif(x == 2):
            bandera = False
        else:
            print("ok")
            n = input("")
            bandera = False
    except:
        print("No ingresó un numero valido.")
        n = input("")
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
def saloncamper():
    with open('JsonSalones.json', 'r') as f:
          Salones = json.loads(f.read())
          f.close()
    with open('JsonCampers.json', 'r') as f:
          Campers = json.loads(f.read())
          f.close()
    with open('JsonTrainers.json', 'r') as f:
          Trainers = json.loads(f.read())
          f.close()
          
          
    print("""
---------------------------------------
-------Ingresar Camper al Salon-------
---------------------------------------

1. 6 AM - 10 PM
2. 10 AM - 2 PM
3. 2 PM - 6 PM
4. 6 PM - 10 PM

""")
    try:
        opc = int(input("Que horario desea?"))
        match(opc):
            case 1:
                os.system('clear')
                try:
                    print("""
        ----------------------------
            SALONES DISPONIBLES
        ----------------------------
        """)
                    for i,item in enumerate(Salones):
                        if Salones[i]["Trainer1"] == False:
                            n+=1
                            print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
---------------------""")
                except:
                    pass
            case 2:
                os.system('clear')
            case 3:
                os.system('clear')
            case 4:
                os.system('clear')
    except:
        print("Esa no es una opcion valida")                
                
                
    with open('JsonSalones.json', 'w') as f:
          json.dump(Salones, f, indent=4)
          f.close()
    with open('JsonCampers.json', 'w') as fire:
          json.dump(Campers, fire, indent=4)
          fire.close()
    with open('JsonTrainers.json', 'w') as fire:
          json.dump(Trainers, fire, indent=4)
          fire.close()
def prueba_admision():
    os.system('clear')
    with open('JsonCampers.json', 'r') as f:
        Campers = json.loads(f.read())
        f.close()
    for i, item in enumerate(Campers):
        if Campers[i]["Estado"]["1"] == True:
            print(f"""
---------------------
{Campers[i]['Nombre']}, {Campers[i]['Apellido']}
Edad {Campers[i]['Edad']}, id {Campers[i]['id']}
---------------------
""")
    p = int(input("A cual camper desea ingresarle notas del examen de admision?"))
    for i,item in enumerate(Campers):
        if (Campers[i]["id"] == p):
            if Campers[i]["Estado"]["1"] == True:
                o = int(input("Cual fue su puntaje en el examen"))
                if(o >= 60):
                    Campers[i]["Estado"]["2"] = True
                    Campers[i]["Estado"]["1"] = False
                else:
                    print("Este camper no ha aprobado la prueba de admisión")
                    Campers[i]["Estado"]["1"] = False
                    Campers[i]["Estado"]["7"] = True
            else:
                print("Este camper se encuentra en un estado diferente a pre-inscrito")
    with open('JsonCampers.json', 'w') as f:
        json.dump(Campers, f, indent = 4)
        f.close()
def salontrainer():
    os.system('clear')
    with open('JsonTrainers.json', 'r') as f:
        Trainers = json.loads(f.read())
        f.close()
    with open('JsonSalones.json', 'r') as f:
        Salones = json.loads(f.read())
        f.close()
        n = 0
    print("""
---------------------------------------
-------Ingresar Trainer al Salon-------
---------------------------------------

1. 6 AM - 10 PM
2. 10 AM - 2 PM
3. 2 PM - 6 PM
4. 6 PM - 10 PM

""")
    try:
        opc = int(input("Que horario desea?"))
        match(opc):
            case 1:
                os.system('clear')
                print("""
----------------------------
    TRAINERS DISPONIBLES
----------------------------
""")
                for i, item in enumerate(Trainers):
                    if Trainers[i]["Horario"]["1"] == True:
                            print(f"""---------------------
{Trainers[i]['Nombre']}, {Trainers[i]['Apellido']}
Edad {Trainers[i]['Edad']}, id {Trainers[i]['id']}
---------------------""")
                opc1 = int(input("Ingrese el id del trainer que desea: "))
                for y, item in enumerate(Trainers):
                    if Trainers[y]["id"] == opc1:
                        
                        try:
                            print("""
        ----------------------------
            SALONES DISPONIBLES
        ----------------------------
        """)
                            for i,item in enumerate(Salones):
                                if Salones[i]["Trainer1"] == False:
                                    n+=1
                                    print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
---------------------""")
                            opc2 = int(input("Ingrese a que salon quiere ingresar este trainer: "))
                            for i,item in enumerate(Salones):
                                if Salones[i]["Codigo"] == opc2:
                                    os.system('clear')
                                    Salones[i]["Trainer1"] = True
                                    Salones[i]["idT1"].append(Trainers[y]["id"])
                                    Salones[i]["Horario"]["1"] = False
                                    Trainers[y]["Horario"]["1"] = False
                                    Trainers[y]["Salon"].append(opc2)
                                    Salones[i]["R1"].append(int(input("Ingrese la ruta que impartira el trainer\n1. JAVA\n2. NetCore\n3. NodeJS")))
                                                
                            
                        except:
                            print("")

            case 2:
                os.system('clear')
                print("""
----------------------------
    TRAINERS DISPONIBLES
----------------------------
""")
                for i, item in enumerate(Trainers):
                    if Trainers[i]["Horario"]["2"] == True:
                            print(f"""---------------------
{Trainers[i]['Nombre']}, {Trainers[i]['Apellido']}
Edad {Trainers[i]['Edad']}, id {Trainers[i]['id']}
---------------------""")
                opc1 = int(input("Ingrese el id del trainer que desea: "))
                for y, item in enumerate(Trainers):
                    if Trainers[y]["id"] == opc1:
                        
                        try:
                            print("""
        ----------------------------
            SALONES DISPONIBLES
        ----------------------------
        """)
                            for i,item in enumerate(Salones):
                                if Salones[i]["Trainer2"] == False:
                                    n+=1
                                    print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
---------------------""")
                            opc2 = int(input("Ingrese a que salon quiere ingresar este trainer: "))
                            for i,item in enumerate(Salones):
                                if Salones[i]["Codigo"] == opc2:
                                    os.system('clear')
                                    Salones[i]["Trainer2"] = True
                                    Salones[i]["idT2"].append(Trainers[y]["id"])
                                    Salones[i]["Horario"]["2"] = False
                                    Trainers[y]["Horario"]["2"] = False
                                    Trainers[y]["Salon"].append(opc2)
                                    Salones[i]["R2"].append(int(input("Ingrese la ruta que impartira el trainer\n1. JAVA\n2. NetCore\n3. NodeJS")))
                                                
                            
                        except:
                            print("")
                    else:
                        print("Este trainer no existe")
                        x = input("")

            case 3:
                os.system('clear')
                print("""
----------------------------
    TRAINERS DISPONIBLES
----------------------------
""")
                for i, item in enumerate(Trainers):
                    if Trainers[i]["Horario"]["3"] == True:
                            print(f"""---------------------
{Trainers[i]['Nombre']}, {Trainers[i]['Apellido']}
Edad {Trainers[i]['Edad']}, id {Trainers[i]['id']}
---------------------""")
                opc1 = int(input("Ingrese el id del trainer que desea: "))
                for y, item in enumerate(Trainers):
                    if Trainers[y]["id"] == opc1:
                        
                        try:
                            print("""
        ----------------------------
            SALONES DISPONIBLES
        ----------------------------
        """)
                            for i,item in enumerate(Salones):
                                if Salones[i]["Trainer3"] == False:
                                    n+=1
                                    print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
---------------------""")
                            opc2 = int(input("Ingrese a que salon quiere ingresar este trainer: "))
                            for i,item in enumerate(Salones):
                                if Salones[i]["Codigo"] == opc2:
                                    os.system('clear')
                                    Salones[i]["Trainer3"] = True
                                    Salones[i]["idT3"].append(Trainers[y]["id"])
                                    Salones[i]["Horario"]["3"] = False
                                    Trainers[y]["Horario"]["3"] = False
                                    Trainers[y]["Salon"].append(opc2)
                                    Salones[i]["R3"].append(int(input("Ingrese la ruta que impartira el trainer\n1. JAVA\n2. NetCore\n3. NodeJS")))
                                                
                            
                        except:
                            print("")
                    else:
                        print("Este trainer no existe")
                        x = input("")
            case 4:     
                os.system('clear')
                print("""
----------------------------
    TRAINERS DISPONIBLES
----------------------------
""")
                for i, item in enumerate(Trainers):
                    if Trainers[i]["Horario"]["4"] == True:
                            print(f"""---------------------
{Trainers[i]['Nombre']}, {Trainers[i]['Apellido']}
Edad {Trainers[i]['Edad']}, id {Trainers[i]['id']}
---------------------""")
                opc1 = int(input("Ingrese el id del trainer que desea: "))
                for y, item in enumerate(Trainers):
                    if Trainers[y]["id"] == opc1:
                        
                        try:
                            print("""
        ----------------------------
            SALONES DISPONIBLES
        ----------------------------
        """)
                            for i,item in enumerate(Salones):
                                if Salones[i]["Trainer4"] == False:
                                    n+=1
                                    print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
---------------------""")
                            opc2 = int(input("Ingrese a que salon quiere ingresar este trainer: "))
                            for i,item in enumerate(Salones):
                                if Salones[i]["Codigo"] == opc2:
                                    os.system('clear')
                                    Salones[i]["Trainer4"] = True
                                    Salones[i]["idT4"].append(Trainers[y]["id"])
                                    Salones[i]["Horario"]["4"] = False
                                    Trainers[y]["Horario"]["4"] = False
                                    Trainers[y]["Salon"].append(opc2)
                                    Salones[i]["R4"].append(int(input("Ingrese la ruta que impartira el trainer\n1. JAVA\n2. NetCore\n3. NodeJS")))
                                                
                            
                        except:
                            print("")
                    else:
                        print("Este trainer no existe")
                        x = input("")
    except:
        print("Numero invalido")
    with open('JsonTrainers.json', 'w') as f:
        json.dump(Trainers, f, indent = 4)
        f.close()
    with open('JsonSalones.json', 'w') as f:
        json.dump(Salones, f, indent = 4)
        f.close()
