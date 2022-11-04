from flask import Flask, render_template, request, redirect
import calculo
import sistema

app = Flask(__name__)


@app.route('/')
def indexpag():
    return render_template('index.html', lista_motivo=sistema.motivo_despensa())


@app.route('/', methods=['POST'])
def enviar_dados():
    nome = request.form['nome']
    salario = request.form['salario']
    data_assinatura = request.form['data_assinatura']
    data_recisao = request.form['data_recisao']
    validar_ferias = request.form['validar_ferias']
    motivo = request.form['motivo']
    lista_motivo = sistema.motivo_despensa()
    motivo = (lista_motivo.index(motivo) + 1)

    acerto = calculo.principal(nome, salario, data_assinatura, data_recisao, validar_ferias, motivo)
    acerto = f'R$ {acerto:.2f}'.replace('.', ',')

    return render_template('index.html', lista_motivo=sistema.motivo_despensa(), acerto=acerto)


app.run(debug=True)
