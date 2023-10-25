n = int(input("Enter the number of terms : "))
a = 0
b = 1
if n < 0:
    print("Enter the possitive number because terms can not be negative.")
elif n == 0:
    print("Enter the bigger number from 0 because zero terms is nothing.")
else:
    print(a)
    print(b)
    for i in range(0,n):
        c = a+b
        a = b
        b = c 
        print(c)

