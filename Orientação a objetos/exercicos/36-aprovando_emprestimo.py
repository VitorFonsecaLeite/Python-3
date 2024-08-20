n1=float(input("Digite o valor da casa: R$"))
n2=float(input("Digite seu salario: R$"))
n3=int(input("Digite em quantos anos vai pagar: "))
parcelas=n3*12
boleto=n1/parcelas
porce=n2*0.30
if boleto>porce:
    print("Seu empretimo não foi aprovado")
else:
    print("Seu empretimo foi aprovado. \n Seram {} parcelas \n Cada parcela no valor de R${:.2f}.".format(parcelas, boleto))