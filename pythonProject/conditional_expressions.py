# conditional expression = A one-line shortcut for the if else statment (ternary operation)
#                           Print of assign one of two values based on a condition
#                           X if condition else Y


#nun = 5
#print("Positive" if nun >0 else "Negative")

#num= 5
#result = "Even" if num% 2== 0 else "Odd"
#print(result)

#a = 6
#b = 7
#max_num = a if a> b else b
#min_num = a if a< b else b
#print(min_num)

#age = 25
#status = "Adult" if age >= 18 else "Child"
#print(status)

user_role = "pepito"

access_level= "Full Acces" if user_role == "admin" else "Limited Access"
print(access_level)