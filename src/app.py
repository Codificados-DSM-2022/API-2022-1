from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tuca123'
app.config['MYSQL_DB'] = 'projeto'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

mysql = MySQL(app)

@app.route('/')
def index():
    return redirect('login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'senha' in request.form:
        # Create variables for easy access
        email = request.form['email']
        senha = request.form['senha']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE usuario_email = %s AND usuario_senha = %s', (email, senha))
        # Fetch one record and return result
        usuarios = cursor.fetchone()
        # If account exists in accounts table in out database
        if usuarios:
            # Create session data, we can access this data in other routes
            print(usuarios)
            session['loggedin'] = True
            session['idUsuario'] = usuarios[0]
            session['usuario_email'] = usuarios[1]
            session['usuario_senha'] = usuarios[2]
            session['usuario_nome'] = usuarios[3]
            session['usuario_contato'] = usuarios[4]
            session['usuario_endereco'] = usuarios[5]
            # Redirect to home page
            return redirect(url_for('indexcliente'))
        cursor.execute('SELECT * FROM Executores WHERE executor_email = %s AND executor_senha = %s', (email, senha))
        executor = cursor.fetchone()
        if executor:
            session['loggedin'] = True
            session['idExecutor'] = executor[0]
            session['executor_email'] = executor[1]
            session['executor_senha'] = executor[2]
            session['executor_nome'] = executor[3]
            session['executor_contato'] = executor[4]
            session['executor_endereco'] = executor[5]
            return redirect(url_for('indexexecutor'))
            # Account doesnt exist or username/password incorrect
        else:
            msg = 'Senha ou email incorretos!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('idUsuario', None)
    session.pop('usuario_email', None)
    session.pop('usuario_senha', None)
    session.pop('usuario_nome', None)
    session.pop('usuario_contato', None)
    session.pop('usuario_endereco', None)
            
    session.pop('ideExecutor', None)
    session.pop('executor_email', None)
    session.pop('executor_senha', None)
    session.pop('executor_nome', None)
    session.pop('executor_contato', None)
    session.pop('executor_endereco', None)

   # Redirect to login page
    return redirect(url_for('login'))


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and request.form['usuario_senha'] != request.form['usuario_csenha']:
        print(request.form['usuario_senha'])
        print(request.form['usuario_csenha'])
        msg = 'Senhas não conferem!'
    elif request.method == 'POST' and 'usuario_email' in request.form and 'usuario_senha' in request.form and 'usuario_nome' in request.form and 'usuario_contato' in request.form and 'usuario_endereco' in request.form:
        # Create variables for easy access
        usuario_email = request.form['usuario_email']
        usuario_senha = request.form['usuario_senha']
        usuario_nome = request.form['usuario_nome']
        usuario_contato = request.form['usuario_contato']
        usuario_endereco = request.form['usuario_endereco']
        
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuarios WHERE usuario_email = %s AND usuario_senha = %s', (usuario_email, usuario_senha))
        # Fetch one record and return result
        usuarios = cursor.fetchone()
        # If account exists in accounts table in out database

        if not usuarios:
            cursor.execute('SELECT * FROM executores WHERE executor_email = %s AND executor_senha = %s', (usuario_email, usuario_senha))
            # Fetch one record and return result
            executor = cursor.fetchone()
            if not executor:
                cursor.execute('insert into usuarios (usuario_nome, usuario_email, usuario_contato, usuario_endereco, usuario_senha) values (%s, %s, %s, %s, %s)', (usuario_nome, usuario_email, usuario_contato, usuario_endereco, usuario_senha))
                mysql.connection.commit()
                usuarios(cursor)
                return redirect(url_for('login'))
            else:
                msg = 'Email já cadastrado!'
        else:
            msg = 'Email já cadastrado!'
    
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Preencha todos os campos!'
    # Show registration form with message (if any)
    return render_template('cadastro.html', msg=msg)

def usuarios(cursor):
    usuarios = cursor.fetchone()
    # http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users



#------------------------------Usuário-------------------------------#

@app.route('/index-cliente')
def indexcliente():
    return render_template('index-cliente.html', nome=session['usuario_nome'])

@app.route('/perfil-user')
def perfilusuario():
    return render_template('perfil-user.html')

@app.route('/perfil-exec')
def perfilexecutor():
    return render_template('perfil-exec.html')

@app.route('/solicitar')
def solicitar():
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

