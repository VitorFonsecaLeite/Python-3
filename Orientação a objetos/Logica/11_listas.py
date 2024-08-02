''' Listas são mutaveis, ao contrario das listas, o que permite mudanças constantes em seu conteudo, aonde são usados [] em sua marcação'''

lanche = ['hamburgue', 'soda', 'pizza', 'pudin']
# Formas de adicionar itens a lista :
lanche[3] = 'bolo'  # Adiciona e substitui o item em uma possição especifica
print(lanche)
lanche.append('pudin')  # Adiciona um novo item ao final da lista
print(lanche)
# Adiciona e não substitui o item em uma possição especifica
lanche.insert(0, 'sorvete')
print(lanche)
'''----------------------------------------------------------------------------------'''
# removendo itens da lista:
del lanche[0]  # Elimina um item especifico da lista
print(lanche)
lanche.pop()  # Elimina o ultimo item da lista, porem tambem pode ser um especifico
print(lanche)
lanche.remove('pizza')  # Elimina um item da lista pela sua forma string
print(lanche)
'''-----------------------------------------------------------------------------------'''
# if e in com listas:
if 'pizza' in lanche:
    # Para evitar um erro, caso o item não esteja na lista
    lanche.remove('pizza')
else:
    print('nao a pizza na lista')
'''------------------------------------------------------------------------------------'''
# Criando listas com range:
valores = list(range(4, 11))  # o ultimo valor de range não é colocado
print(valores)
# list expecifica que se trata de uma lista
'''-------------------------------------------------------------------------------------'''
# Manipulando uma lista
numeros = [4, 6, 8, 15, 17, 22, 24, 10, 2]
print(sorted(numeros))  # colocar em ordem cresente
print(sorted(numeros, reverse=True))  # colocar em ordem decresente
print(max(numeros))  # informa o maior valor da lista
print(min(numeros))  # informa o menor valor da lista
print(sum(numeros))  # Soma todos os valores da lista
print("5" in numeros)  # verifica de um item esta na lista
