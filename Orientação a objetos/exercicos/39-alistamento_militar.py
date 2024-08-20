from datetime import date
n=int(input("Digite seu ano de nascimento:"))
atual=date.today().year
idade=atual-n
print(f"Quem nasceu em {n} tem {idade} anos em {atual}")
if idade<18:
    print("Seu ano de alistamento é {}, em {} anos".format(n+18, 18-idade))
elif idade==18:
    print(f"Estamos no ano do seu alistamento, boa sorte kkkk")
else:
    print("Seu ano de alistamento foi {}, a {} anos atraz.".format(n+18, atual-(n+18)))