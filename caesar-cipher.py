print('-='*20)
print('{:^40}'.format('CIFRA DE CÉSAR'))
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F',
        'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z']
while True:
    print('-=' * 20)
    escolha = str(input('Digite T para cifrar um texto ou C para decifrar uma chave: ')).strip().upper()[0]
    if escolha == 'T':
        texto = str(input('Digite o texto: ')).upper()
        lista_texto = list(texto)
        print('Texto a ser cifrado: ', end='')
        for c in lista_texto:
            print(c, end='')
        for pos, c in enumerate(lista_texto):
            lista_texto[pos] = alfabeto[alfabeto.index(lista_texto[pos])+3]
        print('\nTexto cifrado: ', end='')
        for c in lista_texto:
            print(c, end='')
    elif escolha == 'C':
        chave = str(input('Digite a chave: ')).upper()
        lista_chave = list(chave)
        print('Chave a ser decifrada: ', end='')
        for c in lista_chave:
            print(c, end='')
        for pos, c in enumerate(lista_chave):
            lista_chave[pos] = alfabeto[alfabeto.index(lista_chave[pos])-3]
        print('\nChave decifrada: ', end='')
        for c in lista_chave:
            print(c, end='')
    ver = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()[0]
    while ver not in 'SN':
        ver = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()
    if ver in 'N':
        break
print('-='*20)
print('Fim do programa!')
