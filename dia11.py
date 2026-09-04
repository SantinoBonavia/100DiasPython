tareas=[]
tarea1 = input("Ingrese la primera tarea: ")
tareas.append(tarea1)
tarea2 = input("Ingrese la segunda tarea: ")
tareas.append(tarea2)
tarea3 = input("Ingrese la tercera tarea: ")
tareas.append(tarea3)
tarea4 = input("Ingrese la cuarta tarea: ")
tareas.append(tarea4)
print("Lista de tareas:")
for tarea in tareas:
    print("-", tarea)