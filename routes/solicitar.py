from flask import Blueprint, render_template, request, redirect
from models.chamado import Chamado
from utils.db import db
from datetime import datetime

solicitar = Blueprint('solicitar', __name__)
solicitarExec = Blueprint('solicitarExec', __name__)

@solicitar.route('/solicitar.html')
def home():
    return render_template('solicitar.html')

@solicitar.route('/solicitar', methods=['POST'])
def fazer_chamado():
    Chamado_data_criacao = datetime.today().strftime('%d-%m-%Y')
    Chamado_data_entrega = '0'
    Chamado_titulo = request.form['Chamado_titulo']
    Chamado_tipo = request.form['Chamado_tipo']
    Chamado_descricao = request.form['Chamado_descricao']

    novo_chamado = Chamado(Chamado_data_criacao , Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, '', 0, False)

    db.session.add(novo_chamado)
    db.session.commit()

    return redirect('/')

@solicitar.route('/')
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

#Executor --------------------------------------------------------------------------------------------------------------

@solicitar.route('/solic-act.html')
def execAceitar():
    chamados = Chamado.query.all()
    return render_template('solic-act.html', chamados=chamados)

@solicitar.route('/solic-rec.html')
def execRecusar():
    chamados = Chamado.query.all()
    return render_template('solic-rec.html', chamados=chamados)

@solicitar.route('/solic-executor.html')
def execSolicitar():
    chamados = Chamado.query.all()
    return render_template('solic-executor.html', chamados=chamados)

@solicitar.route('/solicitarExec', methods=['POST'])
def fazer_chamado_exec():
    Chamado_data_criacao = datetime.today().strftime('%d-%m-%Y')
    Chamado_data_entrega = '0'
    Chamado_titulo = request.form['Chamado_titulo']
    Chamado_tipo = request.form['Chamado_tipo']
    Chamado_descricao = request.form['Chamado_descricao']

    novo_chamado = Chamado(Chamado_data_criacao , Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, '', 0, False)

    db.session.add(novo_chamado)
    db.session.commit()

    return redirect('/solic-p-executor.html')

@solicitar.route('/solic-p-executor.html')
def execPendentes():
    chamados = Chamado.query.all()
    return render_template('solic-p-executor.html', chamados=chamados)

@solicitar.route('/solic-r-executor.html')
def execRespondidas():
    chamados = Chamado.query.all()
    return render_template('solic-r-executor.html', chamados=chamados)