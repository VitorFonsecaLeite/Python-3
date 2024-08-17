n1=int(input("Digite o 1º valor:"))
n2=int(input("Digite o 2º valor:"))
n3=int(input("Digite o 3º valor:"))
menor=n1
maior=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
print(f"O menor valor é {menor}")
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print(f"O maior valor é {maior}")