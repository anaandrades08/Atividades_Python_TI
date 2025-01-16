#declararação da lista de frutas
listafrutas = []
#Declaração de váriaveis
nfrutas = 0
i = 0
n = 0

#INPUT Entrada de dados: Informar a quantidade de frutas a cadastrar
print("Digite a quantidade de Frutas a cadastrar: ")
nfrutas = int(input())
#FUNÇÃO CADASTRO DE FRUTAS
#Entrada de dados, guarda informação numa lista de frutas, com dois parametros, nome da fruta e preço
def cadastrofrutas(nfrutas, listafrutas):
    # INPUT Entrada de dados: Informar o nome da fruta
    print("Digite o nome da fruta: ")
    hortifruti = str(input())
    # Transformar o a entrada de dados em maiusculo
    hortifruti = hortifruti.upper()
    #IF condição para verificar se a fruta não foi cadastrada
    if hortifruti not in listafrutas:
        # Adicionar nome da fruta a lista de frutas
        listafrutas.append(hortifruti)
        # INPUT Entrada de dados: Informar o preço da fruta
        print("Digite o valor dessa fruta: ")
        preco = float(input())
        # Adicionar preço da fruta a lista de frutas
        listafrutas.append(preco)
        #Contador decrescente
        nfrutas = nfrutas - 1
    #ELSE condição para verificar se fruta ja foi cadastrada
    else:
        #OUTPUT Saída de dados - Produto já cadastrado
        print("Produto já cadastrado")

#FUNÇÃO BUSCAR FRUTAS
#Guarda informação numa lista de frutas, com nome da fruta e preço
def buscador(hortifruti, listafrutas):
    # IF condição para procurar a fruta na lista de frutas
    if hortifruti in listafrutas:
        #variavel i a posiçao da fruta na lista
        i = listafrutas.index(hortifruti)
        #OUTPUT Saída de dados Escreve preço da fruta
        print(listafrutas[i + 1])
    #ELSE condição se não tem a fruta cadastrada na lista
    else:
        #OUTPUT Saída de dados: produto não cadastrado
        print("Produto nao cadastrado")
        #finaliza execução
        exit()

#WHILE Estrutura de repetição: enquanto numero de frutas a cadastrar for maior que o contador n
while nfrutas > n:
        #Chama função cadastrofrutas
        cadastrofrutas(nfrutas, listafrutas)
        #incrementa o contador
        n += 1

#INPUT Entrada de dados: Procurar uma fruta
print("Procure uma fruta: ")
hortifruti = str(input())
#Transformar o a entrada de dados em maiusculo
hortifruti = hortifruti.upper()

#WHILE estrutura de repetição: enquanto Procurar fruta for diferente de fim
while hortifruti != "FIM":
    #Chamar a função buscador de fruta
    buscador(hortifruti, listafrutas)
    #INPUT Entrada de dados: Procurar outra fruta
    print("Procure outra fruta: ")
    hortifruti = str(input())
    #Transformar o a entrada de dados em maiusculo
    hortifruti = hortifruti.upper()

#IF Condição: Se comando for igual a fim
if hortifruti == "FIM":
    # finaliza execução
    exit()