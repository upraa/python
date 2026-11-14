array = []
n = int(input("please enter your lenght of array: "))
for i in range (n) :
 a = input("Enter your list :")
 array.append(a)
print (array)
k = int(input("Enter shift amount: "))
for i in range(k):
    a = array.pop()
    array.insert(0, a)
print(array)
