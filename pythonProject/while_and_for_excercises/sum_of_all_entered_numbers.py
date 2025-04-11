print("This program add every number you want, to finish type 0")
total = 0
while True:
    num = int(input("Enter a number, 0 to stop: "))
    if num == 0:
        break
    total += num
    
print(total)