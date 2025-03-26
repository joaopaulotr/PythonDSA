# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

for i in range(1,11):
    lista = [i]
    print(i)

print('======================================')
# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

lista5obj = ['1', '2', '3', '4', '5']
print(lista5obj)

print('======================================')
# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

string1 = 'Ola'
string2 = 'Mundo'
string3 = string1 + ' ' + string2
print(string3) 

print('======================================')
# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tuplaex = (1, 2, 2, 3, 4, 4, 4, 5)
print(tuple.count(tuplaex, 4))

print('======================================')
# Exercício 5 - Crie um dicionário vazio e imprima na tela

dic = {}
print('Dicionario vazio', dic)

print('======================================')
# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

dic02 = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'Valor a imprimir na tela'}
print(dic02['chave3'])

print('======================================')
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

dic02['chave4'] = 'Valor a qualquer'
print(dic02['chave4'])

print('======================================')
# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dic03 = {'chave01': 'valor01', 'chave02': 'valor02', 'chave03': [1, 2]}
print(dic03)

print('======================================')
# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.

lista04 = ["ElementoString", (1,2), {'chave01': 'valor01', 'chave02' : 'valor02'}, 1.0]
print(lista04)

print('======================================')
# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
#frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[0:18])