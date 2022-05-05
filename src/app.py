from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tuca123'
app.config['MYSQL_DB'] = 'projeto'

mysql = MySQL(app)

@app.route('/login')
def logindoalazada():
    return render_template('login.html')

@app.route('/cadastro')
def cadastrodopedrada():
    return render_template('cadastro.html')

#------------------------------Usuário-------------------------------#

@app.route('/')
@app.route('/index-cliente')
def indexcliente():
    return render_template('index-cliente.html')

@app.route('/perfil-user')
def perfilusuario():
    return render_template('perfil-user.html')

@app.route('/perfil-exec')
def perfilexecutor():
    return render_template('perfil-exec.html')

@app.route('/solicitar')
def home():
    return render_template('solicitar.html')

@app.route('/solicitar', methods=['POST'])
def fazer_chamado():
    Chamado_data_criacao = datetime.today().strftime('%d-%m-%Y')
    Chamado_data_entrega = '0'
    Chamado_titulo = request.form['Chamado_titulo']
    Chamado_tipo = request.form['Chamado_tipo']
    Chamado_descricao = request.form['Chamado_descricao']
    Chamado_Reposta = ''
    #Chamado_avaliacao = 0
    Chamado_respondido = '0'

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO chamado (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_respondido) VALUES (%s, %s, %s, %s, %s, %s, %s)", (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_Reposta, Chamado_respondido))
    mysql.connection.commit()
    cur.close()
    return render_template('/solicitacoes-p.html')

@app.route('/solicitacoes-p')
def pendentes():
    cur = mysql.connection.cursor()
    Values = cur.execute("SELECT * FROM chamado")
    if Values > 0:
        Chamados = cur.fetchall()
        return render_template('solicitacoes-p.html', Chamados=Chamados)
    else:
        return render_template('solicitacoes-p.html')

@app.route('/solicitacoes-r')
def respondidas():
    cur = mysql.connection.cursor()
    Values = cur.execute("SELECT * FROM chamado")
    if Values > 0:
        Chamados = cur.fetchall()
        print (Chamados)
        return render_template('solicitacoes-r.html', Chamados=Chamados)
    else:
        return render_template('solicitacoes-r.html')

@app.route('/resposta')
def resposta():
    return "solicitando chamado"

#----------------------------Executor--------------------------#

@app.route('/index-executor')
def indexexecutor():
    return render_template('index-executor.html')

@app.route('/solic-act/<idChamado>', methods=['POST','GET'])
def execAceitar(idChamado):

    cur = mysql.connection.cursor()
    if request.method == "POST":
        Chamado_resposta = request.form["resposta"]
        Chamado_respondido = True
        Chamado_data_entrega = datetime.today().strftime('%d-%m-%Y')
        Chamado_aceitar = "Atendido"

        cur.execute("UPDATE chamado SET Chamado_resposta = %s, Chamado_respondido = %s, Chamado_data_entrega = %s, Chamado_aceitar = %s WHERE idChamado = %s", (Chamado_resposta, Chamado_respondido, Chamado_data_entrega, Chamado_aceitar, idChamado))
        cur.connection.commit()
        cur.close()
        return redirect("/solic-r-executor")

    Values = cur.execute("SELECT * FROM chamado")
    Chamados = cur.fetchall()
    for i in Chamados:
        if int(i[0]) == int(idChamado):
            return render_template('solic-act.html', Chamados=i)


@app.route('/solic-act/<idChamado>', methods=['POST','GET'])
def execRecusar(idChamado):

    cur = mysql.connection.cursor()

    if request.method == "POST":
        Chamado_resposta = request.form["resposta"]
        Chamado_respondido = True
        Chamado_data_entrega = datetime.today().strftime('%d-%m-%Y')
        Chamado_aceitar = "Recusado"

        cur.execute("UPDATE chamado SET Chamado_resposta=%s, Chamado_respondido=%s, Chamado_data_entrega=%s, Chamado_aceitar=%s WHERE idChamado=%s", (Chamado_resposta, Chamado_respondido, Chamado_data_entrega, Chamado_aceitar, idChamado))
        cur.connection.commit()
        cur.close()
        return redirect("/solic-r-executor")

    Values = cur.execute("SELECT * FROM chamado")
    Chamados = cur.fetchall()
    for i in Chamados:
        if int(i[0]) == int(idChamado):
            return render_template('solic-act.html', Chamados=i)

@app.route('/solic-executor')
def execSolicitar():
    return render_template('solic-executor.html')

@app.route('/solicitarExec', methods=['POST'])
def fazer_chamado_exec():
    Chamado_data_criacao = datetime.today().strftime('%d-%m-%Y')
    Chamado_data_entrega = '0'
    Chamado_titulo = request.form['Chamado_titulo']
    Chamado_tipo = request.form['Chamado_tipo']
    Chamado_descricao = request.form['Chamado_descricao']
    Chamado_Reposta = ''
    #Chamado_avaliacao = 0
    Chamado_respondido = '0'

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO chamado (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_respondido) VALUES (%s, %s, %s, %s, %s, %s, %s)", (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_Reposta, Chamado_respondido))
    mysql.connection.commit()
    cur.close()
    return render_template('/solic-p-executor.html')

@app.route('/solic-p-executor')
def execPendentes():
    cur = mysql.connection.cursor()
    Values = cur.execute("SELECT * FROM chamado")
    if Values > 0:
        Chamados = cur.fetchall()
        return render_template('solic-p-executor.html', Chamados=Chamados)
    else:
        return render_template('solic-p-executor.html')

@app.route('/solic-r-executor')
def execRespondidas():
    cur = mysql.connection.cursor()
    Values = cur.execute("SELECT * FROM chamado")
    if Values > 0:
        Chamados = cur.fetchall()
        return render_template('solic-r-executor.html', Chamados=Chamados)
    else:
        return render_template('solic-r-executor.html')

if __name__ == "__main__":
    app.run(debug=True)