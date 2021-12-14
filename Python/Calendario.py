days = int(input('Quantos dias: '))
first = int(input('primeiro dia da semana: '))
print('  D   S   T   Q   Q   S   S')
day = 1
while day < first:
    print('    ', end='')
    day += 1
day = 1
while day <= days:
    print(f'{day :>3}', end=' ')
    day += 1
    if first % 7 == 0:
        print(end='\n')
    first += 1
    