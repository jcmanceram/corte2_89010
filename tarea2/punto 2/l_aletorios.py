from random import randint
lista = []
for i in range (0,10):
    lista.append(randint(1,50))
print(f'la lista contiene {lista}')

def mayor(lista):
    n_mayor = lista[0]
    for i in lista:
        if i > n_mayor:
            n_mayor = i
    print(f'el numero mayor de la lista es: {n_mayor}')        

def primos(lista):
     for num in lista:
        if num > 1:  
            for i in range(2, num):
                if num % i == 0:  
                    break
            else:  
                print(f'el numero {num} es primo')

print(mayor(lista),primos(lista))