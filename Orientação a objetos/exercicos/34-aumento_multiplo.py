n=float(input("Digite o salario do funcionario : R$"))
if n<=1250:
    n1=1250*0.15
else:
    n1=1250*0.10
print(f"O funcionaria tera um aumento de {n1}")
print("Seu salario agora é de R${}".format(n+n1))