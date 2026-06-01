from flask import Flask, render_template

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    mensagem = ""

    if request.method == 'POST':
        nome = request.form.get('nome')
        if not nome:
            mensagem = "O campo nome é obrigatório."
        else:
            mensagem = f"Cadastro realizado com sucesso! Bem vindo, {nome}"
    return render_template('cadastro.html', mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)

    #ATIVIDADE

    from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/inscricao', methods=['GET', 'POST'])
def inscricao():

    mensagem = ""

    if request.method == 'POST':
        nickname = request.form.get('nickname')
        jogo = request.form.get('jogo')
        email = request.form.get('email')

        if not nickname or not jogo or not email:
            mensagem = "Preencha todos os campos obrigatórios."

        elif len(nickname) < 4:
            mensagem = "Preencha todos os campos obrigatórios."

        else:
            mensagem = "Inscrição realizada com sucesso!"

    return render_template('inscricao.html', mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)



