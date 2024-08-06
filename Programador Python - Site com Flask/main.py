from flask import Flask, url_for, render_template

# Inicializacao do projeto/Flask
app = Flask(__name__)

# Rotas do projeto
@app.route('/')
def hello_world():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Daniel", "membro_ativo": True },
        {"nome": "Gabriel", "membro_ativo": False },
        {"nome": "Samuel", "membro_ativo": True },
        {"nome": "Rafael", "membro_ativo": False },
    ]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return "<h1> Testando o HTML </h1>"

# Executar o projeto em modo de desenvolvimento
app.run(debug=True)