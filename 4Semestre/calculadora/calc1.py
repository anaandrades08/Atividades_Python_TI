import click
import sympy as sp


# Definir os componentes reutilizáveis para operações matemáticas
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"


@click.command()
@click.option('--operacao', prompt='Digite a operação (soma, subtracao, multiplicacao, divisao)')
@click.option('--valor1', prompt='Digite o primeiro valor')
@click.option('--valor2', prompt='Digite o segundo valor')
def calcular(operacao, valor1, valor2):
    """Calculadora Simples com Componentes Reutilizáveis."""
    valor1 = float(valor1)
    valor2 = float(valor2)

    if operacao == 'soma':
        resultado = soma(valor1, valor2)
        click.echo(f"Resultado da soma: {resultado}")
    elif operacao == 'subtracao':
        resultado = subtracao(valor1, valor2)
        click.echo(f"Resultado da subtração: {resultado}")
    elif operacao == 'multiplicacao':
        resultado = multiplicacao(valor1, valor2)
        click.echo(f"Resultado da multiplicação: {resultado}")
    elif operacao == 'divisao':
        resultado = divisao(valor1, valor2)
        click.echo(f"Resultado da divisão: {resultado}")
    else:
        click.echo("Operação inválida. Por favor, escolha entre soma, subtracao, multiplicacao ou divisao.")


if __name__ == '__main__':
    calcular()