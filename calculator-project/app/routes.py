from app import server
from flask import render_template, request

@server.route('/')
def index():
    return render_template('index.html')


@server.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacao = request.form['operacao']

        resultado = calcular(num1, num2, operacao)
        return render_template('index.html', resultado=resultado)

    return render_template('index.html', resultado=None)


def calcular(num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero!"