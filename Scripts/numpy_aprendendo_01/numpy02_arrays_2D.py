import numpy as np
import matplotlib.pyplot as plt

#O que vou ver nessa aula?
    #Criação de arrays 2D
    #Indexing e Slicing de Arrrays 2D
    #Operações básicas em Arrays 2D

#[start:end:step] -> ARRAY SLICING

# Slicing in python means taking elements from one given index to another given index.
#
# We pass slice instead of index like this: [start:end].
#
# We can also define the step, like this: [start:end:step].
#
# If we don't pass start its considered 0
#
# If we don't pass end its considered length of array in that dimension
#
# If we don't pass step its considered 1


def separador():
    print('************************************************************************\n' )

#arrays 2D
print('abaixo uma lista contendo outras listas aka nested lists todas com o mesmo tamanho:')
a = [[11,12,13], [21,22,23], [31,32,33]]
print(a)
separador()

print('transformando uma lista em um array: ')
a = np.array(a)
print(type(a))
separador()

print('Número de nested lists:')
print(f'O Número de Dimensões do array: {np.ndim(a)}')
print(f'O Shape {np.shape(a)}, E Retorna uma tupla dizendo que nesse caso é 3 por 3')
print(f'O Tamanho do array: {np.size(a)}')

print(f'Shape: {a.shape}') # shape
print(f'Size:  {a.size}')
print(f'Numero de Dimensões: {a.ndim}')
separador()

print('Acessando elementos do array: ')
print(f'segunda linha, segunda coluna temos o elemento:\n {a[1,2]}') # segunda linha, 2 coluna
print(f'Segunda Linha e Terceira Coluna temos o elemento:\n {a[1][2]}') # mesma coisa da linha 36, mas da p ser desse jeito
print(f'Acessando Linha 0 e Coluna 0 temos o elemento:\n {a[0,0]}' )
separador()

print('Slicing de Arrays 2D')
# print('we can also use slicing in numpy arrays. Consider the following figure. We would like to obtain the first two columns in the first row')
print(f'Acessando os elementos da primeira Linha e Primeira e Segunda Coluna: {a[0][0:2]}') # o [0:2] SIGNIFICA ACESAR AS PRIMEIRAS 2 COLUNAS
print(f'Acessando as Duas Primeiras Linhas da Terceira Coluna: {a[0:2, 2]}') # o [0:2] CORRESPONDE AS DUAS PRIMEIRAS LINHAS E O ,2 É A COLUNA
print(np.array(a))
print(f'{a[0,1:3]}')
separador()

print('Operações Básicas')
print('Soma de Arrays:')
x = np.array([[1,0], [0,1]])
print(f'Array X: \n{x}')
y = np.array([[2,1], [1,2]])
print(f'Array Y: \n{y}')
print(f'Somando os Arrays X e Y:')
z = x +y
print(f'O valor de Z é: \n{z}')
separador()

print('Multiplicação de Arrays')
Y = np.array([[2,1], [1,2]])
print(f'O Array Y: \n {Y}')
print(f'Multiplicando o Array Y por 2 Temos: \n{y * 2}')
print('Voltando O Array Y para seu valor normal: ')
Y = np.array([[2,1], [1,2]])
print(Y)
X = np.array([[1,0], [0,1]])
print(f'O Valor do Array X é: \n{x}')
Z = x * y
print(f'Multiplicando o ARRAY X POR Y TEMOS: \n{z}')
separador()

print('Criando uma Matriz')
A = np.array([[0,1,1], [1,0,1]])
print(f'Matriz A = \n {A}')
B = np.array([[1,1], [1,1], [-1,1]])
print(f'Matriz B= \n {B}')
Z = np.dot(A,B)
print(f'A Multiplicação DOT das Matrizes A e B Resultam em: \n {Z}')
print('A DOT funciona assim: ')
k, l = np.arange(3), np.arange(3, 6)
print(k)
print(l)
print(np.dot(k,l))
print('retorna 14')
print('Retorna 14 pq multiplicando as duas matrizes vc vai ter 14 -> a conta: ')
print('3x0 + 1x4 + 2x5 = 14')
separador()
print(f'Seno de Z {np.sin(z) }')
print('Criando a Matriz C: ')
C = np.array([[1,1], [2,2], [3,3]])
print(f' A Matriz C = \n {C}')
#print(f'Matriz transposta de C : {C.transpose()}')
separador()

q = np.array([[1,0],[0,1]])
print(q)
separador()
w = np.array([[0,1],[1,0]])
print(w)
separador()
print(q + w)


separador()

o = np.array([[1,0],[0,1]])
print(o)
separador()

p = np.array([[2,2],[2,2]])
print(p)
separador()
print(np.dot(o, p))