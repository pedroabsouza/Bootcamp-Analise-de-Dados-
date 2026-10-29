# Neste estudo, irei desenvolver um código que receba um número e imprima na tela "FIZZ" caso este número seja múltiplo de 3, 'BUZZ" caso seja múltiplo de 5, 
# "FIZZBUZZ" caso seja múltiplo de 15 e imprima o próprio número caso não se aplique em nenhum dos casos. 

for i in range(1,101): # Comando cuja funçã é fazer com que nosso loop percorra a distância de 1 até 100
    if i % 3 == 0 and i % 5 == 0: # Se ambas forem verdadeiras, o número é múltiplo de 15
        print('FIZZBUZZ')
    elif i % 3 == 0:
        print('FIZZ')
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i) # Printa o próprio número na tela