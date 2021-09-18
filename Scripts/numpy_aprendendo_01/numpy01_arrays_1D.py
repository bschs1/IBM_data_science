import numpy as np
import matplotlib as plt


# pra que serve? pra trabalahar com array,, listas melhores, mais rápido, e é a base do pandas

# o que vamos fazer?
    # Criação básica de arrays
    # Indexing e Slicing (index é índice)
    # Basic Operations
    # Funções Universais

print('NESTE ARQUIVO SÃO TUDO RELACIONADO A ARRAY 1D')

def separador():
    print('************************************************************************\n' )

#USANDO PRA 1D ARRAYS
a = np.array([0,1,2,3,4]) # 0 Based, começa do 0
print(a) # printando o array
print(a[4]) # usamos o [ÍNDICE] pra acessar o valor que queremos, no caos quero o 4 elemtento '4'
print(type(a)) # o tipo do array, ou seja np array
print(a.dtype) # int 32, ou seja 32 bits
print(a.size) # tamanho do array
print(a.ndim) # número de dimensões do array
print(a.shape) # é uma tupla que mostra o numero de elementos em cada dimensão do array
mean = a.mean() # Basciamente tira a média
print('média é:', mean) #é a media
max_a = a.max()
min_a = a.min()
print(f'O minimo é: {min_a} ,e o máximo é: {max_a}')
standard_deviation = a.std() #desvio padrão
print(f'O Desvio padrão é: ',standard_deviation) # desvio padrão
separador()
b = np.array([3.1,11.02,6.2,213.2,5.2])
print(b) # mostrando o array
print(type(b)) # tipo de array
print(b.dtype) # float 64, é o tipo d memoria

separador()
#index and slicing

c = np.array([20,1,2,3, 4]) # criando o array
print(c) # printando o array
c[0] = 100 # mudando o valor do primeiro elemento pra 100
print(c)
d = c[1:4] # pegando do elemento 01 que é o numero 1, até o elemento 4 que é o numero 3
print(d)
c[3:5] = 300, 400 # alterando os valores dos elementos 3 e 5, para 300 e 400 respectivamente
print(c)
separador()
print('confesso q essa parte daqui n entendi direito n')
select = [0,2, 3] # criando uma lista indexada
d = c[select] #usando a lista pra selecionar elementos, colocamos a lista como argumento
print(d)
c[select] = 100000
print(c)
separador()

#operações básicas
# vetores: se for [1] desse jeito, com o 1 em cima vai apontar pra -> (horizontal)           [0] o 0 em cima quer dizer q n se move na horizontal
#                 [0] o de baixo é da vertical, e como é 0 não se move                       [1] o 1 embaixo quer dizer q ele se movimenta na vertical
#somando dois vetores:
u = [1,0]
v = [0,1]
z = []
for n, m in zip(u,v): #zip é um método pra retornar um iterador nas tuplas no primeiro item de cada, dps no segundom, terceiro e bla
    z.append(n+m)
    print(z)

print('ou: ')
z = u + v
print(f' o valor da soma doas arrays u + v é:  {z}')
separador()

print('agora usando numpy')

u = np.array([1,0])
v = np.array([0,1])
z = u + v
print(z)

separador()

#multiplicação de arrays

print('Múltiplação e Arrays: ')
y = np.array([1,2])
print(y)
z = 2 * y
print('multiplicando o array y por 2 temos: ', z)
separador()
print('produto de 2 arrays:')
u = np.array([1,2])
print(f'o array u: {u}')
separador()
v = np.array([3,2])
print(f' o array v é {v}')
separador()
z = u * v
print(f'o produto dos dois arrays é: {z}')
separador()
print(f'dot multiplciation: {np.dot(u,v)}')
separador()

print('colocando uma constante nos arrays por ex o array [1,2,3, -1] com a constante ficaria assim: [1+1,1+2,1+3]')
u = np.array([1,2,3, -1])
u + 1
print(u)
separador()

print('Funções Matemáticas')
print(np.pi)

x = np.array([0, np.pi/2 , np.pi])
print(x)

y = np.sin(x)
print(x)

print('Linspace: Linspace retorna números espaçados de modo uniforme em um intervalo. '
      'Dessa forma, dado um ponto inicial e de parada, assim como a quantidade de valores, '
      'linspace irá distribuí-los uniformemente para você em uma matriz NumPy. '
      'Isso é especialmente útil para visualizações de dados e declaração de eixos durante a plotagem.')
print(np.linspace(1.0, 10.0, num = 5)) # 1.0 = ponto de partida, 10.0 = ponto de parada, 5 = quantidade de valores

print(f'agora 9 números separados even de -2 até 2: {np.linspace(-2,2, num=9)}')