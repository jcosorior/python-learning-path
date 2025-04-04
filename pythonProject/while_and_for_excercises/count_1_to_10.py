import time
num = 0 
while True:
    if num != 10:
        num = num + 1
        print(num)
        time.sleep(0.5)
    else:
        break