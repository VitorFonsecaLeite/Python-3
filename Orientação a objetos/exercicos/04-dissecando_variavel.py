a=input("Digite algo para analise:")
print("-----------------------------------------------------")
print(f"Os dados são do tipo :", type(a))
print(f"Os dados tem espaços ? :", a.isspace())
print(f"É um numero ? :", a.isnumeric())
print(f"É alfabetico ? :", a.isalpha())
print(f"É alfanumerico ? :", a.isalnum())
print(f"Esta em maiusculas ? :", a.isupper())
print(f"Esta em minusculas ? :", a.islower())
print("É capitalizado ? :", a.istitle())

""" Quando comando finaliza com (), ele se trata de um metodo"""