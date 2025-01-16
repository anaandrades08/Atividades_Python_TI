12############################################################################
#[Checkout de Presença] Módulo 3 – Entrada, saída de dados e modularização
#[2º semestre Tecnologia da Informação]
############################################################################
# Calcular quantidade de combustível
# Calcular distância percorrida
# Consumo médio CM 1KM/L
# VM=S/T CM=S/V
############################################################################
#Declaração de váriaveis, e atribuição de valor inicial
T=0
VM=0
S=0
V=0
CM = 0
#Estrutura
if VM==0 and T==0 and CM==0:
    print("Informe o Tempo gasto na viagem: ")
    T= float(input())
    print("Informe a Velocidade média do carro:")
    VM= float(input())
    print("Consumo médio do carro:")
    CM= float(input())
    #Calculo
    S=float(T*VM)
    V=float(S/CM)
    #Resposta
    print("Viajando a uma velocidade media de ",VM,"Km/h e gastando em torno de ",T," horas")
    print("A distancia percorrida é: ",S," kilometros")
    print("A quantidade de combustível gasta é: ",V," litros")
else:
    print("erro")
