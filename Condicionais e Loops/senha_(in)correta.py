senhacorreta = 'TurmaAD05'
tentativas = 0
acertou = False

while tentativas < 3: # Variável que permite que o loop aconteça. A cada vez que o código roda, adiciona um nesta variável, se exceder 3, para. 
    senha = input('Digite a senha: ')
    tentativas += 1

    if senha == senhacorreta: # Quando usuário digita a senha correta, a variável acertou passa a guardar o valor 'True' e o break encerra o loop imediatamente.
        acertou = True
        break

    print('Errou!')

if acertou: # Se o valor contido for True, prossegue, caso contrário, parte para o else
    print('Parabéns, acesso liberado!')
else:
    print('Número de tentativas excedido. Acesso bloqueado! ')
