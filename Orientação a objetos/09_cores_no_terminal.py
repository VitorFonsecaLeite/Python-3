''' ANSI - escape sequence, modelo de codigo utilizado para dar formato
    a saida de dados no terminal, baseado na norma ANSI '''

# \033[ style; text; back m 'codigo base para saida de cor no terminal'

'''Style ou estilo       text   e   back 
0(none, nada)         30  (branco)   40 ] 34 (azul) 44     
1(negrito)            31 (vermelho)  41 ] 35 (roxo) 45
4(sublinhado)         32   (verde)   42 ] 36 (ciano)46
7(inversão)           33 (amarelo)   43 ] 37 (Cinza)47'''

print("\033[1;31;43mola mundo\033[m")
