from utils.db import db

class Chamado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    tipo = db.Column(db.String(100))
    descricao = db.Column(db.String(1000))
    resposta = db.Column(db.String(1000))
    avaliacao = db.Column(db.Integer)
    respondido = db.Column(db.Boolean)

    def __init__(self, titulo, tipo, descricao, resposta, avaliacao, respondido):
        self.titulo = titulo
        self.tipo = tipo
        self.descricao = descricao
        self.resposta = resposta
        self.avaliacao = avaliacao
        self.respondido = respondido