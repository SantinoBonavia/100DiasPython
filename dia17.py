import random
nombre=input("Ingrese su nombre: ")
vibras=[" es genial", " es increíble", " es asombroso", " es extraordinario", " es impresionante"]
for i in range(5):
    print(nombre+random.choice(vibras)+str(random.randint(5,15)))