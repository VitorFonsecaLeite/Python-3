n=int(input("Digite um numero:"))
n1=0
n2=[]
print(f"Ao analisar o numero {n}.\nConcluimos que:",end=' ')
for c in range(1, 10):
    if n%c==0:
        n1=+1
        n2.append(c)
if len(n2)<=2 and n1<=2:
    print(f"É primo ")
else:
    print('Não é primo')