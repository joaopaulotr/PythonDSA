print("\n******************* Lista Exercícios Cap06 *******************")

# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
print("\n===============================================================")
print("Exercício 1\n")
lista = [1,2,3]
for i in lista:
    print("A terceira potencia do",i,"elemento é:",i**3)

print("\n===============================================================")
# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
# palavras = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'.split()
# resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
# for i in resultado:
#     print(i)
print("\n===============================================================")
print("Exercício 2\n")
palavras = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'.split()
def ex02(texto):
    resultado = [texto.upper(), texto.lower(), len(texto)]
    return resultado

print(list(map(ex02, palavras)))


print("\n===============================================================")
# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
# matrix = [[1, 2],
#           [3, 4],
#           [5, 6],
#           [7, 8]]
print("\n===============================================================")
print("Exercício 3\n")
matrix = [[1, 2],
          [3, 4],
          [5, 6],
          [7, 8]]

matix02 = [[1,3,5,7],
           [2,4,6,8]]

transposta = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposta)

print("\n===============================================================")
# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo.
# Aplique as duas funções aos elementos da lista abaixo.
# Obs: as duas funções devem ser aplicadas simultaneamente.
# lista = [0, 1, 2, 3, 4]
print("\n===============================================================")
print("Exercício 4\n")

lista = [0, 1, 2, 3, 4]
def elevaQuad(e):
    return(e**2) 
def elevaCub(e):
    return(e**3)

lista02 = [(elevaQuad(x), elevaCub(x)) for x in lista]
print(lista02)

print("\n===============================================================")
# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado
# ao elemento correspondente na listaB.

print("\n===============================================================")
print("Exercício 5\n")

listaA = [2, 3, 4]
listaB = [10, 11, 12]

for i in range(0,3):
    print(listaA[i] ** listaB[i],"\n")

print("\n===============================================================")
# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar
# apenas os valores negativos.
print("\n===============================================================")
print("Exercício 6\n")

def is_negative(num):
    return num < 0

negativos = list(filter(is_negative, range(-5, 5)))

print(negativos)


print("\n===============================================================")
# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
print("\n===============================================================")
print("Exercício 7\n")

a = [1, 2, 3, 5, 7, 9]
b = [2, 3, 5, 6, 7, 8]

# Função para verificar se um elemento está em b
def is_common(x):
    return x in b

comuns_filter = list(filter(is_common, a))
print(comuns_filter)

print("\n===============================================================")
# Exercício 8 - Considere os dois dicionários abaixo.
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 4, 'd': 5}
print("\n===============================================================")
print("Exercício 8\n")

dict3 = dict(zip(dict1, dict2.values()))
print(dict3)

print("\n===============================================================")
# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("\n===============================================================")
print("Exercício 9\n")

for i in range(len(lista)):
    print(f"Índice: {i}, Valor: {lista4[i]}")

print("\n===============================================================")
# Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras
# Data e Science na frase: 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'
print("\n===============================================================")
print("Exercício 10\n")

import re

frase = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'

padrao = r'\b(?:Data|Science)\s+(\w+)'

resultados = re.findall(padrao, frase)

print(resultados)


print("\n===============================================================")