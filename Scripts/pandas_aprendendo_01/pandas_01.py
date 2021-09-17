import pandas as pd
# df.loc[<linhas>, <colunas>] -> linhas e dps colunas
# loc é baseado nas labels das colunas, mas podemos utilizar um array boolean
# quando o loc não encontrar nenhum item ele retorna KeyError
# podemos usar o loc assim ó: df.loc[[5]] pra chamar pelo índice, ou df.loc[[0,1,2]], neste segundo jeito veremos os elemtnos 0, 1, 2
# fatiando usando loc df.loc[2:3] (neste método a final e a inicial conta n é q nem o python chatao)
# chamando diretamente pela linha: df.loc['1, Artist']
# chamando pelo array:


def separador():
    print('-' * 100)

csv_path = 'TopSellingAlbums.csv'  # local do csv
df = pd.read_csv(csv_path)  # lendo o csv e tendo o read_csv apontando pro local do csv
print(df.head())  # o head é pra examinar as 5 primeiras linhas

xlsx_path = 'TopSellingAlbums.xlsx'  # local do excel file
df = pd.read_excel(xlsx_path)  # lendo o excel e tendo o read-excel apontando pro local do excel
print(df.head())  # head é pra examianr as 5 primeiras linhas

separador()

x = df[[
    'Length']]  # para vermos as colunas como se fossem uma série, tipo um embaixo do outro, e tbm estamos vendo a duração de cada álbum
print(x)

separador()

x = df[['Artist']]  # pegando as colunas como se fossem data frames
print(type(x))  # estamos vendo que o tipo é um data frame

separador()

y = df[['Artist', 'Length', 'Genre']]  # Acessando múltiplas colunas do nosso CSV
print(y)

separador()

print(df.iloc[0,0]) # para acessar a primeira linha e primeira coluna usamos o método iloc
#output: michael jackson

separador()

print(df.iloc[1,0]) # acessando 2 linha e 1 coluna:
#output: AC/DC

separador()

print(df.iloc[0,2]) #valor da linha 1 e coluna 3:
#output: 1982

separador()

print(df.iloc[1,2]) #valor da linha 2 e coluna 3
#output: 1980

separador()

#acessando colunas utilizando o próprio nome delas:
print(df.loc[1, 'Artist']) # 01 = linha 1 (q é a 2 pq tem a frescura q começa no 0), e 'artist' é o nome da coluna q qeuremos ver
#output acdc
separador()

print(df.loc[0, 'Released'])
#output 1982

separador()

#slicing a data frame
#podemos sliçar usando ambos os index é o nome da coluna

print(df.iloc[0:2, 0:3]) # usando o index LINHA, COLUNA ESTA É A ORDEM OK, linha 0, até o index 2, e as colunas da coluna 0 até a 3

separador()

#usando nome
print(df.loc[0:2, 'Artist':'Length']) # pegando as linhas 0, 1,2 e as colunas de artista até length