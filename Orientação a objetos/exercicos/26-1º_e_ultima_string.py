n=str(input("Digite uma frese:")).lstrip().upper()
n1=n.count('A')
n2=(n.find('A'))+1
n3=(n.rfind('A'))+1
print(f"A letra A aparece {n1} vezes")
print(f"A 1º letra A aparece como {n2}º posição")
print(f"A ultima letra A aparece na posição {n3}º")