import math
n1=float(input("Digite o comprimento do cateto oposto :"))
n2=float(input("Digite o comprimento do cateto adjacente :"))
n3=(n1**2)+(n2**2)
n4=math.sqrt(n3)
print("A hipotenusa vai medir :{:.2f}".format(n4))