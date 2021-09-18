import numpy as np
import matplotlib.pyplot as plt

#O que vou ver nessa aula?
    #Criação de arrays 2D
    #Indexing e Slicing de Arrrays 2D
    #Operações básicas em Arrays 2D


def separador():
    print('************************************************************************\n' )

#arrays 2D
print('abaixo uma lista contendo outras listas aka nested lists todas com o mesmo tamanho:')
a = [[11,12,13], [21,22,23], [31,32,33]]
print(a)
separador()

print('transformando uma lista em um array: ')
a_to_array = np.array(a)
print(type(a_to_array))
separador()

print(f'Shape: {a_to_array.shape}') # shape
print(f'Size:  {a_to_array.size}')
print(f'Numero de Dimensões: {a_to_array.ndim}')
separador()

print('Acessando elementos do array: ')

plt.plot(a_to_array)
print((plt.plot(a_to_array)))