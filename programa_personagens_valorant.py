#Programa Executavel que mostra qual personagem pegar de acordo com a Função e Mapa

mapas = [' ','Breeze', 'Icebox', 'Haven', 'Bind', 'Ascent', 'Fracture', 'Pearl', 'Split']

funcoes = [' ', 'Iniciador', 'Dueslita', 'Sentinela', 'Controlador']


print('-------- Qual personagem devo Pickar? --------\n                  v1.0 | Ato 4         \n')

while True:
    funcao = int(input('\nQual função deseja saber?\nDigite uma das opções:\n1 - Iniciador\n2 - Duelista\n3 - Sentinela\n4 - Controlador\nR: ')) 
    if (funcao > 4) or (funcao == 0):
        print('\nDigite uma opção válida para Função por favor.')
    else:
        mapa = int(input('\nQual Mapa você vai jogar?\nDigite uma das opções:\n1 - Breeze\n2 - Icebox\n3 - Haven\n4 - Bind\n5 - Ascent\n6 - Fracture\n7 - Pearl\n8 - Split\nR: '))
        if (mapa > 8) or (mapa == 0):
            print('\nDigite uma opção válida para Mapa por favor.')

            
    if funcao <= 4 and mapa <= 8:
        if (funcao == 1) and (mapa == 1):
            print(f'\nOs personagens com função de {funcoes[1]} no mapa {mapas[mapa]} recomendados:\n1 - Sova\n2 - Skye\n3 - Breach.')
        elif (funcao == 1) and (mapa == 2):
            print(f'\nOs personagens com função de {funcoes[1]} no mapa {mapas[mapa]} recomendados:\n1 - Skye\n2 - Breach\n3 - Kayo\n4 - Sova\nOBS.: Se você souber jogar, Sova em 1º lugar.')
        elif (funcao == 1) and (mapa == 3):
            print(f'\nOs personagens com função de {funcoes[1]} no mapa {mapas[mapa]} recomendados:\nQualquer um deles é OP, boa sorte.')
        elif (funcao == 1) and (mapa == 4):
            print(f'\nOs personagens com função de {funcoes[1]} no mapa {mapas[mapa]} recomendados:\n1 - Sova\n2 - Skye\n3 - Breach.')
        elif (funcao == 1) and (mapa == 5):
            print(f'\nOs personagens com função de {funcoes[1]} no mapa {mapas[mapa]} recomendados:\n1 - Sova\n2 - Fade\n3 - Breach.')
        elif (funcao == 1) and (mapa == 6):
            print(f'\nOs personagens com função de {funcoes[1]} no mapa {mapas[mapa]} recomendados:\n1 - Breach\n2 - Fade\n3 - Kayo.')
        elif (funcao == 1) and (mapa == 7):
            print(f'\nOs personagens com função de {funcoes[1]} no mapa {mapas[mapa]} recomendados:\n1 - Breach\n2 - Fade\n3 - Kayo.')
        elif (funcao == 1) and (mapa == 8):
            print(f'\nOs personagens com função de {funcoes[1]} no mapa {mapas[mapa]} recomendados:\n1 - Breach\n2 - Fade\n3 - Kayo\n4 - Skye.')

    if (funcao == 2) and (mapa == 1):
        print(f'\nOs personagens com função de {funcoes[2]} no mapa {mapas[mapa]} recomendados:\n1 - Jett\n2 - Neon\n E se você souber bem Yoru.')
    elif (funcao == 2) and (mapa == 2):
        print(f'\nOs personagens com função de {funcoes[2]} no mapa {mapas[mapa]} recomendados:\n1 - Jett\n2 - Raze\n3 - Reyna.')
    elif (funcao == 2) and (mapa == 3):
        print(f'\nOs personagens com função de {funcoes[2]} no mapa {mapas[mapa]} recomendados:\nQualquer um desses é bom aqui: Phoenyx, Jett, Raze e Neon.')
    elif (funcao == 2) and (mapa == 4):
        print(f'\nOs personagens com função de {funcoes[2]} no mapa {mapas[mapa]} recomendados:\n1 - Raze\n2 - Reyna\n3 - Neon.')
    elif (funcao == 2) and (mapa == 5):
        print(f'\nOs personagens com função de {funcoes[2]} no mapa {mapas[mapa]} recomendados:\n1 - Jett\n2 - Raze.')
    elif (funcao == 2) and (mapa == 6):
        print(f'\nO personagem com função de {funcoes[2]} no mapa {mapas[mapa]} recomendado:\nNeon.')
    elif (funcao == 2) and (mapa == 7):
        print(f'\nOs personagens com função de {funcoes[2]} no mapa {mapas[mapa]} recomendados:\n1 - Neon\n2 - Jett\nE se você souber Reyna ou Phoenyx.')
    elif (funcao == 2) and (mapa == 8):
        print(f'\nOs personagens com função de {funcoes[2]} no mapa {mapas[mapa]} recomendados:\n1 - Raze\n2 - Reyna\n3 - Neon.')

    if (funcao == 3) and (mapa == 1):
        print(f'\nO personagem com função de {funcoes[3]} no mapa {mapas[mapa]} recomendado:\nChamber.')
    elif (funcao == 3) and (mapa == 2):
        print(f'\nOs personagens com função de {funcoes[3]} no mapa {mapas[mapa]} recomendados:\n1 - Chamber\n2 - KJ\n3 - Sage.')
    elif (funcao == 3) and (mapa == 3):
        print(f'\nOs personagens com função de {funcoes[3]} no mapa {mapas[mapa]} recomendados:\n1 - Chamber\n2 - KJ\n3 - Cypher\n4 - Sage.')
    elif (funcao == 3) and (mapa == 4):
        print(f'\nOs personagens com função de {funcoes[3]} no mapa {mapas[mapa]} recomendados:\n1 - KJ\n2 - Chamber\n3 - Cypher\n4 - Sage.')
    elif (funcao == 3) and (mapa == 5):
        print(f'\nOs personagens com função de {funcoes[3]} no mapa {mapas[mapa]} recomendados:\n1 - KJ\n2 - Chamber\n3 - Sage\n4 - Cypher')
    elif (funcao == 3) and (mapa == 6):
        print(f'\nOs personagens com função de {funcoes[3]} no mapa {mapas[mapa]} recomendados:\n1 - Chamber\n2 - KJ\n3 - Sage.')
    elif (funcao == 3) and (mapa == 7):
        print(f'\nO personagem com função de {funcoes[3]} no mapa {mapas[mapa]} recomendado:\nChamber.')
    elif (funcao == 3) and (mapa == 8):
        print(f'\nOs personagens com função de {funcoes[3]} no mapa {mapas[mapa]} recomendados:\n1 - KJ\n2 - Sage\n3 - Cypher.')

    if (funcao == 4) and (mapa == 1):
        print(f'\nO personagem com função de {funcoes[4]} no mapa {mapas[mapa]} recomendado:\nViper.')
    elif (funcao == 4) and (mapa == 2):
        print(f'\nOs personagens com função de {funcoes[4]} no mapa {mapas[mapa]} recomendados:\n1 - Viper\n2 - Harbor\n3 - Brim\n4 - Astra.')
    elif (funcao == 4) and (mapa == 3):
        print(f'\nOs personagens com função de {funcoes[4]} no mapa {mapas[mapa]} recomendados:\n1 - Omen\n2 - Brim\n3 - Astra.')
    elif (funcao == 4) and (mapa == 4):
        print(f'\nOs personagens com função de {funcoes[4]} no mapa {mapas[mapa]} recomendados:\n1 - Brim\n2 - Viper\n3 - Astra.')
    elif (funcao == 4) and (mapa == 5):
         print(f'\nOs personagens com função de {funcoes[4]} no mapa {mapas[mapa]} recomendados:\n1 - Omen\n2 - Brim\n3 - Astra\n4 - Viper.')
    elif (funcao == 4) and (mapa == 6):
        print(f'\nOs personagens com função de {funcoes[4]} no mapa {mapas[mapa]} recomendados:\n1 - Brim\n2 - Viper\n3 - Astra.')
    elif (funcao == 4) and (mapa == 7):
        print(f'\nOs personagens com função de {funcoes[4]} no mapa {mapas[mapa]} recomendados:\n1 - Viper\n2 - Harbor')
    elif (funcao == 4) and (mapa == 8):
        print(f'\nOs personagens com função de {funcoes[4]} no mapa {mapas[mapa]} recomendados:\n1 - Brim\n2 - Astra\n3 - Omen.')            


    continuar = input('\nDeseja fazer uma nova pesquisa? S/N\nR: ').upper()
    if continuar == 'N':
        print('\nCriado com amor e carinho por Soolari.')
        break