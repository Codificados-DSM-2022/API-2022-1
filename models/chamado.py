from utils.db import db

class Chamado(db.Model):
    idChamado = db.Column(db.Integer, primary_key=True)
    Chamado_data_criacao = db.Column(db.String(15))
    Chamado_data_entrega = db.Column(db.String(15))
    Chamado_titulo = db.Column(db.String(100))
    Chamado_tipo = db.Column(db.String(100))
    Chamado_descricao = db.Column(db.String(1000))
    Chamado_resposta = db.Column(db.String(1000))
    Chamado_avaliacao = db.Column(db.Integer)
    Chamado_respondido = db.Column(db.Boolean)

    def __init__(self, Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_avaliacao, Chamado_respondido):
        self.Chamado_data_criacao = Chamado_data_criacao
        self.Chamado_data_entrega = Chamado_data_entrega
        self.Chamado_titulo = Chamado_titulo
        self.Chamado_tipo = Chamado_tipo
        self.Chamado_descricao = Chamado_descricao
        self.Chamado_resposta = Chamado_resposta
        self.Chamado_avaliacao = Chamado_avaliacao
        self.Chamado_respondido = Chamado_respondido