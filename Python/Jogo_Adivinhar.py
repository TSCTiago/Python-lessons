from random import randint
from time import sleep
print('Programa de adivinhação')
nome = str(input('Qual o seu nome? '))
print(f'Olá {nome}, Vamos jogar?')
print('Irei pensar em um número, tente adivinhar em seguida!!!')
sleep(0.5)
print('Pensado....')
sleep(1)
print()
vcomp = 0
vjog = 0
total = 0
while True:
    comp = randint(1,3)
    while True:
        jog = int(input('Que número pensei entre 1 e 3? '))
        if jog >= 1 and jog <= 3:
            break
        else:
            print('\033[91mNúmero Inválido. Tente Novamente!!!\033[m')
    print('Validando jogada.....')
    sleep(1)
    if comp == jog:
        print(f'Computador jogou {comp}')
        print(f'{nome} jogou {jog}')
        print(f'\033[93m{nome} Ganha\033[m')
        vjog += 1
    elif comp != jog:
        print(f'Computador jogou {comp}')
        print(f'{nome} jogou {jog}')
        print('\033[91mComputador Ganha!!\033[m')
        vcomp += 1
    total += 1
    continuar = str(input('Quer continuar??[S/N]')).upper()
    print()
    print('==='*15)
    if continuar == 'S':
        continue
    else:
        break
print(f'Você jogou {total} partidas')
print('           PLACAR')
print(f'\033[92mCOMPUTADOR {vcomp} X {vjog} {nome} \033[m')
if vcomp == vjog:
    print('\033[93mEMPATE\033[m')
elif vcomp < vjog:
    print('\033[92mVOCÊ VENCEU!!!')
    print('PARABÉNS!!\033[m')
else:
    print('\033[91mCOMPUTADOR VENCEU!!')
    print('TENTE DE NOVO FILHO!!!!\033[m')

