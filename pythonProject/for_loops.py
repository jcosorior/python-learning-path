# for loops = execute a block of code a fixed number of imes.
#           You can interate over a range, string, sequence, etc.
# while is better when you need something posible infinite ammount of times (such as you are acceptin user input for example)
#for x in reversed(range(1, 11, 2)):
#    print(x)
#
#print("Happy new year!!")


credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)


for x in range(1, 21):
    if x == 13:
        continue #continue skip the conditions you steated, break will break the loop
    else:
        print(x)

for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)

