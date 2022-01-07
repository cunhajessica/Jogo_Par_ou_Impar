from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
v = 0
while True:
    n = int(input('Diga um valor:'))
    res = str(input('Par ou ímpar[P/I]?')).strip().upper()[0]
    num = randint(1, 11)
    soma = n + num
    if soma % 2 == 0:
        valor = 'PAR'
        v += 1
    else:
        valor = 'ÍMPAR'
    print(f'Você escolheu {n} e o computador {num}. Total de  {soma}.\nO resultado foi {valor}.')
    if valor == 'PAR' and res == 'P':
        print('Você VENCEU!\nVamos jogar novamente...')
        v += 1
        print('=-'*15)
    if valor == 'ÍMPAR' and res == 'I':
        print('Você VENCEU! \n Vamos jogar novamente...')
        print('=-' * 15)
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {v} vezes.')





