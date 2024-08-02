''' Aqui criamos um pacote de funções, que iremos importar para o projeto principal'''
def fatorial(n):
    f=1
    for c in range(1, n+1):
        f *=c 
    return f

def dobto(n):
    return n*2

def triplo(n):
    return n*3