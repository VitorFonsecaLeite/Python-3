import math
n=float(input("Digite um algulo Cº"))
n1=math.sin(math.radians(n))
n2=math.cos(math.radians(n))
n3=math.tan(math.radians(n))
print("O angulo Cº{} possue o seno de {:.2f}".format(n, n1))
print("O angulo Cº{} possue o cosseno de {:.2f}".format(n, n2))
print("O angulo Cº{} possue a tangente de {:.2f}".format(n, n3))