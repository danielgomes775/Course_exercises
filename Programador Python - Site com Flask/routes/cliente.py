from flask import Blueprint, render_template, url_for, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

# Retorna uma lista dos clientes já cadastrados
@cliente_route.route("/")
def lista_clientes():

    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)

# Insere os dados do cliente no banco de dados
@cliente_route.route("/", methods=['POST'])
def inserir_cliente():
    data = request.json

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email']
    )

    return render_template('item_cliente.html', cliente=novo_usuario)

# Retorna um formulário para cadastrar um novo cliente
@cliente_route.route("/new")
def form_cliente():
    return render_template('form_cliente.html')

# Retorna um cliente desejado já cadastrado
@cliente_route.route("/<int:cliente_id>")
def detalhe_cliente(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)

# Retorna um formulário para editar um cliente
@cliente_route.route("/<int:cliente_id>/edit")
def form_edit_cliente(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)


    return render_template('form_cliente.html', cliente=cliente)

# Atualiza as informações do cliente
@cliente_route.route("/<int:cliente_id>/update", methods=['PUT'])
def atualizar_cliente(cliente_id):
    cliente_editado = None
    data = request.json

    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()
            
    return render_template('item_cliente.html', cliente=cliente_editado)

# Deletar um cliente
@cliente_route.route("/<int:cliente_id>/delete", methods=['DELETE'])
def deletar_cliente(cliente_id):
    
    cliente_deletado = Cliente.get_by_id(cliente_id)
    cliente_deletado.delete_instance()
    return {'deleted': 'ok'}