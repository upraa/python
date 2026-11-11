num = int(input("pls enter your number : "))
for i in range (1 , num) :
    if num % i == 0:
        print ("no prime")
        break
else :
     print (" prime")