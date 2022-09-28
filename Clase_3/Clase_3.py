#Condicionales en Python
from traceback import print_tb


a = 3
b = 2
c = 5


if a > b:
    print('A es mayor a B')
    if a > c:
        print('A es mayor que C')
    else:
        print('C es mayor que C y A')