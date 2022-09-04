from random import randint
from time import sleep

numero = str(randint(100000000, 999999999))
novo_cpf = numero
reverso = 10
total = 0
for c in range(19):
    if c > 8:
        c -= 9
    total += int(novo_cpf[c]) * reverso
    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print('\033[33m=' * 40)
print('GERADOR DE CPF'.center(40))
print('=' * 40)
sleep(1)
print('Gerando sequência ...')
sleep(2)
print('Finalizando ...')
sleep(2)
print(f'\033[32mNOVO CPF: {novo_cpf}')