import random
items = ["piedra", "papel", "tijera"]
computer = random.choice(items)
user = input("Elige piedra, papel o tijera: ").lower()
print(f"La computadora eligió: {computer}")
if user == computer:
    print("Empate")
elif (user == "piedra" and computer == "tijera") or (user == "papel" and computer == "piedra") or (user == "tijera" and computer == "papel"):
    print("Ganaste")
else:
    print("Perdiste")       