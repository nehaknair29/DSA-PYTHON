i=1
while(i<10):
    print(i)
    if i==5:
        break
    i+=1
 
i=1
while i<=3:
    j=1
    while j<=2:
        print(f"i={i}, j={j}")
        j+=1
    i+=1

for i in range(5):
    print(i)
for i in range(2,6):
    print(i)
for i in range(1,10,2):
    print(i)
for i in range(10,0,-2):
    print(i)
for i in range(-100,100,2):
    print(i)

n=int(input("Enter a number: "))
sum=0
i=0
while i<=n:
    sum+=i
    i+=1
print(sum)

i=1
while i<=5:
    print("*"*i)