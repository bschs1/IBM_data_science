#file1 = open("exemplo01.txt", 'r')
#print(file1.name)
#print(file1.mode)
#file1.close()

#with statment
# with open('exemplo01.txt','r') as file1: #o with automaticamente fecha a file dps, esse bloco de código vai ler tudo no bloco e dps fechar
#     file_stuff=file1.read() #o metodo read armazena os valores do arquivo na varaivel file_stuff como uma string
#     print(file_stuff) #print o que tem na file
#
# print(file1.close()) #checa p ver se fechou a file
# print(file_stuff) #checa o conteudo da file
#

# with open('exemplo01.txt','r') as file1:
#     # file_stuff = file1.readline() #readline é pra ler a primeira linha, e ta sendo salvo na variavel file_stuff
#     # print(file_stuff)
#     # file_stuff = file1.readline() #usando dnv vai ler a segunda linha
#     # print(file_stuff)
#     #file_stuff = file1.readline(4) # colocando o numero de strings que vai ler da linha 01
#     #print(file_stuff)
#     ########## fazendo um loop contador de linhas ######
#     for x in file1:
#         print(x)

