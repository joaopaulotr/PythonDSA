# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. 
# Se o dia for igual a Domingo ou igual a sábado, imprima na tela "Hoje é dia de descanso", 
# caso contrário imprima na tela "Você precisa trabalhar!"

diaSemana = input("Digite o dia da semana:").lower() 

if diaSemana == "domingo" or diaSemana == "sabado":
    print("Hoje é dia de descanso")
else: 
    print("Você precisa trabalhar!")

print("========================================================================")
# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

listaFrutas = ['Morango', 'Abacaxi', 'Laranja', 'Pera', 'Kiwi']
for fruta in listaFrutas:
    if fruta == 'Morango':
        print("Morango é uma das frutas")

print("========================================================================")
# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 
# e guarde os resultados em uma lista

tupla = (1,2,3,4)
lista = []

for elemento in tupla:
    lista.append(elemento * 2)

print(lista)

print("========================================================================")
# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

for x in range(100, 151):
    print(x)

print("========================================================================")
# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. 
# Enquanto temperatura for maior que 35, imprima as temperaturas na tela

temperatura = 40

if temperatura > 35:
    print(temperatura)        

print("========================================================================")
# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto contador for menor que 100, 
# imprima os valores na tela, mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0

while contador < 100:
    if contador == 23:
        print(contador)
        break  
    print(contador)
    contador += 1
        

print("========================================================================")
# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

lista = []
variavel = 4

for variavel in range(4,21,2):
    lista.append(variavel)

print("========================================================================")
# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)

nik = []

for num in range(5,45,2):
    nik.append(num)
print(nik)

print("========================================================================")
# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
# temperatura = float(input('Qual a temperatura? '))
# if temperatura > 30
# print('Vista roupas leves.')
# else
#     print('Busque seus casacos.')

temperatura = float(input('Qual a temperatura? '))

if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

print("========================================================================")
# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. 
# Use um placeholder na sua instrução de impressão
# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.”

frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão."

contador_r = 0

for caractere in frase:
    if caractere.lower() == "r":
        contador_r += 1

print(contador_r)

print("========================================================================")
# Exercício 11 - Crie uma função que imprima a sequência de números pares entre 1 e 20 
# (a função não recebe parâmetro) e depois faça uma chamada à função para listar os números

def imprimeNum():
    for numeros in range(1,21):
        if numeros % 2 == 0:
            print(numeros)

imprimeNum()

print("========================================================================")
# Exercício 12 - Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas. 
# Faça uma chamada à função, passando como parâmetro uma string
fraseEx = "Exemplo Transformar Upper"

def maius(palavra):
    return palavra.upper()

print(maius(fraseEx))

print("========================================================================")
# Exercício 13 - Crie uma função que receba como parâmetro uma lista de 4 elementos, 
# adicione 2 elementos à lista e imprima a lista

lista4el = [1,2,3,4]
lista2el = [5,6]

def recebe4el(lista):
    lista += lista2el
    return lista
    
print(recebe4el(lista4el))

print("========================================================================")
# Exercício 14 - Crie uma função que receba um argumento formal e uma possível lista de elementos. 
# Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def recebeArg(argumento):
    return argumento

lista9 = [1,2,3,4]
print(recebeArg(3))
print(recebeArg(lista9))

print("========================================================================")
# Exercício 15 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. 
# A expressão vai receber 2 números como parâmetro e retornar a soma deles

soma = lambda x, y: x + y
print(soma(5, 3)) 

print("========================================================================")
# Exercício 16 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma(arg1, arg2):
    total = arg1 + arg2
    print("Dentro da função o total é: ", total)
    return total
soma(10, 20)
print("Fora da função o total é: ", total)

print("========================================================================")
# Exercício 17 - Abaixo você encontra uma lista com temperaturas em graus Celsius. 
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função. 
# Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda c: (c * 9/5) + 32, Celsius)
print(list(Fahrenheit))

print("========================================================================")
# Exercício 18 - Crie uma list comprehension que imprima o quadrado dos números de 1 a 10

[print(x*x) for x in range(1,11)]

print("========================================================================")
# Exercício 19 - Crie uma list comprehension que imprima as palavras com a letra a no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]

[print(palavra) for palavra in palavras if "a" in palavra]

print("========================================================================")
# Exercício 20 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10

lista24 = [i for i in range(1,11) if i < 5]
print(lista24)

print("========================================================================")