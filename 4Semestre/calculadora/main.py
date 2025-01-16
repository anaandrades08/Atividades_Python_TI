"""
ANA CLAUDIA NOGUEIRA ANDRADES TECNOLOGIA DA INFORMAÇÃO
Checkout de Presença do Módulo 3 - Desenvolvimento baseado em componentes
App 1: Calculadora Simples com Componentes Reutilizáveis
Se você escolheu o App 1 (Calculadora Simples com Componentes Reutilizáveis):
Crie/use pelo menos dois componentes reutilizáveis para operações matemáticas
(adição, subtração, multiplicação e divisão),  usando, caso queira, a biblioteca SymPy ou math;
Documente cada componente;
Desenvolva uma interface de linha de comando usando a biblioteca Click para interagir com os componentes.
Para o App 1 (Calculadora Simples com Componentes Reutilizáveis), você pode utilizar as seguintes bibliotecas:
SymPy (Biblioteca para Matemática Simbólica em Python).
Biblioteca math (Parte da Biblioteca Padrão do Python).
Para criar interfaces de linha de comando em Python em ambos os Apps:
Biblioteca Click.
"""

# Importar bibliotecas click e sympy
import click
import sympy as sp

# Definir os componentes reutilizáveis para operações matemáticas
# Função soma, subtracao, multiplicacao e divisao
def soma(a, b):
    print(f"Somando: {a} + {b}")
    return a + b


def subtracao(a, b):
    print(f"Subtraindo: {a} - {b}")
    return a - b

def multiplicacao(a, b):
    print(f"Multiplicando: {a} * {b}")
    return a * b

def divisao(a, b):
    if b != 0:
        print(f"Dividindo: {a} / {b}")
        return a / b
    else:
        return "Não é possível dividir por zero"

# incio da função calcular com a biblioteca click
@click.command()
#@click.option('--operacao', prompt='Digite a operação (soma, subtracao, multiplicacao, divisao)')
@click.option('--operacao', prompt='Digite a operação (1-soma, 2-subtracao, 3-multiplicacao, 4-divisao)')
@click.option('--valor1', prompt='Digite o primeiro valor')
@click.option('--valor2', prompt='Digite o segundo valor')
def calcular(operacao, valor1, valor2):
    #Calculadora Simples com Componentes Reutilizáveis.
    valor1 = float(valor1)
    valor2 = float(valor2)
    #click.echo(operacao)
    if operacao == '1' or operacao == 'soma' or operacao == '2' or operacao == 'subtracao' or operacao == '3' or operacao == 'multiplicacao' or operacao == '4'  or operacao == 'divisao':
        if operacao == '1' or operacao == 'soma':
            resultado = soma(valor1, valor2)
            click.echo(f"Resultado da soma: {resultado}")
        if operacao == '2' or operacao == 'subtracao':
            resultado = subtracao(valor1, valor2)
            click.echo(f"Resultado da subtração: {resultado}")
        if operacao == '3' or operacao == 'multiplicacao':
            resultado = multiplicacao(valor1, valor2)
            click.echo(f"Resultado da multiplicação: {resultado}")
        if operacao == '4'  or operacao == 'divisao':
            resultado = divisao(valor1, valor2)
            click.echo(f"Resultado da divisão: {resultado}")
    else:
        click.echo("Operação inválida. Por favor, escolha entre 1-soma, 2-subtracao, 3-multiplicacao, 4-divisao")


if __name__ == '__main__':
    calcular()