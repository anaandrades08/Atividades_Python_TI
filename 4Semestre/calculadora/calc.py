# Importar a biblioteca SymPy
import sympy as sp

# Componente de soma
def soma(a, b):
    return a + b

# Componente de subtração
def subtracao(a, b):
    return a - b

# Componente de multiplicação
def multiplicacao(a, b):
    return a * b

# Componente de divisão
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é definida"

# Interface de linha de comando usando Click
import click

@click.command()
@click.option('--operacao', prompt='Operação (soma, subtracao, multiplicacao, divisao)',
              help='Escolha a operação matemática')
@click.option('--num1', prompt='Primeiro número', type=float, help='Digite o primeiro número')
@click.option('--num2', prompt='Segundo número', type=float, help='Digite o segundo número')
def main(operacao, num1, num2):
    # Realiza a operação selecionada
    if operacao == 'soma':
        resultado = soma(num1, num2)
    elif operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"

    # Exibe o resultado
    click.echo(f"Resultado da operação {operacao}: {resultado}")

if __name__ == '__main__':
    main()