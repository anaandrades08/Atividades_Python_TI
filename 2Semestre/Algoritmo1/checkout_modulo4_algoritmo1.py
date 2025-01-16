########################################################################
# CHECKOUT MODULO 4 - ALGORITMO 1 Lista de cadastro de frutas
# 2º semestre Tecnologia da Informação
########################################################################
listafrutas = []
print("Digite a quantidade de Frutas a cadastrar: ")
nfrutas = int(input())
i = int(0)
n = int(0)
#hortifruti = str("")

def cadastrofrutas(nfrutas, listafrutas):
    print("Digite o nome da fruta: ")
    hortifruti = str(input())
    hortifruti = hortifruti.upper()
    if hortifruti not in listafrutas:
        listafrutas.append(hortifruti)
        print("Digite o valor dessa fruta: ")
        preco = float(input())
        listafrutas.append(preco)
        nfrutas = nfrutas - 1
    else:
        print("Produto já cadastrado")

def buscador(hortifruti, listafrutas):
    if hortifruti in listafrutas:
        i = listafrutas.index(hortifruti)
        print(listafrutas[i + 1])
        # print ("Produto já cadastrado")

    else:
        print("Produto nao cadastrado")
        exit()

while nfrutas > n:
    cadastrofrutas(nfrutas, listafrutas)
    n += 1


# procurar fruta
print("Procure uma fruta: ")
hortifruti = str(input())
hortifruti = hortifruti.upper()

#print(hortifruti)

##while diferente de fim
while hortifruti != "FIM":
    buscador(hortifruti, listafrutas)
    print("Procure outra fruta: ")
    hortifruti = str(input())
    hortifruti = hortifruti.upper()
    #print(hortifruti)1


if hortifruti == "FIM":
    exit()


