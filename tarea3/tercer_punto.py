def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=int(input('ingrese el numero en cual quiere terminar de secuencia de fibonacci: '))
print(fibonacci(n))