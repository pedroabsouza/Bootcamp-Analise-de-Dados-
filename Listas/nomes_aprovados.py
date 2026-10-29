nomes_aprovados = ['João', 'Pedro', 'Michelle', 'Artur'] # Cria uma lista com elementos do tipo string

nome = input("Digite seu nome: ").strip() # strip() Remove eventuais espaços digitados por engano pelo usuário

if nome.lower() in [nome_lista.lower() for nome_lista in nomes_aprovados]: # 'nome.lower' converte o nome digitado para letras minúsculas, evitando possíveis erros de digitação.
    print(f"{nome} aprovado(a)!")                                          # A função '[nome_lista.lower() for nome_lista in nomes_aprovados]' cria uma nova lista temporária onde todos nomes são convertidos para letras minúsculas
else:                                                                      # o 'in' verifica se o nome digitado pelo usuário está contido nesta lista temporária. 
    print(f'{nome} reprovado(a)!')