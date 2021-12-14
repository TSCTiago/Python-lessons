import random
from time import sleep
print('GAME PEDRA-PAPEL- TESOURA')
print('''' OPÇÕES
    [0] = PEDRA
    [1] = PAPEL
    [2] = TESOURA
''')
puter = random.randint(0, 2)
while True:
    jog = int(input('SUA OPÇÃO: '))
    if 0 != jog and jog != 1 and jog != 2:
        print('Opção Inválida')
        print('Tente novamente.....')
    if 0 <= jog <= 2:
        break
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
if puter == 0:
    if jog == 0:
        print('Computador jogou Pedra')
        print('Empate')
    elif jog == 1:
        print('Computador jogou Pedra')
        print('Jogador Vence')
    elif jog == 2:
        print('Computador jogou Pedra')
        print('Computador Vence')
elif puter == 1:
    if jog == 0:
        print('Computador jogou Papel')
        print('Computador Vence')
    elif jog == 1:
        print('Computador jogou Papel')
        print('Empate')
    elif jog == 2:
        print('Computador jogou Papel')
        print('Jogador Vence')
elif puter == 2:
    if jog == 0:
        print('Computador jogou Tesoura')
        print('jogador Vence')
    elif jog == 1:
        print('Computador jogou Tesoura')
        print('Computador Vence')
    elif jog == 2:
        print('Computador jogou Tesoura')
        print('Empate')