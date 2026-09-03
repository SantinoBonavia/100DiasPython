import random
chars="!@#$%^&*()_+1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
password=""
for i in range(8):
    password+=random.choice(chars)
print("Su contraseña generada es:", password)