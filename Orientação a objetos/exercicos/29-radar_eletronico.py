n=int(input("Digite a velocidade do carro: Km"))
if n<=80:
    print("Voce esta no limite de velocidade permitido")
else:
    n1=(n-80)*7
    print("voce passou o limite de velocidade \n Devera pagar uma multa de R${:.2f}".format(n1))