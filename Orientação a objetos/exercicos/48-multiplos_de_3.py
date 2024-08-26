cal=0
itens=0
plos=[]
for multi in range(1, 500):
    if multi%3==0 and multi%2!=0:
        cal+=multi
        itens+=1
        plos.append(multi)
print(f"A soma dos {itens} multiplos impares de de 3 entre 1 a 500\nResulta em {cal}")
print(plos)