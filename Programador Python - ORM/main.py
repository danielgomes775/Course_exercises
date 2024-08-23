from database import db, Usuario, Anuncio # Importamos as tabelas para nosso arquivo principal

db.connect() # Chamamos a função para nos conectarmos ao banco de dados 

db.create_tables([Usuario, Anuncio]) # Criamos as tabelas, caso elas não existam no Database


usuario = Usuario.create(nome="Daniel Gomes", email="daniel2@gmail.com", senha="1234")

print("Novo usuário:", usuario.id, usuario.nome, usuario.email)