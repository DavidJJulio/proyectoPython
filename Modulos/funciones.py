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
           "Ruta1" : 0,
           "Ruta2" : 0,
           "Ruta3" : 0,
           "Ruta4" : 0
        })
    with open('JsonTrainers.json', 'w') as file:
        json.dump(Lista, file, indent = 4)
        file.close()
def crearcamper():
    with open('JsonCampers.json', 'r') as f:
        Lista = json.loads(f.read())
        f.close()
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
            "1" : False},
        "Ruta" : 0,
        "Estado" : {
            "1" : False,
            "2" : False,
            "3" : False,
            "4" : False,
            "5" : False,
            "6" : False,
            "7" : False
        },
        "Riesgo" : 0
    })
    x = len(Lista)
    if Lista[x-1]["Edad"] < 18:
        Lista[x-1].update({
            "Acudiente" : input("Ingrese el nombre de su acudiente: "),
            "CelAcudiente" : input("Ingrese el numero telefonico de el acudiente: ")
            })
    n = (input
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
    for i in (Lista[x-1]["Estado"]):
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
    with open('JsonSalones.json', 'r') as f:
          Salones = json.loads(f.read())
          f.close()
    with open('JsonCampers.json', 'r') as f:
          Campers = json.loads(f.read())
          f.close()
    n = 0
    k = 0
    print("""
---------------------------------------
---------Horarios disponibles----------
---------------------------------------

1. 6 AM - 10 PM
2. 10 AM - 2 PM
3. 2 PM - 6 PM
4. 6 PM - 10 PM

""")
    try:
        opc = int(input("Que horario desea?: "))
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
                        if Salones[i]["Trainer1"] == True:
                            n+=1
                            print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
Ruta: {Salones[i]["R1"]}
Trainer: {Salones[i]["idT1"]}
---------------------""")
                    opc = int(input("Seleccione un salon"))
                    for i,item in enumerate(Salones):
                        if Salones[i]["Trainer1"] == True:
                            try:
                                match(opc):
                                    case 1:
                                        for i, item in enumerate(Salones[opc-1]["Camp1"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp1"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True
                                                            

                                    case 2:
                                        for i, item in enumerate(Salones[opc-1]["Camp1"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp1"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True
                                    case 3:
                                        for i, item in enumerate(Salones[opc-1]["Camp1"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp1"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True
                        
                            except:
                                print("")
                        else:
                            print("No existen salones con clases cursando en este")
                except:
                    print("")
            case 2:
                os.system('clear')
                try:
                    print("""
        ----------------------------
            SALONES DISPONIBLES
        ----------------------------
        """)
                    for i,item in enumerate(Salones):
                        if Salones[i]["Trainer2"] == True:
                            n+=1
                            print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
Ruta: {Salones[i]["R2"]}
Trainer: {Salones[i]["idT2"]}
---------------------""")
                    opc = int(input("Seleccione un salon"))
                    for i,item in enumerate(Salones):
                        if Salones[i]["Trainer2"] == True:
                            try:
                                match(opc):
                                    case 1:
                                        for i, item in enumerate(Salones[opc-1]["Camp2"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp2"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True

                                    case 2:
                                        for i, item in enumerate(Salones[opc-1]["Camp2"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp2"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True
                                    case 3:
                                        for i, item in enumerate(Salones[opc-1]["Camp2"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp2"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True
                        
                            except:
                                print("")
                        else:
                            print("No existen salones con clases cursando en este")
                except:
                    print("")
            case 3:
                os.system('clear')
                try:
                    print("""
        ----------------------------
            SALONES DISPONIBLES
        ----------------------------
        """)
                    for i,item in enumerate(Salones):
                        if Salones[i]["Trainer3"] == True:
                            n+=1
                            print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
Ruta: {Salones[i]["R3"]}
Trainer: {Salones[i]["idT3"]}
---------------------""")
                    opc = int(input("Seleccione un salon"))
                    for i,item in enumerate(Salones):
                        if Salones[i]["Trainer3"] == True:
                            try:
                                match(opc):
                                    case 1:
                                        for i, item in enumerate(Salones[opc-1]["Camp3"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp3"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True

                                    case 2:
                                        for i, item in enumerate(Salones[opc-1]["Camp3"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp3"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True
                                    case 3:
                                        for i, item in enumerate(Salones[opc-1]["Camp3"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp3"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True
                        
                            except:
                                print("")
                        else:
                            print("No existen salones con clases cursando en este")
                except:
                    print("")
            case 4:
                os.system('clear')
                try:
                    print("""
        ----------------------------
            SALONES DISPONIBLES
        ----------------------------
        """)
                    for i,item in enumerate(Salones):
                        if Salones[i]["Trainer4"] == True:
                            n+=1
                            print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
Ruta: {Salones[i]["R4"]}
Trainer: {Salones[i]["idT4"]}
---------------------""")
                    opc = int(input("Seleccione un salon"))
                    for i,item in enumerate(Salones):
                        if Salones[i]["Trainer4"] == True:
                            try:
                                match(opc):
                                    case 1:
                                        for i, item in enumerate(Salones[opc-1]["Camp4"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp4"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True

                                    case 2:
                                        for i, item in enumerate(Salones[opc-1]["Camp4"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp4"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True
                                    case 3:
                                        for i, item in enumerate(Salones[opc-1]["Camp4"]):
                                            k +=1
                                            for b,item in enumerate(Campers):
                                                if Salones[opc-1]["Camp4"][i] == Campers[b]["id"]:
                                                    a = int(input(f"Ingrese el valor de la prueba practica del estudiante({Campers[b]['Nombre']}): "))
                                                    d = int(input(f"Ingrese el valor de la prueba examen del estudiante({Campers[b]['Nombre']}): "))
                                                    c = int(input(f"Ingrese el promedio de las notas(Trabajos) del estudiante({Campers[b]['Nombre']}): "))
                                                    a = a *0.6
                                                    d = d *0.3
                                                    c = c *0.3
                                                    if((a+b+c) >60):
                                                        Campers[b]["Estado"]["3"] = True
                                                        Campers[b]["Estado"]["2"] = False
                                                    else:
                                                        Campers[b]["Estado"]["2"] = False
                                                        Campers[b]["Estado"]["4"] = True
                                                        Campers[b]["Riesgo"] += 1
                                                        if Campers[b]["Riesgo"] == 2:
                                                            Campers[b]["Estado"]["1"] = False
                                                            Campers[b]["Estado"]["2"] = False
                                                            Campers[b]["Estado"]["3"] = False
                                                            Campers[b]["Estado"]["4"] = False
                                                            Campers[b]["Estado"]["5"] = False
                                                            Campers[b]["Estado"]["6"] = False
                                                            Campers[b]["Estado"]["7"] = True
                        
                            except:
                                print("")
                        else:
                            print("No existen salones con clases cursando en este")
                except:
                    print("")
    except:
        print("")
    with open('JsonSalones.json', 'w') as f:
          json.dump(Salones, f, indent=4)
          f.close()
    with open('JsonCampers.json', 'w') as fire:
          json.dump(Campers, fire, indent=4)
          fire.close()
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
          
    n = 0
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
                        if Salones[i]["Capacidad1"] >0 and len(Salones[i]["R1"]) != 0:
                            n+=1
                            print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
Ruta: {Salones[i]["R1"]}
Trainer: {Salones[i]["idT1"]}
---------------------""")
                        elif Salones[i]["Capacidad1"] >0 and len(Salones[i]["R1"]) == 0:
                            n+=1
                            print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
Ruta: 
Trainer: 
---------------------""")
                    u = int(input("A que salon desea ingresar el camper?: "))
                    for i,item in enumerate(Salones):
                        if Salones[i]["Codigo"] == u and Salones[i]["Capacidad1"] >0:
                            d = int(input("Ingrese el id del camper: "))
                            for b, item in enumerate(Campers):
                                if Campers[b]["id"] == d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] == True and Salones[i]["Trainer1"] == True:
                                    Campers[b]["Salon"].append(u)
                                    Campers[b]["Horario"] = True
                                    Salones[i]["Capacidad1"] -=1
                                    Salones[i]["Camp1"].append(Campers[b]["id"])
                                    Campers[b]["Trainer"].append(Salones[i]["idT1"][1])
                                    Campers[b]["Ruta"] = (Salones[i]["R1"])
                                elif(Campers[b]["id"] == d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] == True):
                                    Campers[b]["Salon"].append(u)
                                    Campers[b]["Horario"] = True
                                    Salones[i]["Capacidad1"] -=1
                                    Salones[i]["Camp1"].append(Campers[b]["id"])
                                elif(Campers[b]["id"] != d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] != True):
                                    print("Este camper no esta disponible para agregarse a un salon")
                                    x = input("Ingrese enter para continuar...")
                                else:
                                    pass
                except:     
                    pass
                
            case 2:
                os.system('clear')
                try:
                    print("""
        ----------------------------
            SALONES DISPONIBLES
        ----------------------------
        """)
                    for i,item in enumerate(Salones):
                        if Salones[i]["Capacidad2"] >0:
                            n+=1
                            print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
Ruta: {Salones[i]["R2"]}
Trainer: {Salones[i]["idT2"][1]}
---------------------""")
                    u = int(input("A que salon desea ingresar el camper?: "))
                    for i,item in enumerate(Salones):
                        if Salones[i]["Codigo"] == u and Salones[i]["Capacidad2"] >0:
                            d = input("Ingrese el id del camper: ")
                            for b, item in enumerate(Campers):
                                if Campers[b]["id"] == d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] == True and Salones[i]["Trainer2"] == True:
                                    Campers[b]["Salon"].append(u)
                                    Campers[b]["Horario"] = True
                                    Salones[i]["Capacidad2"] -=1
                                    Salones[i]["Camp2"].append(Campers[b]["id"])
                                    Campers[b]["Trainer"].append(Salones[i]["idT2"][2])
                                    Campers[b]["Ruta"] = (Salones[i]["R2"])
                                elif(Campers[b]["id"] == d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] == True):
                                    Campers[b]["Salon"].append(u)
                                    Campers[b]["Horario"] = True
                                    Salones[i]["Capacidad2"] -=1
                                    Salones[i]["Camp2"].append(Campers[b]["id"])
                                elif(Campers[b]["id"] != d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] != True):
                                    print("Este camper no esta disponible para agregarse a un salon")
                                    x = input("Ingrese enter para continuar...")
                                else:
                                    pass
                except:
                    pass
                
            case 3:
                os.system('clear')
                try:
                    print("""
        ----------------------------
            SALONES DISPONIBLES
        ----------------------------
        """)
                    for i,item in enumerate(Salones):
                        if Salones[i]["Capacidad3"] >0:
                            n+=1
                            print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
Ruta: {Salones[i]["R3"]}
Trainer: {Salones[i]["idT3"][1]}
---------------------""")
                    u = int(input("A que salon desea ingresar el camper?: "))
                    for i,item in enumerate(Salones):
                        if Salones[i]["Codigo"] == u and Salones[i]["Capacidad3"] >0:
                            d = input("Ingrese el id del camper: ")
                            for b, item in enumerate(Campers):
                                if Campers[b]["id"] == d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] == True and Salones[i]["Trainer3"] == True:
                                    Campers[b]["Salon"].append(u)
                                    Campers[b]["Horario"] = True
                                    Salones[i]["Capacidad3"] -=1
                                    Salones[i]["Camp3"].append(Campers[b]["id"])
                                    Campers[b]["Trainer"].append(Salones[i]["idT3"][1])
                                    Campers[b]["Ruta"] = (Salones[i]["R3"])
                                elif(Campers[b]["id"] == d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] == True):
                                    Campers[b]["Salon"].append(u)
                                    Campers[b]["Horario"] = True
                                    Salones[i]["Capacidad3"] -=1
                                    Salones[i]["Camp1"].append(Campers[b]["id"])
                                elif(Campers[b]["id"] != d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] != True):
                                    print("Este camper no esta disponible para agregarse a un salon")
                                    x = input("Ingrese enter para continuar...")
                                else:
                                    pass
                except:
                    pass
            case 4:
                os.system('clear')
                try:
                    print("""
        ----------------------------
            SALONES DISPONIBLES
        ----------------------------
        """)
                    for i,item in enumerate(Salones):
                        if Salones[i]["Capacidad4"] >0:
                            n+=1
                            print(f"""---------------------
{n}.{Salones[i]["Nombre"]}
Ruta: {Salones[i]["R4"]}
Trainer: {Salones[i]["idT4"][1]}
---------------------""")
                    u = int(input("A que salon desea ingresar el camper?: "))
                    for i,item in enumerate(Salones):
                        if Salones[i]["Codigo"] == u and Salones[i]["Capacidad4"] >0:
                            d = input("Ingrese el id del camper: ")
                            for b, item in enumerate(Campers):
                                if Campers[b]["id"] == d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] == True and Salones[i]["Trainer4"] == True:
                                    Campers[b]["Salon"].append(u)
                                    Campers[b]["Horario"] = True
                                    Salones[i]["Capacidad4"] -=1
                                    Salones[i]["Camp4"].append(Campers[b]["id"])
                                    Campers[b]["Trainer"].append(Salones[i]["idT4"][1])
                                    Campers[b]["Ruta"] = (Salones[i]["R1"])
                                elif(Campers[b]["id"] == d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] == True):
                                    Campers[b]["Salon"].append(u)
                                    Campers[b]["Horario"] = True
                                    Salones[i]["Capacidad4"] -=1
                                    Salones[i]["Camp4"].append(Campers[b]["id"])
                                elif(Campers[b]["id"] != d and len(Campers[b]["Salon"]) == 0 and Campers[b]["Estado"]["2"] != True):
                                    print("Este camper no esta disponible para agregarse a un salon")
                                    x = input("Ingrese enter para continuar...")
                                else:
                                    pass
                except:
                    pass
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
    with open('JsonCampers.json', 'r') as f:
        Campers = json.loads(f.read())
        f.close()
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
                                    Salones[i]["Trainer1"] = True
                                    Salones[i]["idT1"].append(Trainers[y]["id"])
                                    Salones[i]["idT1"].append(Trainers[y]["Nombre"])
                                    Salones[i]["Horario"]["1"] = False
                                    Trainers[y]["Horario"]["1"] = False
                                    Trainers[y]["Salon"].append(opc2)
                                    t = int(input("Ingrese la ruta que impartira el trainer\n1. JAVA\n2. NetCore\n3. NodeJS"))
                                    Salones[i]["R1"].append(t)
                                    Trainers[y]["Ruta1"] = t
                                    Salones[i]["Clase 1"].append(input("Ingrese la fecha de inicio del programa (DD/MM/AA: )"))
                                    Salones[i]["Clase 1"].append(input("Ingrese la fecha de finalizacion del programa (DD/MM/AA): "))
                                    for b, item in enumerate(Salones[i]["Camp1"]):
                                        for c,item in enumerate(Campers):
                                            if Salones[i]["Camp1"][b] == Campers[c]["id"]:
                                                Campers[c]["Trainer"].append(Trainers[y]["Nombre"])
                                                Campers[c]["Ruta"] = Salones[i]["R1"]
                            
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
                                    Salones[i]["idT1"].append(Trainers[y]["Nombre"])
                                    Salones[i]["Horario"]["2"] = False
                                    Trainers[y]["Horario"]["2"] = False
                                    Trainers[y]["Salon"].append(opc2)
                                    t = int(input("Ingrese la ruta que impartira el trainer\n1. JAVA\n2. NetCore\n3. NodeJS"))
                                    Salones[i]["R2"].append(t)
                                    Trainers[y]["Ruta2"] = t
                                    Salones[i]["Clase 2"].append(input("Ingrese la fecha de inicio del programa (DD/MM/AA: )"))
                                    Salones[i]["Clase 2"].append(input("Ingrese la fecha de finalizacion del programa (DD/MM/AA): "))
                                    for b, item in enumerate(Salones[i]["Camp2"]):
                                        for c,item in enumerate(Campers):
                                            if Salones[i]["Camp2"][b] == Campers[c]["id"]:
                                                Campers[c]["Trainer"].append(Trainers[y]["Nombre"])
                                                Campers[c]["Ruta"] = Salones[i]["R2"]
                                                
                            
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
                                    Salones[i]["idT1"].append(Trainers[y]["Nombre"])
                                    Salones[i]["Horario"]["3"] = False
                                    Trainers[y]["Horario"]["3"] = False
                                    Trainers[y]["Salon"].append(opc2)
                                    t = int(input("Ingrese la ruta que impartira el trainer\n1. JAVA\n2. NetCore\n3. NodeJS"))
                                    Salones[i]["R3"].append(t)
                                    Trainers[y]["Ruta3"] = t
                                    Salones[i]["Clase 3"].append(input("Ingrese la fecha de inicio del programa (DD/MM/AA: )"))
                                    Salones[i]["Clase 3"].append(input("Ingrese la fecha de finalizacion del programa (DD/MM/AA): "))
                                    for b, item in enumerate(Salones[i]["Camp3"]):
                                        for c,item in enumerate(Campers):
                                            if Salones[i]["Camp3"][b] == Campers[c]["id"]:
                                                Campers[c]["Trainer"].append(Trainers[y]["Nombre"])
                                                Campers[c]["Ruta"] = Salones[i]["R3"]                                               
                            
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
                                    Salones[i]["idT1"].append(Trainers[y]["Nombre"])
                                    Salones[i]["Horario"]["4"] = False
                                    Trainers[y]["Horario"]["4"] = False
                                    Trainers[y]["Salon"].append(opc2)
                                    t = int(input("Ingrese la ruta que impartira el trainer\n1. JAVA\n2. NetCore\n3. NodeJS"))
                                    Salones[i]["R4"].append(t)
                                    Trainers[y]["Ruta4"] = t
                                    Salones[i]["Clase 4"].append(input("Ingrese la fecha de inicio del programa (DD/MM/AA: )"))
                                    Salones[i]["Clase 4"].append(input("Ingrese la fecha de finalizacion del programa (DD/MM/AA): "))
                                    for b, item in enumerate(Salones[i]["Camp4"]):
                                        for c,item in enumerate(Campers):
                                            if Salones[i]["Camp4"][b] == Campers[c]["id"]:
                                                Campers[c]["Trainer"].append(Trainers[y]["Nombre"])
                                                Campers[c]["Ruta"] = Salones[i]["R4"]                                                
                            
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
    with open('JsonCampers.json', 'w') as f:
        json.dump(Campers, f, indent = 4)
        f.close()
