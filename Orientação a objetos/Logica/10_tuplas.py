# Tuplas são variaveis compostas com multiplos dados imutaveis
lanche = ('hanburgue', 'batatas', 'pizza', 'bolo')
for c in lanche:
    print('Eu vou comer', c)


print(sorted(lanche))  # para exibir em ordem alfabetica
print(lanche.index('bolo'))  # Para exiber a posição de determinado item
del (lanche)  # Para apagar a tupla do run
