import random
cont=1
alunos=[]
while cont<=4 :
    n=str(input(f"digite o nome do {cont}ºaluno :"))
    alunos.append(n)
    cont=cont+1
random.shuffle(alunos)
print("A ordem de apresentação seras :")
print(alunos)