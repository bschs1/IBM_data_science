#file01 = open('exemplo02.txt', 'w') #'w' é writting, to cirando outro file.txt
#file01.write("LINHA 01\n")
#file01.write("LINHA 02\n")

# lines = ["Linha 01\n","Linha 02\n","Linha 03\n","Linha 04\n",]
# with open('exemplo02.txt','w') as file1:
#     for line in lines:
#         file1.write(line)
#         print(line)

with open('exemplo01.txt', 'r') as readfile:
    with open('exemplo03', 'w') as writefile:
        for line in readfile:
            writefile.write(line)
            print(line)
#o for loop armazena no exemplo 3 o que ta no readfile(exemplo01) e via copiando linha por linha até o final em q o arquivo é fechado.