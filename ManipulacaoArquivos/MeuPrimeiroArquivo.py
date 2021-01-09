#arquivo = open("primeiro_arquivo.txt" , "w") #R: READ/W: WRITE/ A:APPEND(READ AND WRITE)/X:EXCLUSIVO

#arquivo.write("Meu primeiro arquivo!")

#arquivo.close()

#with open("primeiro_arquivo.txt" , "w") as arquivo: #with abre o arquivo e manipula ele
    #arquivo.write("\nHakuna Matata!")

#with open("primeiro_arquivo.txt" , "a") as arquivo: #append
    #arquivo.write("\nHakuna Matata!")

with open("primeiro_arquivo.txt" , "r") as arquivo: #read
    conteudo = arquivo.readline()
    for linha in arquivo.readlines():
        print(linha)
