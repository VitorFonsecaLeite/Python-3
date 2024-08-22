altura=float(input("Qual a sua altura ? :"))
peso=float(input("Qual a sua altura ? :"))
imc=peso/(altura*altura)
print("Seu IMC é {:.1f}, esta classificado como :".format(imc))
if imc<=18.5:
    print("Abaixo do peso")
elif imc>18.5 and imc<25:
    print("Peso ideal")
elif imc<30:
    print("Sobre peso")
elif imc<40:
    print("Obsidade")
else:
    print("Obsidade morbida")