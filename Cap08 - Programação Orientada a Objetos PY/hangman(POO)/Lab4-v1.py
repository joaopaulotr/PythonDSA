# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

     palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
     # Método Construtor
     def __init__(self):
          self.palavra = random.choice(palavras)
          self.letras_descobertas = ['_' for letra in palavra]
          self.chances = 6
          self.letras_erradas = []

	# Método para adivinhar a letra
     def adivinhaLetra(self):
          tentativa = input("\nDigite uma letra: ").lower()

          if tentativa in self.palavra:
            index = 0
            for letra in self.palavra:
                if tentativa == letra:
                    self.letras_descobertas[index] = letra
                index += 1
          else:
            self.chances -= 1
            self.letras_erradas.append(tentativa)
	
     # Método para verificar se o jogo terminou
     def jogoAcabou(self):	
          if "_" in self.letras_descobertas:
               print("\nVocê perdeu, a palavra era:", palavra)

	# Método para verificar se o jogador venceu
	def venceu(self):
          if "_" not in self.letras_descobertas:
               print("\nVocê venceu, a palavra era:", palavra)

	# Método para não mostrar a letra no board
	def naoLetra(self):
	# Método para checar o status do game e imprimir o board na tela
     def imprimeBoard(self):


jogo = Hangman()
jogo = adivinhaLetra()