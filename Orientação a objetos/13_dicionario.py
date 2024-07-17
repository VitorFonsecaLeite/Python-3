"""Um dicionario é declarado utilizando {} ou dict(), ao contrario das tuplas ou listas, o dicionario não utiliza indices numericos para referenciar seus dados, mas sim atravez de chaves strings """

dados = dict()  # declarando um dicionario
# Adicionando itens e declarando um dicionario
dados = {'nome': 'pedro', 'idade': 25}
dados['genero'] = 'masculino'  # Adicionando uma nova chave ao dicionario
print(dados['nome'])
print(dados['idade'])
print(dados['genero'])
'''----------------------------------------------------------------------------------------------'''
# Deletar uma chave do dicionario:
del dados['genero']
print(f'{dados}')
'''----------------------------------------------------------------------------------------------'''
# Extraindo dados do dicionario
filmes = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filmes.values())  # Para obter os valores
print(filmes.keys())  # Para obter as chaves
print(filmes.items())  # Para obter chaves e valores
'''----------------------------------------------------------------------------------------------'''
# usando loop com dicionarios
for k, v in filmes.items():
    print(f"O {k} é {v}")
'''----------------------------------------------------------------------------------------------'''
# É possivel criar uma tubla ou uma lista (composta ou não) de dicionarios
locadora = list()
# Adicionando um dicionario ja criado a uma lista, copy() e não [:]
locadora.append(filmes.copy())
# Adicionando novos dicionarios nas listas
locadora.append({'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},)
locadora.append({'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'})
