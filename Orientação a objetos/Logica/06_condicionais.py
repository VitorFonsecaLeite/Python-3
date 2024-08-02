idade=int(input("Informa sua idade :"))

if idade>= 19: #1º condição a ser especificada
    print("Permitido")

elif idade==18: # Apos o if uma serie de elif podem ser declarados para condições especificas
    print('Permitido pelo 1º vez')

else: # Quando nenhuma das condições for atendidas o else sera aplicado
    print('Não Permitido')
#---------------------------------------------------------------------------------------------------
''' Em alguns casos temos mais de uma condição a ser avaliada, nestes casos utilizamos o and
    para adicionar mais de uma condicional a cada if/elif, veja a seguir :  '''
salario=float(input("Informe o seu salario :R$"))

if salario<= 3000:
    print("Programador Junior")
elif salario > 3000 and salario <= 6000 :
    print("Programador pleno")
elif salario > 6000 and salario <=15000 :
    print('Programador Pleno')
else :
    print(" Gerente de projetos")