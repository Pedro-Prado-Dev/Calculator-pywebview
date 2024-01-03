from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    operacao = data.get('operacao')
    numero1 = data.get('numero1')
    numero2 = data.get('numero2')

    if operacao == 'soma':
        resultado = numero1 + numero2
    elif operacao == 'subtracao':
        resultado = numero1 - numero2
    elif operacao == 'multiplicacao':
        resultado = numero1 * numero2
    elif operacao == 'divisao':
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            return jsonify({'erro': 'Divisão por zero não é permitida!'}), 400
    else:
        return jsonify({'erro': 'Operação inválida!'}), 400

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run()
