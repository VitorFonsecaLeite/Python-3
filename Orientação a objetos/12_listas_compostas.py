'''Listas compostas são listas feitas de listas'''
dados = ['pedro', 25]  # exemplo e uma lista simples
print(dados[0])
print(dados[1])
# Adicionar uma lista simples a uma lista composta
pessoas = list()  # declaro umanova lista
# adiciono a lista dados como uma sub-lista de pessoas,
pessoas.append(dados[:])
# [:] Significa que estou fazendo uma copia da lista, cano seja colocado a lista seram interliogadas, ou seja, uma alteração ira afetar ambas as listas
print(pessoas)
'''-------------------------------------------------------------------------'''
# Declarando uma lista composta:
turma = [['pedro', 25], ['Ana', 18], ['joão', 33]]  # Exemplo de lista composta
# O 1º[] refere-se a qual sublista queremos, o 2º a qual item da sublista
print(turma[1][0])
# caso o 2º[] não seja informado, a sublista intera sera impressa
print(turma[2])
'''--------------------------------------------------------------------------'''
# Usando loop com listas
for p in turma:
    print(f'{p[0]} tem {p[1]} anos de idade')
'''---------------------------------------------------------------------------'''
# Entrada de dados com listas
galera = list()
info = list()
for c in range(0, 4):
    info.append(str(input('Nome:')))
    info.append(int(input('Idade:')))
    galera.append(info[:])
    info.clear()
print(galera)
