# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")


# Definindo as funções

def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):  
    return a / b
def potencia(a,b):
    return a ** b

numEscolhido = 0


while numEscolhido != 5:
    print("\nEscolha uma operação:")
    print("1 - Soma \n")
    print("2 - Subtração \n")
    print("3 - Multiplicação \n") 
    print("4 - Divisão \n")
    print("5 - Sair \n")
    numEscolhido = int(input("Escolha uma opção: "))
    
    if numEscolhido == 1:
        print("Você escolheu a soma!")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"O resultado da soma entre {num1} e {num2} é:", soma(num1, num2))

    elif numEscolhido == 2:
        print("Você escolheu a subtração!")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"O resultado da subtração entre {num1} e {num2} é:", subtracao(num1, num2))
    elif numEscolhido == 3:
        print("Você escolheu a multiplicação!")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"O resultado da multiplicação entre {num1} e {num2} é:", multiplicacao(num1, num2))
    elif numEscolhido == 4:
        print("Você escolheu a divisão!")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 == 0:
            print("Divisão por zero não é permitida!")
        else:
            print(f"O resultado da divisão entre {num1} e {num2} é:", divisao(num1, num2))
    elif numEscolhido == 5:
        print("Voce escolheu sair, Adeus!")

        numEscolhido = int(input("Deseja continuar o programa? (1 - Sim / 2 - Não): "))
        if numEscolhido == 1:
            numEscolhido = 5
        else:
            numEscolhido = 0