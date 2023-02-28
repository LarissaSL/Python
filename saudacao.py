while True:
    print('-------- Saudação --------\n')
    
    while True:
        nome = input('Olá, qual o seu nome?\n').lower().title().strip()
        
        caracterInvalido = 0
        numeros = ['1','2','3','4','5','6','7','8','9','0']
        
        for posicao in range (len(nome)):
            if nome[posicao] in numeros:
                caracterInvalido += 1
                
        if caracterInvalido > 0:
            print('\nDigite um nome válido, por favor.\n')
        elif caracterInvalido == 0:
            break
    
    while True:
        genero = input('Digite seu Gênero:\nM - Masculino\nF - Feminino\nB - Não Binário\nO - Outro\n').upper().strip()
    
        if genero in 'MFOB':
            break
        else:
            print('\nPor favor digite um gênero válido.\n')

    if genero == 'O':
        while True:
            preferencia = input('\nComo deseja ser chamadx?\n\nAs opções são: \nVindo\nVindx\nVinda\n\nDigite por qual deseja ser chamadx aqui: ').lower().strip()
            
            if (preferencia == 'vindo') or (preferencia == 'vindx') or (preferencia == 'vinda'):
                print(f'\nOlá, {nome}, seja bem {preferencia}, espero que esteja tendo um bom dia.')
                break
            else:
                print('Digite uma opção válida, por favor.\n')
        
    if genero != 'O':
        definicaoGenero = ['M','F','B']
        saudacao = ['vindo','vinda','vindx']

        saudacaoDefinida = ''

        for posicao in range (3):
            if genero == definicaoGenero[posicao]:
                saudacaoDefinida = saudacao[posicao]
        
        print(f'\nOlá, {nome}, seja bem {saudacaoDefinida}, espero que esteja tendo um bom dia.')
            
    continuar = input('\nDeseja outra saudação?\nS - Para Sim\nN - Para Não\n').upper()

    if continuar == 'N':
        print('Obrigada por utilizar o sistema. Tenha um bom dia.')
        break