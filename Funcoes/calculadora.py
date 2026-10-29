# Programa de calculadora simples capaz de somar, subtrair, multiplicar e dividir
from cores import *

def menu():
    print("\n" + FRENTE_VERMELHO + "_____CALCULADORA_____" + RESET) # RESET Necessário para ele parar de colorir
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print('4 - Dividir')
    print("5 - Sair.")

    
def soma(n1, n2):
    return n1 + n2

def subtrai(n1, n2):
    return n1 - n2

def multiplica(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

menu()

opcao = ''

while True: 
    opcao = input('Qual operação você gostaria de fazer? ')

    if opcao == '1':
        n1 = int(input('1° Número: '))
        n2 = int(input('2° Número: '))
        resultado = soma(n1, n2)
        print(f'O resultado da soma é: {resultado}')

    elif opcao == '2':
        n1 = int(input('1° Número: '))
        n2 = int(input('2° Número: '))
        resultado = subtrai(n1, n2)
        print(f'O resultado da subtração é: {resultado}')

    elif opcao == '3':
        n1 = int(input('1° Número: '))
        n2 = int(input('2° Número: '))
        resultado = multiplica(n1, n2)
        print(f'O resultado da multiplicação é: {resultado}')

    elif opcao == '4':
        n1 = int(input('1° Número: '))
        n2 = int(input('2° Número: '))
        resultado = divide(n1, n2)
        print(f'O resultado da divisão é: {resultado}')

    elif opcao == '5':
        break

    else:
        print('Digite uma opção válida!')
    