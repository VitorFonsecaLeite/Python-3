""" O python possue um metodo nativo de entrada de dados, o comando input"""

nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
peso = float(input("Digite seu peso:"))
# varavel = tipo prim.(entrada("...dados..."))

'''Para uma melhor organização sempre declare o tipo primitivo dos dados,
o input pode ser realizado sem a declaração do tipo, porem, a classificação
sera automatica o que pode acabar atrabalhando depois'''

print("-----------------------------------------")
print(nome)
print(idade)
print(peso)
