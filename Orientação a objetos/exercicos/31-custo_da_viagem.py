n=int(input("Digite a distancia que deseja viajar: KM"))
if n<=200:
    n1=n*0.50
else:
    n1=n*0.45
print("Em uma viagem de {}Km, voçe deve pagar R${:.2f} na passagem".format(n, n1))