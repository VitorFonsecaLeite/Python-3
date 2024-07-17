''' A variavel tem o papel de guardar dados, sejam textos, numeros ou valor booleano '''

nome = " programado"
# STR ou string é referente a mensagens de texto, sempre entre aspas "..."

idade = 23
# INT ou inteiro é referente a numeros inteiros, sejam positivos ou negativos

peso = 72.5
# FLOAT ou flutuante referente a numeros decimais, ou seja, com virgula

is_python= True
is_java= False
''' BOOL ou boleano reference ao estado da variavel e possue apenas 2 valores,
    verdadeiro (True) e/ou falso (False)'''

# Exemplo de armazenamento condicional booleano
ingresso=50
compradores=250
tem_ingresso_suficiente= (ingresso >= compradores)

#Resultdos
print(nome)
print(idade)
print(peso)
print("Tem ingresso a venda ? :",tem_ingresso_suficiente)