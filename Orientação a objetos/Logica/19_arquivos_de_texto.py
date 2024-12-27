'''Aqui eu chamo o meu arquivo e o deixo dentro de um objeto '''
arquivo=open(
    "E:\\Tecnologia\\Python-3\\Orientação a objetos\\Logica\\arquivo 01.TXT",#local do arquivo
     encoding='UTF-8' #especifica a lingua do arquivo
     )

print(arquivo.read())# metodo que todo o arquivo de txt
print(arquivo.readline())# Le uma linha por vez do arquivo txt
print(arquivo.readlines())# Retorna uma lista com as linhas do arquivo txt
arquivo.close() #Fecha o arquivo de texto 

"""
Por padrão o metodo open vem como o modo de leitura ativado "r", porem podemos expecificar outros modos para esse metodo, como por exemplo:

"w" modo para escrita
"x" modo para criação e erro
"a" modo para anexo um conteudo ao final do arquivo
"b" modo para abrir em binario
"t" modo para abrir em modo texto
"+" modo para abrir atualizações
"""