def k(n, p):
    
    if n == 1:
        return p
    else:
        return n**p + k(n-1, p)
n=int(input('ingrese el numero de terminos: '))
p=int(input('ingrese el numero del exponente: '))
print(k(n,p))