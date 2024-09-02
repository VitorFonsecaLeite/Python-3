from datetime import date
atual=date.today().year
n=int(input("Quantas pessoas vão ser avaliadas ? :"))
if n==0:
    print("OK, até mais")
else:   
    maior=0
    menor=0
    for num in range(1, n+1):
        n1=int(input(f"Em que ano a {num}º pessoa nasceu ?:"))
        if atual-n1>=18:
            maior=maior+1
        else:
            menor=menor+1
    print(f"Temos {maior} individuos maiores de idade\nE {menor} individuos menores de idade")