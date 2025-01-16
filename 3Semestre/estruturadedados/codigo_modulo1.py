
def hash_divisao(chave, tamanho_tabela):
    return chave % tamanho_tabela

# Lê a quantidade de chaves e o tamanho da tabela
k, m = map(int, input().split())

# Calcula o endereço-base para cada chave e imprime o resultado
for _ in range(k):
    chave = int(input())
    endereco_base = hash_divisao(chave, m)
    print(f"{chave} -> {endereco_base}")
