import math
n=int(input("Enter a number:"))
fact=math.factorial(n)
print("Factorial:",fact)
square_root=math.sqrt(n)
print("Square root is:",square_root)

i=1
while(i<10):
    print(i)            
    if i==5:
        break
    i+=1
