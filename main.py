from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('formulario.html')


@app.route('/autenticar', methods=['GET'])
def autenticar():
   usuario = request.args.get('usuario')
   senha = request.args.get('senha')
   curso = request.args.get('curso')
   cidade = request.args.get('cidade')
   idade = request.args.get('idade')
   email = request.args.get('E-mail')
   return "{} e {}".format(usuario, senha, curso, cidade, idade, email)

if __name__ == '__main__':
    app.run(debug=True)