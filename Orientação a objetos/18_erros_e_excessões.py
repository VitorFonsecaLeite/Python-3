''' Erros iram acontecer ao executar o codigo, e algumas coisas podem ser feitas para tratalos'''

try:  # é um tentativa de execução, em algo que pode dar problema
    a = int(input("numerador:"))
    b = int(input('denominador:'))
    c = a/b
except (ValueError, TypeError):  # caso ocorra um erro tal ação deve ser tomado
    print('Tivemos um problema com o tipo de dado informado')
except ZeroDivisionError:  # informando o tipo exceessão em questão para a resposta ser informada
    print('Não é possivel dividir um numero por zero')
except KeyboardInterrupt:  # podendo ser feito um numero inlimitado excessões previstas
    print('O usuario não informou os dados')
except Exception as erro:
    print(f'O erro encontratado foi {erro.__cause__}')

else:  # caso nenhum erro seja percebido, tal ação deve ser executada
    print(f'O resultado é {c:.1f}')
finally:  # mensagem final que informa o fim da tentativa "try"
    print('Fim de operação, volte sempre')

'''Tipos de erros que podem acontecer :               '''
# NameErro              EOFError
# ValueErro             Keyboardinterrupt
# ZeroDivisionError     OSError
# TypeError             MemoryError
# IndexError            ConnenctionError
# KeyError              RuntimeError
