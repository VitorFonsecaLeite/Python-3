n = float(input("Digite a quantida dias de que o corro foi alugado :"))
n1 = float(input("Digite a quantida de que o corro rodou nesses dias Km"))
n2 = n*60
n3 = n1*0.15
print("O carro rodou {}km, em {} dias, o total a pagar pelo aluguel é de R${:.2f}".format(n1, n, n2+n3))
