import time
import random
def loopParaSomarTempo(n):
    soma = 0
    i=1
    j=1
    for i in valores_n:
        for j in valores_n:
            aleatorio = random.randint(1, 1000)
            soma += aleatorio
            print(soma)

print("::::::::::::::::::::::::::::::")   
print("Algoritmo2")
valores_n = [10, 100, 1000]

for n in valores_n:
        inicio1 = time.time()
        resultado=loopParaSomarTempo(n)   
        fim1 = time.time()
        tempoexecucao1=((fim1 - inicio1))
        print("n:",n)
        print(resultado)
        print(tempoexecucao1)
        print("::::::::::::::::::::::::::::::")