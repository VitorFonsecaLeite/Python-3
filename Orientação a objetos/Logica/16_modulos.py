'''Modularização: dividir o programa em outros menores, assim agilizando seu desenvolvimento, os pacotes seriam então um conjunto de funções importadas de outro arquivo'''

import uteis  # aqui importamos todo um modulo de funções
from uteis import fatorial  # aqui importamos uma função expessifica do modulo


num = int(input("Digite um numero: "))
fat = uteis.fatorial(num)
dob = uteis.dobto(num)
tri = uteis.triplo(num)
print(f"O fatorial de {num} é {fat}")
print(f'o dobro de {num} é {dob}')
print(f'O triplo de {num} é {tri}')
