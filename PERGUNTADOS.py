from time import sleep
perguntas = {
    'Pergunta 1': {
        'pergunta': '\033[31mQuanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', 'd': '6'},
        'resposta_certa': 'b'},
    'Pergunta 2': {
        'pergunta': '\033[33mQuanto cores tem o arco-íris?',
        'respostas': {'a': '8', 'b': '6', 'c': '7', 'd': '5'},
        'resposta_certa': 'c'},
    'Pergunta 3': {
        'pergunta': '\033[32mQual fruta caiu na cabeça de Isaac Newton?',
        'respostas': {'a': 'maça', 'b': 'melão', 'c': 'banana', 'd': 'laranja'},
        'resposta_certa': 'a'},
    'Pergunta 4': {
        'pergunta': '\033[36mQual vitamina a seguir não existe?',
        'respostas': {'a': 'A', 'b': 'D', 'c': 'K', 'd': 'P'},
        'resposta_certa': 'd'},
    'Pergunta 5': {
        'pergunta': '\033[34mQuantos filmes tem na saga Harry Potter?',
        'respostas': {'a': '8', 'b': '7', 'c': '9', 'd': '6'},
        'resposta_certa': 'a'},
}

respostas_certas = 0
print('=' * 70)
print('PERGUNTADOS'.center(70))
print('=' * 70)
sleep(1)
print('A seguir será apresentado algumas questões de multipla escolha!')
sleep(2)
print('Escolha apenas UMA opção (letra) e confira sua pontuação no final!')
sleep(2)
print('Boa sorte! :)')
sleep(2)
print()
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Escolha dentre as opções abaixo: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    sleep(2)
    resposta_usuario = input('\033[mSua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        sleep(1)
        print('Você acertou!!!')
        respostas_certas += 1
    else:
        sleep(1)
        print('Você errou!!!')
    print()
qtd_perguntas = len(perguntas)
porcetagem_acerto = respostas_certas / qtd_perguntas * 100
print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcetagem_acerto:.2f}%.')
