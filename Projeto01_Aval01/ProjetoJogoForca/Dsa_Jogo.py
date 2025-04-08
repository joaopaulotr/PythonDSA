# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

# Import
import random
from os import system, name

# Função para limar a tela a cada execução
def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

# Função
def game():

    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ['banana', 'uva', 'morango', 'laranja']
    
    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista para letras erradas
    letras_erradas = []

    while chances < 0:

        print("".join(letras_descobertas))
        print("\nChances Restantes:", chances)
        print("Letras Erradas", " ".join(letras_erradas))
        
        
        tentativa = input("Digite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # COndicional

        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break

    if "_" not in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)
        
if __name__ == "__main__":
    game()
    print("Parabéns, você ganhou")