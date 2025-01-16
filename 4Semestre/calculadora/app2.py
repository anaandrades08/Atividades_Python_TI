import click
from pint import UnitRegistry

# Criando um registro de unidades
ureg = UnitRegistry()

# Função para converter unidades de temperatura
def converter_temperatura(valor, unidade_origem, unidade_destino):
    try:
        valor_convertido = ureg(valor + unidade_origem).to(unidade_destino).magnitude
        return valor_convertido
    except Exception as e:
        return f"Erro ao converter unidades de temperatura: {str(e)}"

# Função para converter unidades de comprimento
def converter_comprimento(valor, unidade_origem, unidade_destino):
    try:
        valor_convertido = ureg(valor + unidade_origem).to(unidade_destino).magnitude
        return valor_convertido
    except Exception as e:
        return f"Erro ao converter unidades de comprimento: {str(e)}"

# Definindo a interface de linha de comando com Click
@click.command()
@click.option('--tipo', prompt='Tipo de Conversão (temperatura/comprimento)',
              help='Escolha o tipo de conversão (temperatura ou comprimento)')
@click.option('--valor', prompt='Valor a Converter', type=float,
              help='Digite o valor a ser convertido')
@click.option('--origem', prompt='Unidade de Origem',
              help='Digite a unidade de origem da conversão')
@click.option('--destino', prompt='Unidade de Destino',
              help='Digite a unidade de destino da conversão')
def converter_unidades(tipo, valor, origem, destino):
    if tipo.lower() == 'temperatura':
        resultado = converter_temperatura(valor, origem, destino)
    elif tipo.lower() == 'comprimento':
        resultado = converter_comprimento(valor, origem, destino)
    else:
        resultado = "Tipo de conversão não suportado. Escolha entre 'temperatura' ou 'comprimento'."

    click.echo(f"Resultado da conversão: {resultado}")

if __name__ == '__main__':
    converter_unidades()