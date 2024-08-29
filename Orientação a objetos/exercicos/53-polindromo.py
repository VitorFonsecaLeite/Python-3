n=str(input("Digite uma frase:")).upper().strip()
n1=n[::-1]
if n==n1:
    print("É um polidromo")
else:
    print("não é um polidromo")
print(n)
print(n1)