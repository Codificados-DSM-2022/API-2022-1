from flask import Blueprint, render_template, request, redirect
from models.chamado import Chamado
from utils.db import db

solicitar = Blueprint('solicitar', __name__)

@solicitar.route('/')
@solicitar.route('/solicitar.html')
def home():
    return render_template('solicitar.html')

@solicitar.route('/solicitar', methods=['POST'])
def fazer_chamado():
    titulo = request.form['titulo']
    tipo = request.form['tipo']
    descricao = request.form['descricao']

    novo_chamado = Chamado(titulo, tipo, descricao, '', 0, True)

    db.session.add(novo_chamado)
    db.session.commit()

    return redirect('/')

@solicitar.route('/solicitacoes-p.html')
def pendentes():
    chamados = Chamado.query.all()
    return render_template('solicitacoes-p.html', chamados=chamados)

@solicitar.route('/solicitacoes-r.html')
def respondidas():
    chamados = Chamado.query.all()
    return render_template('solicitacoes-r.html', chamados=chamados)

@solicitar.route('/resposta')
def resposta():
    return "solicitando chamado"
