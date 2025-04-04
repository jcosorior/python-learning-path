#Compount interest ecuation
#A = P(1+(r/n))ᵗ 
#A = final amount
#P = initial principal balance
#r = interest rate
#t = number of time periods elapsed
#n = number of times interest is capitilized in one year

#this is my attemp before the tutorial way, (I gave myself two hours to resolve it)
#the excerscise doesn't disclose the value for n, I gave it 12 
#rate = 1.3
#time = 1
#n = 12
#principle = float(input("What is your principle balance? "))
#while not principle == 0:
#    a = principle*(1+(rate/n))**time
#    print(f"Your debt is ${a:.2f}")
#    break
#else:
#    print("you are debt free")

#I took 1.8 hours :D #I realize if the user types a negative number, my program doesn`t have something for that

#now I will type what it says the tutorial

#principle = 0
#rate = 0
#time = 0

#while principle <=0:
#    principle = float(input("enter the principle amount: "))
#    if principle <=0:
#        print("principle can't be less or equal to zero")
#
#while rate <=0:
#    rate = float(input("enter the rate amount: "))
#    if rate <=0:
#        print("interest rate can't be less or equal to zero")
#
#while time <=0:
#    time = int(input("enter the time in years: "))
#    if time <=0:
#        print("time can't be less or equal to zero")
#
#total = principle * pow(1+(rate/100), time)
#
#print(f"Blance after {time} year/s: ${total:.2f}")


# Conclusions
#I need to validate user inputs
# Ensure the ecuation uses the rate in decimal form (divede rate by 100 if it's in percentage)
# Avoid infinite loops by updating values inside the while loop
# format the output for better clarity


# Variation of the excerscise

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("enter the principle amount: "))
    if principle <0:
        print("principle can't be less or equal to zero")
    else:
        break

while True:
    rate = float(input("enter the rate amount: "))
    if rate <0:
        print("interest rate can't be less or equal to zero")
    else:
        break

while True:
    time = int(input("enter the time in years: "))
    if time <0:
        print("time can't be less or equal to zero")
    else:
        break

total = principle * pow(1+(rate/100), time)

print(f"Blance after {time} year/s: ${total:.2f}")