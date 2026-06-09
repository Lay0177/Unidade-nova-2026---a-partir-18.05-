from flask import (
    Flask, 
    render_template,
    request,
    redirect,
    url_for,
    make_response
)

app = Flask(__name__)

@app.route('/')
def inicio():
    nome = request.cookies.get('nome', '')
    tema = request.cookies.get('tema', 'claro')
    return render_template('inicio.html', nome=nome, tema=tema)


@app.route('/salvar-nome', methods=['POST'])
def salvar_nome():
    nome = request.form.get('nome', '').strip()
    tema = request.cookies.get('tema', 'claro')

    resposta = make_response(redirect(url_for('inicio')))

    if nome:
        resposta.set_cookie('nome', nome, max_age=60 * 60 * 24 * 365)

    resposta.set_cookie('tema', tema, max_age=60 * 60 * 24 * 365)
    return resposta


@app.route('/tema/<escolha>')
def trocar_tema(escolha):

    if escolha not in ['claro', 'escuro']:
        escolha = 'claro'

    resposta = make_response(
        redirect(url_for('inicio'))
    )

    resposta.set_cookie(
        'tema', 
        escolha,
        max_age=60*60*24*30
    )

    return resposta

if __name__ == '__main__':
    app.run(debug=True)