n = int(input('Digite N: '))
for l in range(1, n+1):
    for c in range(1, n+1):
        if c == l:
            print('*', end='')
        else:
            print('.', end='')
        if c % n == 0:
            print('\n', end='')