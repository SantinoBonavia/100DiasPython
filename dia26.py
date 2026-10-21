account={
    "name": "Santino",
    "age": 20,
    "pin": 1234,
    "type": "savings",
}

print("Welcome to the bank!")
pin=int(input("Enter your pin: "))
if pin==account["pin"]:
    print("Access granted!")
    print("Your account details are:")
    print("Name:", account["name"])
    print("Age:", account["age"])
    print("Account type:", account["type"])
else:
    print("Access denied!")
