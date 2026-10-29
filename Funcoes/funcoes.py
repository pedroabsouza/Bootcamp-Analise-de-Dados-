# Compreender o uso de funções dentro de um código
# Facilitar manutenção do código criando funções que desenvolvem atividades específicas

# Função sem retorno e sem parâmetros
def sobre():
    print('Desenvolvido por: Pedro Augusto')

# Função com parâmetros, mas sem retorno - Customizar o que será exibido na tela através dos parâmetros passados
def turma(turma, ano):
    print(f'Turma: {turma} - Ano {ano}')

# Função com parâmetros e retorno
def somar(numero1, numero2):
    return numero1 + numero2 # Necessário chamar a função return para retornar um valor 
    


sobre()

turma('AD-05', 2026) # Parâmetro que será passado à função

numero1 = float(input('Digite o 1° número: '))
numero2 = float(input('Digite o 2° número: '))

resultado = somar(numero1, numero2)
print(f'A Soma de 10 + 5 = {resultado:.0f}') # :.0f funciona de modo que eu informe quantos zeros eu quero que apareçam