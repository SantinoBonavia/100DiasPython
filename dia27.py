import time
print("Velocidad de tipeo")
sentencia="abcdefghijklmnopqrstuvwxyz"
print("Escribe la siguiente sentencia:")
print(sentencia)
input("Presiona enter para iniciar...")
start_time=time.time()
typed=input("Escribe la sentencia: ")
end_time=time.time()
time_taken=round(end_time-start_time,2)
speed=round(len(sentencia)/time_taken,2)
print("Tiempo tomado:", time_taken, "segundos")
print("Velocidad de tipeo:", speed, "caracteres por segundo")