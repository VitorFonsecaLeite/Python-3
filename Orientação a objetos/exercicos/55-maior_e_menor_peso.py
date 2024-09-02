n=int(input("Quantas pessoas vão ser avaliadas ? :"))
if n==0:
    print("OK, até mais")
else:   
    valores=[]
    for num in range(1, n+1):
        n1=float(input(f"Peso da {num}º pessoa ?:"))
        valores.append(n1)
        maior=max(valores)
        menor=min(valores)
    print(f"Omaior peso é {maior} e o menor é {menor}")