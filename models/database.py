from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Classe responsável por criar a entidade "Estudante" com os atributos: id, nome e idade. 
class Yup(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(1000))
    preco = db.Column(db.Float)
    imagem = db.Column(db.String(50))
    
    def __init__(self, nome, descricao, preco, imagem):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.imagem = imagem