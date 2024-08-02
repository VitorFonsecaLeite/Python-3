'''Funções possuem utilidades diversas, como facilitadores no workflow, vamos explorar algumas desas utilidades'''

help(print)  # help interativo, ele informa as expecificações de uma função
# doc expressa a documentação de uma função, com informações elem do help()
print(input.__doc__)

'''Agora nossas proprias funções podem e devem ser comentadas, para melhor utilização dos mesmo. Isso se chama DocStrings'''


def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela
    param i: inicio da contagem
    param f: fim da contagem
    param P: passos da contagem
    returm: sem retorno'''
    c = 1
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('fim')


print(contador(1, 10, 2))
help(contador)

'''Parametros opçionais, servem para evitarmos erros com def, como não informar os valores dod parametros, então são pre-estabelicidos valores. '''


def soma(a=0, b=0, c=0):
    s = a+b+c
    print(f" a soma vale{s}")


'''Funções com retorno, ao inves de usarmos um print ou variavel para retorna o valor da funções, nos utilizamos a comando return '''


def soma1(a=0, b=0, c=0):
    s = a+b+c
    return s


n1 = soma1(3, 2, 5)
n2 = soma1(7, 4)
n3 = soma1(6)
print(f"Meus calculos deram {n1}, {n2}, {n3}")
