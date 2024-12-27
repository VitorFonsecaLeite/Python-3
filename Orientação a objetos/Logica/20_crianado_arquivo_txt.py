#Criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?"

#usando a função open para criar um objeto do tipo arquivo
arquivo = open(
    "E:\\Tecnologia\\Python-3\\Orientação a objetos\\Logica\\arquivo 02.TXT",
      "w", # expecifico que se trata do modo de escrita ou writh
      encoding='UTF-8')

#Escrevendo o conteúdo da variável conteudo dentro do arquivo
arquivo.write(conteudo)

#fechando o arquivo
arquivo.close()