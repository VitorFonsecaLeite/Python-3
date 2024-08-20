n1=float(input("Digite o 1º numero:"))
n2=float(input("Digite o 2º numero:"))
media=(n1+n2)/2
print(f"O aluno tem media {media}")
if media>=7:
    print("Alunos aprovado")
elif media<7 and media>=5:
    print("Alunos em recuperação")
else:
    print("Aluno reprovado")