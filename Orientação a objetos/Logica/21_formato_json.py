#importando o módulo json
import json

#criando um dicionário para usarmos como exemplo a ser convertido a Json
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

#convertendo o dicionário para uma string o formato json
final = json.dumps(contatos, indent=4) # indent indica o Nº de espaços para indentação

#exibindo a string convertida
print(final)