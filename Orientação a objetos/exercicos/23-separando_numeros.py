n=int(input("Digite um numero inteiro :"))
print(f"Analisando o numero {n} :")
print(f"Unidade: {n//1%10}\nDezena: {n//10%10}\nCentena: {n//100%10}\nMilhar: {n//100%10}")