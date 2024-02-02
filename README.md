-------------------------------------------------ESTRUCTURACION DEL PROGRAMA-----------------------------------------------------------

IDEA CENTRAL:
Un programa que permita: Crear rutas de aprendizaje, crear trainers (CRUD), crear campers (CRUD), manejar horario de los trainers, asignar rutas a los trainers, asignar salones a los trainers, asignar campers a una ruta, asignar un camper a un trainer, asignar un camper a un salon, manejar notas de campers, filtros y manejar un modulo de reportes.

REQUERIMIENTOS RESUMEN:

1. Registrar campers con toda su informacion
2. Realizar una prueba inicial a los campers y en caso de pasarla asignarles una ruta
3. Realizar un sistema de notas y filtros para camper
4. Asignar campers a un salon
5. Creacion de nuevas rutas con sus respectivos modulos
6. Registrar Trainers y su informacion
7. modulo de matriculas que permita asignar los campers aprobados, experto encargado, ruta de entrenamiento asignada, fecha de inicio, fecha de finalizacion y salón de entrenamiento
8. Manejo de riesgo y filtro de estudiantes
9. Modulo de reportes.



ORDEN DEL DESARROLLO:


1. Coordinacion:

    Coordinacion debe manejar: Modulos, Rutas, Notas de los estudiantes, Estado de los campers, Informes.

2. Diseño de las rutas:
    
    En primera instancia se debe elaborar que Rutas existiran, los modulos que las conformaran, cantidad de filtros y la duracion de la ruta.

3. CRUD de Trainers:

    Se crearan a los trainers, se introduciran sus horarios y en base a ellos se les repartira un salon y una ruta. 

4. CRUD de Campers:

    Se crearan a los campers, se les asignara un Trainer, salon y ruta. 
