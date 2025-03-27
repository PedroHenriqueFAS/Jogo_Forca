print('Iniciando o jogo da forca\n')

palavra = input('Insira a palavra secreta: ')
# Preencher a quantidade de vidas com o valor desejado
vidas = int(input('Insira a quantidade de vidas o jogo terá: '))

print('\n' * 100)  # Limpa a tela para o jogador não ver a palavra secreta

print('Jogo iniciado!')
print(f'Você tem {vidas} vidas.')

aux = '*' * len(palavra)  # Cria uma string auxiliar com o mesmo tamanho da palavra secreta
print(f'A palavra é {aux}')

# Iniciar o loop do jogo
while True:
    # Permitir uma letra para avariavel var
    var =  input('Insira uma letra: ')
    # verificar se var ja foi digitada
    
    # verificar se var esta na palavra
    
    # verificar se ainda temos vidas
    
    # mostrar a palavra com var
    
    # mostrar a quantidade de vidas restante
    
    # mostrar as letras digitadas
    
    # verificar se o jogador ganhou
    
# avaliando se ainda temos vida e se a palavra ja foi preenchida