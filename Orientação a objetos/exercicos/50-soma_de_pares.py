cont=0
for n in range(1, 7):
    num=int(input(f"Digite o {n}º numero:"))
    if num%2==0:
        cont+=num
print(f"A soma dos valores pares é {cont}")