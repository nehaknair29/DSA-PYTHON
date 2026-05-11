#fibonacci series using recursion

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(10))  # Output: 55
print(fibonacci(0))   # Output: 0               
print(fibonacci(1))   # Output: 1