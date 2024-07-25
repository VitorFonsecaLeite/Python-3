n=float(input("Qual o salario do funcionario ? R$"))
n1=n*15/100
print("O funcionario que ganha R${:.2f}, com um acrescimo de 15% parra a ganhar R${:.2f}".format(n, n+n1))