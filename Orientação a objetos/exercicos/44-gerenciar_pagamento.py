valor=float(input("Digite o valor do produto: R$"))
print("Escolha a forma de pagamento:\n[1] Dinhero ou cheque\n[2] Cartão de debito\n[3] Cartão de credito em 2x\n[4] Cartão de credito em 3x ou mais")
op=int(input("Qual a sua opção:"))
print("O valor a ser pago é:")
if op==1:
    valor-=(valor*0.10)
    print(f"R${valor}")
elif op==2:
    valor-=(valor*0.05)
    print(f"R${valor}")
elif op==3:
    print(f"R${valor}")
else:
    valor+=(valor*0.10)
    print(f"R${valor}")
