from math import cos
def coseno ():
    n= float(input('ingrese un numero para calcular el coseno:\n'))
    r= cos(n)
    print(f'el resultado de {n} por el coseno es: {r}')
if __name__ == '__main__':
    coseno()