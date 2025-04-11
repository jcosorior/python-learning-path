
passcode = int(input("Enter your passcode: "))
attemps = 3
while passcode !=1234:
    passcode = int(input("Try again: "))
    if passcode != 1234:
        attemps -= 1
    else:
        break    
if attemps == 0:
    print("Your card is block, call your bank")
else:
    print("Transaction in progress")
