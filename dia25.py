print("\n===MINI SHOPPING CART===")
productos = ["Leche", "Pan", "Huevos", "Queso", "Frutas", "Verduras", "Carne", "Pescado", "Arroz", "Pasta"]
precios = [1.5, 0.8, 2.0, 3.5, 4.0, 2.5, 5.0, 6.0, 1.2, 1.8]
carrito = []
total = 0.0
while True:
    print("\nProductos disponibles:")
    for i in range(len(productos)):
        print(f"{i+1}. {productos[i]} - ${precios[i]:.2f}")
    opcion = input("Ingrese el número del producto que desea agregar al carrito (o 'salir' para finalizar): ")
    if opcion.lower() == "salir":
        break
    elif opcion.isdigit() and 1 <= int(opcion) <= len(productos):
        carrito.append(int(opcion)-1)
        print(f"{productos[int(opcion)-1]} agregado al carrito.")
    else:
        print("Opción inválida. Intente nuevamente.")   
