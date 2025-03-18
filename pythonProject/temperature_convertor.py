Temperature = float(input("Enter the temperature you want to convert: "))
convertion = int(input("F° to C° type 1, C° to F° type 2: "))

if convertion == 1:
    c = round((5/9)*(Temperature-32), 1)
    print(f"{c} C°")
elif convertion == 2:
    f = round((9/5)*Temperature + 32, 1)
    print(f"{f} F°")
else:
    print(f"{convertion} is an invalid unit")