c = int(input('Digite o cpf: '))
f = c // 100
num = f
digito = str(c % 100)
i = 2
soma = 0
resto = 0
while f > 0:
    resto = f % 10
    soma = soma + (resto * i)
    f = f // 10
    i = i + 1
dv = 11 - (soma % 11)
if dv == 10 or dv == 11:
    dv = 0
# calculando o segundo dígito verificador
i = 3
soma = 0
resto = 0
while num > 0:
    resto = num % 10
    soma = soma + (resto * i)
    num = num // 10
    i = i + 1
soma = soma + (dv * 2)
dv1 = 11 - (soma % 11)
if dv1 == 10 or dv1 == 11:
    dv1 = 0
s = str(dv)
r = str(dv1)
u = r + s
if digito == u:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')