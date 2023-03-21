from math import tan
def tangente ():
    n=float(input('ingrese un numero para calcular la tangente:\n'))
    r= tan(n)
    print(f'el resultado de {n} por la tangete es: {r}')
if __name__ == '__main__':
    tangente()