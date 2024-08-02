'''Funções são caracterizadas como rotina, ou seja, comando utilizados de forma repetitiva em nossa aplicação, temos como exemplo o comando Print. Funções são declaradas com o comando def'''


def mostraLinha():  # exemplo de uma função sem parametros
    print('______________________________________')


mostraLinha()  # chamando a função
print('Ola mundo')
mostraLinha()

'''Funcões com parametros------------------------------------------------------------------------'''


def soma(a, b):  # Exemplo de função com parametros definidos
    s = a+b
    print(s)


soma(5, 5)

'''Funções com parametros compactados, como listas e tuplas--------------------------------------'''


def contador(*num):  # O * é o desempacotador, sinalisa que não ha um numero definido de parametrtos
    print(num)


contador(1, 2, 3)
