n=int(input("Digite um numero inteiro:"))
print("Escolha uma das bases para converter:\n(1) para binario\n(2) para octal\n(3) para hexadecimal")
n1=int(input("Sua opção :"))
if n1==1:
    print("{} convertido para binario se torna : {}".format(n, bin(n)))
elif n1==2:
    print("{} convertido para octal se torna : {}".format(n, oct(n)))
elif n1==3:
    print("{} convertido para hexadecimal se torna : {}".format(n, hex(n)))