print('Iniciando o jogo da forca\n')

palavra = input('Insira a palavra secreta: ')
# Preencher a quantidade de vidas com o valor desejado
vidas = int(input('Insira a quantidade de vidas o jogo terá: '))

print('\n' * 100)  # Limpa a tela para o jogador não ver a palavra secreta

print('Jogo iniciado!')
print(f'Você tem {vidas} vidas.')

aux = '*' * len(palavra)  # Cria uma string auxiliar com o mesmo tamanho da palavra secreta
print(f'A palavra é {aux}')

usadas = []  # Lista para armazenar as letras já digitadas

# Iniciar o loop do jogo
while True:
    # Permitir uma letra para avariavel var
    var =  input('Insira uma letra: ')
    
    # verificar se var ja foi digitada
    if var in usadas:  # O 'in' quer dizer que vou na lista usadas e verifico se a letra ja foi digitada
        print('A letra {var} já foi digitada, tente outra.')
        continue  # Se a letra já foi digitada, continua o loop sem diminuir vidas
    else:
        usadas.append(var) # Adiciona a letra digitada na lista usadas
        
    # verificar se var esta na palavra
    if var in palavra:
        print(f'A letra {var} esta na palavra!')
        frase = ''
        for letra in palavra:
            if letra in usadas:
                aux = letra
            else: 
                aux = '*'
            frase = frase + aux
        print(f'A palavra é: {frase}') 
    else:
        print(f'A letra {var} não está na palavra. Tente novamente.')
        
        if vidas < 0:
            vidas -= 1  # Se a letra não estiver na palavra, diminui uma vida	
        if vidas == 0:
            print('Você perdeu!')
            print(f'A palavra era: {palavra}')
            break
        print('Agora você tem {vidas} vidas.')
    print(f' As letras que ja foram usadas são: {usadas}')
    
print ('Jogo Finalizado!')
    
    # verificar se ainda temos vidas
    
    # mostrar a palavra com var
    
    # mostrar a quantidade de vidas restante
    
    # mostrar as letras digitadas
    
    # verificar se o jogador ganhou
    
# avaliando se ainda temos vida e se a palavra ja foi preenchida