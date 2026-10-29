# Lista simples de afazeres
from cores import * # Importar biblioteca do arquivo cores.py

tarefas = []

def menu():
    print("\n" + FRENTE_AMARELO + "________MENU________" + RESET) # RESET Necessário para ele parar de colorir
    print("1 - Adicionar Tarefa;")
    print("2 - Listar Tarefas;")
    print("3 - Remover Tarefa;")
    print("4 - Sair.")

def adicionarTarefa():
    tarefa = input('Digite o nome da tarefa: ')
    tarefas.append(tarefa)
    print("Tarefa Adicionada com sucesso!")

def listarTarefa():
    if len(tarefas) == 0:
        print('Você não tem tarefas adicionadas!')
    else:
        for numero, tarefa in enumerate(tarefas, start = 1):
            print(numero, "-", tarefa)

def removerTarefa():
    listarTarefa()

    if len(tarefas) > 0: 
        numero = int(input("Digite o número da tarefa a ser removida: "))

        if 1 <= numero <= len(tarefas): # Se o número está entre 1 e o número de tarefas que tenho na lista 
            tarefas.pop(numero - 1) # Para o usuário tarefas se iniciam em 1, para o programa em 0
            print('Tarefa removida!')
        else: 
            print('Número inválido')

opcao = ""

while opcao != 4:
    menu()
    opcao = input('Selecione uma opção: ')

    if opcao == "1":
        adicionarTarefa()

    elif opcao == "2":
        listarTarefa()

    elif opcao == "3":
        removerTarefa()

    elif opcao == "4":
        print('Até logo')
            
    else:
        print('Opção inválida')    