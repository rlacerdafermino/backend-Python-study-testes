"""iterando strings"""

nome = input("Digite seu nome: ")

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)


#nome =  input("Digite seu nome: ")


#tamanho_nome = len(nome)
#letra = 0
#while letra < tamanho_nome:
#    print(nome[letra])
 #   letra =+1
  #  break

# print(nome[2])
# contador = 0
# while contador < tamanho_nome:
#     print (nome[contador])
#     nome[contador] = nome + '*'
#     contador +=1
    
    ## Resultado

indice = 0
novo_nome = ''
while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice +=1
novo_nome += '*'
print(novo_nome)
