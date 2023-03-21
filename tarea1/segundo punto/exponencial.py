from math import exp
def exponencial ():
    n=float(input('ingrese un numero para calcular el exponencial:\n'))
    r= exp(n)
    print(f'el resultado es: {r}')
if __name__=='__main__':
    exponencial()