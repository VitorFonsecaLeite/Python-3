from datetime import date
n=int(input("Digite um ano, para saber se é bissexto, zero para ano atual:"))
if n==0:
    n=date.today().year
    
if n % 4==0 and n%100!=0 or n%400==0:
    print(f"O ano {n} É bissexto")
else:
    print(f"O ano {n} Não é bissexto")