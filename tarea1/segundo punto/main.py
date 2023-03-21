from seno import seno
from coseno import coseno
from tangente import tangente
from exponencial import exponencial
from log_nautural import logaritmo_natural
def main():
    op=int(input('\ningrese la opccion que decea: '))
    if op == 1:
        print(f'la opcion es seno\n{seno()}')
    if op == 2:
        print(f'la opcion es coseno\n{coseno()}')
    if op == 3:
        print(f'la opcion es tangente\n{tangente()}')
    if op == 4:
        print(f'la opcion es exponencial\n{exponencial()}')
    if op == 5:
        print(f'la opcion es logaritmo natural\n{logaritmo_natural()}')
if __name__=='__main__':
    main()