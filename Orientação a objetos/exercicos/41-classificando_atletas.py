from datetime import date
n=int(input("Digite o ano do seu nascimento:"))
atual=date.today().year
idade=atual-n
print(f"Quem nasceu em {n} possue {idade} anos\nNesta idade esta classificado para:")
if idade<=9:
    print("Mirim")
elif idade<=14:
    print("Infantil")
elif idade<=19:
    print("Junior")
elif idade<=25:
    print("Sênior")
else:
    print("Master")