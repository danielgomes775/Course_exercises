from flask import Flask
from configuration import configure_all

# Inicializacao do projeto/Flask
app = Flask(__name__)

configure_all(app)

# Executar o projeto em modo de desenvolvimento
app.run(debug=True)









