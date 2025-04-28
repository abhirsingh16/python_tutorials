# Factorial - recursion
def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num-1)
    

print(factorial(3))

print(factorial(4))



# Fibonacci sequence

def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))