'''WHILE : loop que executa ações enquanto
    a condição for verdadeira'''

controladora=1
while controladora<= 5: #Até que a variavel controladora chegue a 5, o loop ira se repetir
    print(controladora)
    controladora=controladora+1 #Ao final de cada loop, é adicinado +1 na varial controladora

while True: #Estrutura de repetição 'infinita', que não possue uma variavel controladora
    print(controladora+1)
    controladora=controladora+1
    if controladora==10:
        break #Comando para interromper a estrutura de repetição