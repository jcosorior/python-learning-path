#if = Do some code only IF some condition is True
# Else do something else

age = int(input("Enter you age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet")
elif age >= 100: #si ejecutas el programa te aparecera el mensaje de la linea 7, porque en una cade de if statement la condicion que se ejecute primero es la que se imprime
    print("You are too old to sign up")
else:
    print("You must be 18+ to sign up")
    

if age >= 100:  #tienes que colocarlo al principio si quieres que se ejecute primero
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ to sign up")
    

response = input("Would you like food? (Y/N): ")

if response == "Y":# == is the comparison operator it will check to see if two values are the same
    print("Have some food!")
else:
    print("No food for you!")
    

name = input("Enter your name: ")
if name == "":
    print("YOu did not type in your name!")
else:
    print(f"Hello {name}")
    
    
for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This is not for sale")