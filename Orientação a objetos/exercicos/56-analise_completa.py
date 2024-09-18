dados=list()
for n in range(1, 5):
    nom=str(input(f"Digite o nome da {n}º pessoa:"))
    idade=int(input(f"Digite a idade da {n}º pessoa:"))
    genero=str(input(f"Digite o genero da {n}º pessoa \n[M para masculino, F para feminino]:")).upper()
    dados.append({'nome': nom, 'idade': idade, "sexo":genero})
print(dados)