palavra_secreta = ''
digitadas = []
chances = 6
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letras_erradas = []
palavra_temporaria = ''
print('=' * 51)
print('JOGO DA FORCA'.center(51))
print('=' * 51)
while True:
    for car in alfabeto:
        if car in palavra_temporaria:
            print(f'\033[96m{car} ', end='')
        elif car in letras_erradas:
            print(f'\033[31m{car} ', end='')
        else:
            print(f'\033[33m{car} ', end='')
    letra = input('\n\033[mDigite uma letra: ').upper()
    if len(letra) > 1:
        print('\033[33mPor favor digite apenas uma letra!\033[m')
        continue
    if letra.isnumeric():
        print('\033[33mPor favor digite apenas letras!\033[m')
        continue
    if letra in palavra_secreta:
        print(f'\033[36mUHUU! A letra {letra} está na palavra!\033[m')
        digitadas.append(letra)
    else:
        print(f'\033[31mA letra {letra} não está na palavra! Tente outra vez!\033[m')
        letras_erradas.append(letra)
        chances -= 1
    print(f'\033[33mVocê tem {chances} chances!\033[m')
    if chances == 0:
        print('Você perdeu!!!')
        break
    palavra_temporaria = ''
    for let in palavra_secreta:
        if let in digitadas:
            palavra_temporaria += let
        else:
            palavra_temporaria += '*'
    if palavra_temporaria == palavra_secreta:
        print(f'\033[32mQue legal! Você ganhou!!! A palavra era {palavra_temporaria}.\033[m')
        break
    else:
        print(f'\033[33mA palavra secreta está assim: {palavra_temporaria}\033[m')
    print('\033[33m-\033[m' * 51)
