import numpy as np

# pra que serve? pra trabalahar com array,, listas melhores, mais rápido, e é a base do pandas

# o que vamos fazer?
    # Criação básica de arrays
    # Indexing e Slicing (index é índice)
    # Basic Operations
    # Funções Universais

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
print(mean) #é a media
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
#confesso q essa parte daqui n entendi direito n
select = [0,2, 3] # criando uma lista indexada
d = c[select] #usando a lista pra selecionar elementos, colocamos a lista como argumento
print(d)
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

