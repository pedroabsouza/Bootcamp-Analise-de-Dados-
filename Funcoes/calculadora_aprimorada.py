# Calculadora capaz de somar ou multiplicar uma lista inteira de números e responder a perguntas simples sobre eles, como "este número é par?"

def somarmultiplosnumeros(lista_numeros):
    resultadosoma = 0 
    for i in lista_numeros: # Percorre os elementos da lista um a um
        resultadosoma += i # Adiciona cada elemento e o soma
    return resultadosoma 

def multiplicarmultiplosnumeros(lista_numeros):
    resultadomulti = 1 # Se a multiplicação se iniciar em 0, o resultado final será 0
    for i in lista_numeros: # Percorre os elementos da lista um a um
        resultadomulti *= i # Adiciona cada elemento e o multiplica
    return resultadomulti

def ehpar(num):
    if num % 1 != 0 or num % 2 == 1: # Se meu número é decimal ou se apresenta resto quando dividido por 2 automaticamente é ímpar
        par = False
    else:
        par = True
    return par

def ehinteiro(num):
    if num % 1 == 0: # Se o número divido por 1 tem resto, não é inteiro
        inteiro = True
    else:
        inteiro = False
    return inteiro

lista_numeros = []
while True:
    numero = float(input('Qual valor gostaria de somar? '))
    lista_numeros.append(numero) # Adiciona à lista 
    continuar = input('Gostaria de adicionar mais um valor? (S/N) ')
    if continuar == 'N': # Se o usuário digitar 'N' encerra o loop imediatamente
        break
    

num = float((input('\nMe diga um número e te direi se ele é par e se é inteiro ou não: ')))


resultadosoma = somarmultiplosnumeros(lista_numeros) 
resultadomulti = multiplicarmultiplosnumeros(lista_numeros)
par = ehpar(num)
inteiro = ehinteiro(num)

print(f'\nOs números somados resultam em: {resultadosoma}')
print(f'Os números multplicados resultam em: {resultadomulti}')

if par == False: 
    print('O número digitado é ímpar!')
else:
    print('O número digitado é par!')

if inteiro == False:
    print('O número digitado não é inteiro!')
else:
    print('O número digitado é inteiro!')


