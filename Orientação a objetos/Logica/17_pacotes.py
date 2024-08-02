''' Pacotes são modulos compostos por modulos, são as chamadas bibliotecas, 
sendo necessario a criação do arquivo __init__ para colocar as funções desejadas'''

from muitoUteis import numeros  # exemplo de importação de pacotes

num = int(input("Digite um numero: "))
fat = numeros.fatorial(num)
dob = numeros.dobto(num)
tri = numeros.triplo(num)
print(f"O fatorial de {num} é {fat}")
print(f'o dobro de {num} é {dob}')
print(f'O triplo de {num} é {tri}')
