print(str("Informe o nome da cidade: "))
nome_cidade = input(str())
print(str("Informe o numero de habitantes: "))
num_hab = input(float())
print(str("Informe o o nome do estado: "))
estado_cidade = input(str())
print(str("Informe o tamanho da cidade: "))
tamanho_cidade = input(float())
print(str("Informe se possui metrô: "))
metro_cidade = input(str())
print(nome_cidade,"-",estado_cidade)
print("Possui: ", num_hab, " habitantes")
print("Area da cidade: ",tamanho_cidade)
if ((metro_cidade=="Sim") or (metro_cidade=="sim") or
(metro_cidade=="Não") or (metro_cidade=="Nao") or
(metro_cidade=="não") or (metro_cidade=="nao")):
 print("Possui metro: ",metro_cidade)
else:
 print(metro_cidade, " esta inválido essa resposta para metrô.")