frase = 'Rafael Lacerda Fermino'
i = 0

qtd_apareceu_mais_vezes = 0
letra_que_mais_apareceu = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_apareceu_atual = frase.count(letra_atual)

    if qtd_apareceu_atual > qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = qtd_apareceu_atual
        letra_que_mais_apareceu = letra_atual

    i += 1
print(f'A letra que mais apareceu foi "{letra_que_mais_apareceu}" que apareceu {qtd_apareceu_mais_vezes} vezes.')
