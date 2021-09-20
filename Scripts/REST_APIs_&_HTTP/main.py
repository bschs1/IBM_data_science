import requests
import os
from PIL import Image
from IPython.display import IFrame

#Requests em python
#Get Requests
#Gost Requests

def separador():
    print('*' * 10)

url = 'https://www.ibm.com'
r = requests.get(url)
print(r.status_code) #pede o status code
print(r.request.body) #pede o body
print(r.request.headers) #pede o header
print('request body: ', r.request.body) # msm coisa do request body do de cima
header = r.headers # retorna um dicionario do http header
print(r.headers)
print(header['date']) # retorna a data do request
print(header['Content-Type']) # retonra o content type
print(header['Cache-Control']) # retorna o cache control
print(r.text[0:100]) # podemos usar o text pra mostra o HTML, e eu to selecionando os 100 primeiros caracteres
separador()

url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png' # um link de imagem
r = requests.get(url) # fazendo request do URL
print(r.headers) # imprimindo o header
print(r.headers['Content-Type']) # retornando o content type
print('agora vamos codar pra conseguir ver a imagem em sí')
path = os.path.join(os.getcwd(), 'image.png')
print(f'local q a imagem foi salva: {path}')
print('salvando a imagem: ')
with open(path,'wb') as f: # usamos o 'wb' pra dizer que é  escrita em binario
    f.write(r.content) # salvando a imagem

Image.open(path) # abrindo a imagem

separador()

print('Get Requests com parametros de URL')
url_get = 'http://httpbin.org/get'
print('Query String')
# é basicamente pra mandar uma query pro servidor
# a estrutura é assim: começa com (?) q significa start of query, seguido por um parametro de nome (name), (=), valor (value (joseph)), & (ID) = (123)
#ficando assim: http://httpbin.org/get? Name=Joseph&ID=123
payload = {'name': "Joseph", 'ID': '123'} # nome > joseph, ID > 123 ( a estrutura é de um dicionario, key -> value). The keys are the parameter names and the values are the value of the Query string
r = requests.get(url_get, params=payload) # url get = site, parametros = variaveol paylaod q é o dicionario com a query e os values
print(r.url)
print(r.status_code) # status code
print(r.text) # texto
print(r.headers['Content-Type']) # deve retornar q é um JSON
print(r.json()) # visualizando o json
separador()
print(r.json()['args']) # Vendo os args (argumentos)
separador()

print('Posts Requests')
print('Post Requests é tipo get request mas utilizado pra mandar dados pro servidor em um body')
url_post='http://httpbin.org/post'
print('fazendo um post request usa-se post() e a variavel payload é pro parametro DATA')
r_post = requests.post(url_post, data = payload)
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
print(r_post.json()['form'], 'Visualizar em Json') # vendo em JSON a