from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route

# Inicializacao do projeto/Flask
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')

# Executar o projeto em modo de desenvolvimento
app.run(debug=True)