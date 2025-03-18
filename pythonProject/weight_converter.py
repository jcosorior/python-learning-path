#Python weight converter kg to pound

weight = float(input("Type the number to convert: "))
convertion = int(input("Kilograms to Pounds type 1, Pounds to Kilograms type 2 "))

if convertion == 1:
    convertioned = (weight*2.20462)
    print(f"{round(convertioned, 2)} Pounds")
elif convertion == 2:
    convertioned = (weight*0.453592)
    print(f"{round(convertioned, 2)} Kilograms")
else:
    pass