#Algoritmo 2: complexidade O(n^3)
#soma = 0
#recebe um valor inteiro n
#laço de 1 até n
#    laço de 1 até n
#        laço de 1 até n
#            aleatorio = valor aleatório entre 1 e 1000
#            soma = soma + aleatorio
import time
import random
def loopParaSomarTempo(n):
    soma = 0
    for _ in range(n):
        aleatorio = random.randint(1, 1000)
        soma = soma + aleatorio
    return soma

valores_n = [10, 100, 1000]

for n in valores_n:
    for n in valores_n:
        inicio = time.time()
        resultado = loopParaSomarTempo(n)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"n={n}")
        print("Resultado:",resultado)
        print("Tempo de execução:",tempo_execucao,"segundos")
        print("-----------------------------------------")
   