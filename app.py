from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios = {
    'usuario1': 'senha1',
    'usuario2': 'senha2',
    'usuario3': 'senha3'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']

    if usuario in usuarios and usuarios[usuario] == senha:
        # Autenticação bem-sucedida, redirecionar para a página principal
        return redirect(url_for('pagina_principal'))
    else:
        # Autenticação falhou, mostrar mensagem de erro
        return render_template('login.html', mensagem='Credenciais inválidas. Tente novamente.')

@app.route('/pagina_principal')
def pagina_principal():
    return render_template('index.html')

    
@app.route('/form')
def outra_pagina():
    return render_template('form.html')



if __name__ == '__main__':
    app.run(debug=True)