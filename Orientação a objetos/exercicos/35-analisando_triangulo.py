n1=float(input("Digite o 1º segmento :"))
n2=float(input("Digite o 2º segmento :"))
n3=float(input("Digite o 3º segmento :"))
if n3<n1+n2 and n1<n2+n3 and n2<n3+n1:
    print("Os segmentos formam um triangulo")
else:
    print("Os segmentos não formam um triangu")