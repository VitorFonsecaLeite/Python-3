import random
numeros=[0,1,2,3,4,5]
print('Vou pensar em um numero entre 0 e 5.')
n=int(input("Tente adivinhar qual vai ser o numero:"))
n1=random.choice(numeros)
print(f"A resposta é :{n1}")
if n==n1:
    print('Parabens vocé acertou !!!!')
elif n1+1==n or n1-1==n1:
    print("Voce chegou perto mais eu ganhei")
else:
    print("Errou, eu ganhei")