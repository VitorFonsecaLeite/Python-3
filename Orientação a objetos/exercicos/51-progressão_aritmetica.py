print("10 termos de uma PA")
n1=int(input("Digite o 1º termo :"))
n2=int(input("Digite a razão : :"))
n3=n1
for n in range(1, 11):
    print(f"{n3}", end=" -> ")
    n3=n3+n2
print("Acabou")