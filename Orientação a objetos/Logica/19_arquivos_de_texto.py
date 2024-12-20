'''Aqui eu chamo o meu arquivo e o deixo dentro de um objeto '''
arquivo=open(
    "E:\\Tecnologia\\Python-3\\Orientação a objetos\\Logica\\arquivo 01.TXT",#local do arquivo
     encoding='UTF-8' #especifica a lingua do arquivo
     )

print(arquivo.read())# metodo que todo o arquivo de txt
print(arquivo.readline())# Le uma linha por vez do arquivo txt
print(arquivo.readlines())# Retorna uma lista com as linhas do arquivo txt
arquivo.close() #Fecha o arquivo de texto 