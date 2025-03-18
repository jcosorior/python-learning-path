# logical operators = evaluate multiple conditions (or, and, not)
#                   or at least one ondition must be True
#                   and = both conditions must be true
#                   not = inverts the condition (not False, not True)

#temp = 20
#is_raining = True

#if temp > 35 or temp < 0 or is_raining:
#    print("THe outdoor event is cancelled")
#else:
#    print ("The outdoor event is stil scheduled")

temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is Hot outside")
    print("It is Sunny")
elif temp <= 0 and is_sunny:
    print("It is Cold outside")
    print("It is Sunny")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is Warm outisde")
    print("It is Sunny")
elif temp >= 28 and not is_sunny:
    print("It is Hot outside")
    print("It is Cloudy")
elif temp <= 0 and not is_sunny:
    print("It is Cold outside")
    print("It is Cloudy")
elif temp < 28 and temp > 0 and not is_sunny:
    print("It is Warm outisde")
    print("It is Cloudy")