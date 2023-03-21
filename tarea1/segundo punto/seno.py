from math import sin
def seno ():
    n= float(input('ingrese un numero para calcular el seno:\n'))
    r= sin(n)
    print(f'el resultado de {n} por el seno es: {r}')
if __name__ == '__main__':
    seno()