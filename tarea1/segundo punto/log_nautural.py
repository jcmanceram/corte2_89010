from math import log
def logaritmo_natural():
    n=float(input('ingrese un numero para conocer el logaritmo natural:\n'))
    r=log(n)
    print(f'logaritmo natural de {n} es: {r}')
if __name__ == '__main__':
    logaritmo_natural()
