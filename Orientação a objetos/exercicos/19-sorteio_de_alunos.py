import random
n1=str(input("Digite o nome do 1º aluno:"))
n2=str(input("Digite o nome do 2º aluno:"))
n3=str(input("Digite o nome do 3º aluno:"))
n4=str(input("Digite o nome do 4º aluno:"))
alunos=[n1, n2, n3, n4]
sorteio=random.choice(alunos)
print(f"O aluno soreado foi : {sorteio}")

