# Tratase do tratamento de cadeis de caracteres e/ou texto

frase = "curso em video python"

'''Toda string possue um numero de indices para cada caracter,
   tanto para os visiveis como para os de espaços, começando de
   0 em diante,o exemplo acima possue 20 indices (micro espaços)'''

# Fatiamento ______________________________________________________________
print("Vamos fatiar a frase: ", frase)
print("para pegar um indice especifico ==> ", frase[9])
print("para pegar um conjunto de indices ==> ",
      frase[9:13])  # o ultimo não é considerado
print("para pegar um conjunto de indices, pulande determinada ordem ==> ",
      frase[9:21:2])
print("para pegar um conjunto de indices, até o informado ==> ", frase[:5])
print("para pegar um conjunto de indices, iniciando no informado ==> ",
      frase[15:])
print("para pegar um conjunto de indices, informando aonde se inicia e quantos devem ser pulados ==> ",
      frase[9::3])
print('------------------------------------------------------------------------------------------------------------------------')
# Analise_______________________________________________________________________
print('Agora vamos analisar a frase:')
print("Para mostra a quantidade de indices da frase ==> ", len(frase))
print("Para mostra a quantidade de vezes que certo caracter aparece ==> ",
      frase.count('o'))
print("Para mostra a quantidade de caracteres enttre determinados indices ==>",
      frase.count('o', 0, 13))
print("Para mostra a posição de determinada string ==>", frase.find(
    'video'))  # Se a string não existir, o valor -1 sera retornado
print('Para se saber se determinda string se encontra na frase ==>', "curso" in frase)
print('------------------------------------------------------------------------------------------------------------------------')
# Transformação__________________________________________________________________
print("Passamos para transformação")
print('Para substituir determinada palavra por outra ==>',
      frase.replace('python', 'java'))
print('Para deixar todas as letras em maisculo ==> ', frase.upper())
print('Para deixar todas as letras em minusculo ==> ', frase.lower())
print('Para deixar todas as letras em minusculo menos a primeira ==> ',
      frase.capitalize())
print('A primeira letra de todas as palavras ficam em maiusculo ==>', frase.title())
print('Para eliminar os espaços em branco na frase ==>', frase.strip())
# rstrip para somente os espaços d a direita e lstrip para os da esquerda
print('Para separar as palavras e criar novas lista a partir dela ==>', frase.split())
print('Para juntar as palavras novamente ==>', ''.join(frase))
print('------------------------------------------------------------------------------------------------------------------------')
# Centralisação
print('Centralização de frases "strings"')
print('Justificado a esquerda em 50 espaços')
print(frase.ljust(50, '*'))
print('Justificado ao centro em 50 espaços')
print(frase.center(50, '*'))
print('Justificado a direita em 50 espaços')
print(frase.rjust(50, '*'))
