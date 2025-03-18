#string methos
#phone_number = input("Enter you phone number")
#name = input("Enter your full name: ")
#result = len(name) # len cuenta la longitud de un str
#result = name.find("o")
#result= name.find("o")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()#only returns true if your str only contains digits
#resul = name.isalpha()#only returns tru if theres is only alphabetycal characters
#result = phone_number.count("-")
#phone_number = phone_number.replace("-", " ")
#print(phone_number)

#print(help(str))# gives you an extensive list for methots

#validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

#name = input("Select your name, no more than 12 charcters: ")
#result = "Remeber no loger than 12 haractares" if len(name) > 12 else "Got it "
#print(result)

#name = input("Type you username, do not put any spaces: ")
#result = "Rember to not type any spaces" if " " in name else "Got it "
#print(result)

name = input ("Type your user name, remember to not use digits: ")
result = "Rember to not use DIGITS!" if any(char.isdigit() for char in name) else "Got it"
print(result) 