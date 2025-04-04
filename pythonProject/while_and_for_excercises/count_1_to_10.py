#this first way it was my way to resolve the excersice 
import time
#num = 0 
#while True:
#    if num != 10:
#        num = num + 1
#        print(num)
#        time.sleep(0.5)
#    else:
#        break


#this second version is a sugested version that a senior friend gave me, he says there is some good practices and for this case this excersice is better
# I'm not familiar with complexity of good practice yet, so I'm going to keep going through my learning process
num = 0
while num < 10:
    num +=1
    print(num)
    time.sleep(0.5)