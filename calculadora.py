"""Calculadora Python"""

#resultado = 0
#Identificacao usuario
#user_nome = input("Ola! me diga seu nome ")

#Pedido numero (1)
#numero1 = input(f"Digite o primeiro numero {user_nome} ")
#num1 = int(numero1)
#Pedido numero (2)
#numero2 = input(f"Digite o segundo numero {user_nome} ")
#num2 = int(numero2)
#Operacao matematica
#operacao = input(f"Digite a operacao matematica {user_nome} ")
#---------------------------------------------------------------Variaveis

#if operacao == '+':
#    resultado = num1 + num2
#    print(f"{user_nome} o resultado da operacao e: {resultado} ")
#elif operacao == '-':
#    resultado = num1 - num2
#    print(f"{user_nome} o resultado da operacao e: {resultado}")
#elif operacao == '*':
#    resultado = num1 * num2
#    print(f"{user_nome} o resultado da operacao e: {resultado}")
#elif operacao == '/':
#    if num2 == 0:
#        print(f"{user_nome} nao e possivel dividir por zero")
#    else:
#        resultado = num1 / num2
#        print(f"{user_nome} o resultado da operacao e: {resultado}")
#else:
#    print(f"{user_nome} operacao invalida")
#---------------------------------------------------------------Condicoes
#Fim do programa



while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        breakwhile True:
    sair = input("Deseja sair ?")
    if sair.lower().startswith('s'):
        break
