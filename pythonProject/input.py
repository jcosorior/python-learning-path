#   input() = A function that prompts the user to enter data
#             Returns the entered data as a string

name = input("What is your name?:")
age = input("How old are you?:")
age = int(age) 
age= age +1
print(f"Hello {name}")#you have to put an f string if you want to put variables
print("HAPPY BIRTHDAY")
print(f"You are {age} years old")

#name = input("What is your name?:")
#age = int(input("How old are you?:"))
#age = age + 1
#print(f"Hello {name}")#you have to put an f string if you want to put variables
#print("HAPPY BIRTHDAY")
#print(f"You are {age} years old")
# You can put the type casting there, directly in the variable input, and would work the same