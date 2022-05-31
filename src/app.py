from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
from datetime import datetime


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = '12345' # <- Coloque aqui sua senha do MySQL

app.config['MYSQL_DB'] = 'API_Codificados'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

mysql = MySQL(app)


@app.route('/')
def index():   
    return redirect('login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''

    if request.method == 'POST' and 'email' in request.form and 'senha' in request.form:

        email = request.form['email']
        senha = request.form['senha']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE usuario_email = %s AND usuario_senha = %s', (email, senha))

        usuarios = cursor.fetchone()

        if usuarios:
            session['loggedin'] = True
            session['idUsuario'] = usuarios[0]
            session['usuario_email'] = usuarios[1]
            session['usuario_senha'] = usuarios[2]
            session['usuario_nome'] = usuarios[3]
            session['usuario_contato'] = usuarios[4]
            session['usuario_endereco'] = usuarios[5]
            if usuarios[6] == 'usuario':
                session['usuario_cargo'] = 'usuario'
                return redirect(url_for('indexcliente'))
            elif usuarios[6] == 'tecnico':
                session['usuario_cargo'] = 'tecnico'
                return redirect(url_for('indextecnico'))
            elif usuarios[6] == 'administrador':
                session['usuario_cargo'] = 'administrador'
                return redirect(url_for('indexadm'))
        else:
            msg = 'Senha ou email incorretos!'

    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout(): 

    session.pop('loggedin', None)
    session.pop('idUsuario', None)
    session.pop('usuario_email', None)
    session.pop('usuario_senha', None)
    session.pop('usuario_nome', None)
    session.pop('usuario_contato', None)
    session.pop('usuario_endereco', None)
        
    return redirect(url_for('login'))


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro(): 

    msg = ''

    if request.method == 'POST' and request.form['usuario_senha'] != request.form['usuario_csenha']:

        msg = 'Senhas não conferem!'

    elif request.form.get('check') != 'on':
        msg = 'Você deve aceitar o armazenamento de seus dados'

    elif request.method == 'POST' and 'usuario_email' in request.form and 'usuario_senha' in request.form and 'usuario_nome' in request.form and 'usuario_contato' in request.form and 'usuario_endereco' in request.form:

        usuario_email = request.form['usuario_email']
        usuario_senha = request.form['usuario_senha']
        usuario_nome = request.form['usuario_nome']
        usuario_contato = request.form['usuario_contato']
        usuario_endereco = request.form['usuario_endereco']
        

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuarios WHERE usuario_email = %s', (usuario_email))

        usuarios = cursor.fetchone()

        if not usuarios:
            cursor.execute('insert into usuarios (usuario_nome, usuario_email, usuario_contato, usuario_endereco, usuario_senha, usuario_cargo) values (%s, %s, %s, %s, %s, %s)', (usuario_nome, usuario_email, usuario_contato, usuario_endereco, usuario_senha, 'usuario'))
            cursor.connection.commit()
            cursor.close()
            return redirect(url_for('login'))
        else:
            msg = 'Email já cadastrado!'
    
    elif request.method == 'POST':

        msg = 'Preencha todos os campos!'

    return render_template('cadastro.html', msg=msg)


#-------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Administrador---------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------#


@app.route('/index-adm')
def indexadm():  
    if not session.get('loggedin'):
        return redirect(url_for('login'))
    return render_template('adm/index-adm.html')


@app.route('/perfil-adm', methods=['GET', 'POST'])
def perfiladm():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    
    cur = mysql.connection.cursor()
    msg = ''
    if request.method == "POST":
        if str(request.form['senha']) == str(request.form['csenha']) and str(request.form['senha']) != '':
            cur.execute('UPDATE Usuarios SET usuario_nome = %s, usuario_email = %s, usuario_contato = %s, usuario_endereco = %s, usuario_senha = %s WHERE idUsuario = %s', (request.form['nome'], request.form['email'], request.form['contato'], request.form['endereco'], request.form['senha'], session['idUsuario']))
            cur.connection.commit()
            cur.close()
            return redirect('logout')
        if str(request.form['senha']) == '' and str(request.form['csenha']) == '':
            cur.execute('UPDATE Usuarios SET usuario_nome = %s, usuario_email = %s, usuario_contato = %s, usuario_endereco = %s WHERE idUsuario = %s', (request.form['nome'], request.form['email'], request.form['contato'], request.form['endereco'], session['idUsuario']))
            cur.connection.commit()
            cur.close()
            return redirect('logout')
        else:
            msg = 'Senhas não conferem!'
    return render_template('adm/perfil-adm.html', id=session['idUsuario'],nome=session['usuario_nome'], email=session['usuario_email'], senha=session['usuario_senha'],contato=session['usuario_contato'], endereco=session['usuario_endereco'], msg = msg) 


@app.route('/lista-usuarios', methods=['GET', 'POST'])
def listausuarios():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    
    cur = mysql.connection.cursor()
    msg1 = msg2 = ''
    usu = cur.execute("SELECT * FROM usuarios WHERE usuario_cargo = 'usuario'")
    usuarios = cur.fetchall()
    exe = cur.execute("SELECT * FROM usuarios WHERE usuario_cargo = 'tecnico'")
    tecnicos = cur.fetchall()
    if usu == 0:
        msg1 = 'Nenhum usuário cadastrado!'
    if exe == 0:
        msg2 = 'Nenhum tecnico cadastrado!'

    return render_template('adm/lista-usuarios.html', usuarios=usuarios, tecnicos=tecnicos, msg1=msg1, msg2=msg2)


@app.route('/tornar-tecnico/<id>', methods=['GET', 'POST'])
def tornartecnico(id):  
    cur = mysql.connection.cursor()
    cur.execute('UPDATE usuarios SET usuario_cargo = %s WHERE idUsuario = %s', ('tecnico', id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('listausuarios'))


@app.route('/tornar-usuario/<id>', methods=['GET', 'POST'])
def tornarusuario(id):  
    cur = mysql.connection.cursor()
    cur.execute('UPDATE usuarios SET usuario_cargo = %s WHERE idUsuario = %s', ('usuario', id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('listausuarios'))


@app.route('/excluir-usuario/<id>', methods=['GET', 'POST'])
def excluirusuario(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Chamado WHERE idUsuario = %s', [id])
    cur.execute('DELETE FROM usuarios WHERE idUsuario = %s', [id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('listausuarios'))


@app.route('/excluir-tecnico/<id>', methods=['GET', 'POST'])
def excluirtecnico(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Chamado WHERE idtecnico = %s', [id])
    cur.execute('DELETE FROM usuarios WHERE idtecnico = %s', [id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('listausuarios'))


@app.route('/relatorios')
def relatorios():
    mediaNota = 0
    media = 0
    aceitos = 0
    if not session.get('loggedin'):
        return redirect(url_for('login'))
    cur = mysql.connection.cursor()

    ava = cur.execute('SELECT Chamado_avaliacao FROM Chamado WHERE Chamado_avaliacao > 0')
    avaliacao = cur.fetchall()
    if ava > 0:
        for i in avaliacao:
            mediaNota += i[0]
        mediaNota = mediaNota/ava
    else:
        mediaNota = 0

    valor = cur.execute('SELECT * FROM Chamado')
    chamados = cur.fetchall()

    if valor == 0:
        valor = aberto = fechado = rejeitado = 0
    else:
        for i in chamados:
            if i[9] == 1 or i[9] == 0:
                media += 1
                if i[9] == 1:
                    aceitos += 1
        fechado = round(aceitos * 100 / valor,2)
        rejeitado = round((media - aceitos) * 100 / valor,2)
        aberto = 100 - fechado - rejeitado

    mysql.connection.commit()
    cur.close()

    return render_template('/adm/relatorios.html', aberto=aberto, fechado=fechado, rejeitado=rejeitado, avaliacao=avaliacao, valor=valor, mediaNota=mediaNota)


@app.route('/solicitacoes-p-adm')
def pendentesadm():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    
    cur = mysql.connection.cursor()
    Values = cur.execute("SELECT * FROM Chamado WHERE Chamado_Respondido = 0")
    Chamados = cur.fetchall()
    if Values > 0:
        return render_template('adm/solicitacoes-p.html', Chamados=Chamados)
    else:
        return render_template('adm/solicitacoes-p.html')

@app.route('/responderadm/<aceitar>/<idChamado>', methods=['POST','GET'])
def responderadm(aceitar, idChamado):

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM chamado WHERE idChamado = %s", [idChamado])
    chamado = cur.fetchone()
    if request.method == "POST":
        Chamado_resposta = request.form["resposta"]
        Chamado_respondido = True
        Chamado_data_entrega = datetime.today().strftime('%d-%m-%Y')
        if aceitar == '1':
            Chamado_aceitar = 1
        else:
            Chamado_aceitar = 0

        cur.execute("UPDATE chamado SET Chamado_resposta=%s, Chamado_respondido=%s, Chamado_data_entrega=%s, Chamado_aceitar=%s WHERE idChamado=%s", (Chamado_resposta, Chamado_respondido, Chamado_data_entrega, Chamado_aceitar,idChamado))
        cur.connection.commit()
        cur.close()
        return redirect("/solicitacoes-r-adm")
    return render_template('adm/responder.html', aceitar=aceitar, chamado=chamado)

@app.route('/avaliaradm/<id>', methods=['POST', 'GET'])
def avaliaradm(id):
    if not session.get('loggedin'):
        return redirect(url_for('login'))
    cur = mysql.connection.cursor()
    cur.execute("SELECT chamado_resposta FROM chamado WHERE idChamado = %s", [id])
    resposta = cur.fetchone()
    if request.method == 'POST':
        cur.execute("UPDATE chamado SET chamado_avaliacao = %s WHERE idChamado = %s", (request.form['nota'], id))
        cur.connection.commit()
        cur.close()
        return redirect('/solicitacoes-r-adm')
    return render_template('adm/avaliar.html', resposta=resposta[0])


@app.route('/solicitacoes-r-adm')
def respondidasadm():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    
    cur = mysql.connection.cursor()
    Values = cur.execute("SELECT * FROM chamado WHERE Chamado_respondido = 1")
    if Values > 0:
        Chamados = cur.fetchall()
        return render_template('adm/solicitacoes-r.html', Chamados=Chamados)
    else:
        return render_template('adm/solicitacoes-r.html')


@app.route('/solicitar-adm', methods=['POST', 'GET'])
def solicitaradm():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    

    cur = mysql.connection.cursor()
    tecnicos = cur.execute("SELECT * FROM usuarios WHERE usuario_cargo = 'tecnico'")
    exe = cur.fetchall()
    cur.execute("SELECT idTecnico FROM Chamado ORDER BY idChamado DESC LIMIT 1")
    a = cur.fetchone()

    cur.execute("SELECT idUsuario FROM usuarios WHERE usuario_cargo = 'tecnico' ORDER BY idUsuario DESC LIMIT 1")
    ultimo = cur.fetchone()

    msg = ''

    if tecnicos == 0:
        msg = 'Não existem tecnicos cadastrados'
    if request.method == 'POST' and tecnicos > 0:
        Chamado_data_criacao = datetime.today().strftime('%d-%m-%Y')
        Chamado_data_entrega = '0'
        Chamado_titulo = request.form['Chamado_titulo']
        Chamado_tipo = request.form['Chamado_tipo']
        Chamado_descricao = request.form['Chamado_descricao']
        Chamado_Reposta = ''
        #Chamado_avaliacao = 0
        Chamado_respondido = '0'
        idUsuario = session['idUsuario']

        cur.execute("SELECT idUsuario FROM usuarios WHERE usuario_cargo = 'tecnico' ORDER BY idUsuario LIMIT 1")
        primeiro = cur.fetchone()

        if a is not None:
            if a[0] == ultimo[0]:
                cur.execute("INSERT INTO chamado (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_respondido, idUsuario,idTecnico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_Reposta, Chamado_respondido, idUsuario, primeiro))
                mysql.connection.commit()
                cur.close()
                return redirect("/solicitacoes-p-adm")
            for i in exe:
                if (i[0] == a[0] and len(exe) > exe.index(i) + 1):
                    idtecnico = exe[exe.index(i) + 1][0]
                    cur.execute("INSERT INTO chamado (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_respondido, idUsuario,idTecnico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_Reposta, Chamado_respondido, idUsuario,idtecnico))
                    mysql.connection.commit()
                    cur.close()
                    return redirect("/solicitacoes-p-adm")
        else:
            cur.execute("INSERT INTO chamado (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_respondido, idUsuario,idTecnico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_Reposta, Chamado_respondido, idUsuario, primeiro))
            mysql.connection.commit()
            cur.close()
            return redirect("/solicitacoes-p-adm")
    return render_template('adm/solicitar.html', msg=msg, tecnicos=tecnicos)


#-------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Usuario---------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#


@app.route('/index-cliente')
def indexcliente():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    
    return render_template('usuario/index-cliente.html', nome=session['usuario_nome'])


@app.route('/perfil-user', methods=['GET', 'POST'])
def perfilusuario():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    
    cur = mysql.connection.cursor()
    msg = ''
    if request.method == "POST":
        if str(request.form['senha']) == str(request.form['csenha']) and str(request.form['senha']) != '':
            cur.execute('UPDATE Usuarios SET usuario_nome = %s, usuario_email = %s, usuario_contato = %s, usuario_endereco = %s, usuario_senha = %s WHERE idUsuario = %s', (request.form['nome'], request.form['email'], request.form['contato'], request.form['endereco'], request.form['senha'], session['idUsuario']))
            cur.connection.commit()
            cur.close()
            return redirect('logout')
        if str(request.form['senha']) == '' and str(request.form['csenha']) == '':
            cur.execute('UPDATE Usuarios SET usuario_nome = %s, usuario_email = %s, usuario_contato = %s, usuario_endereco = %s WHERE idUsuario = %s', (request.form['nome'], request.form['email'], request.form['contato'], request.form['endereco'], session['idUsuario']))
            cur.connection.commit()
            cur.close()
            return redirect('logout')
        else:
            msg = 'Senhas não conferem!'
    return render_template('usuario/perfil-user.html', id=session['idUsuario'],nome=session['usuario_nome'], email=session['usuario_email'], senha=session['usuario_senha'],contato=session['usuario_contato'], endereco=session['usuario_endereco'], msg = msg) 
    

@app.route('/solicitar', methods=['POST', 'GET'])
def solicitar():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    

    cur = mysql.connection.cursor()
    tecnicos = cur.execute("SELECT * FROM usuarios WHERE usuario_cargo = 'tecnico'")
    exe = cur.fetchall()
    cur.execute("SELECT idTecnico FROM Chamado ORDER BY idChamado DESC LIMIT 1")
    a = cur.fetchone()

    cur.execute("SELECT idUsuario FROM usuarios WHERE usuario_cargo = 'tecnico' ORDER BY idUsuario DESC LIMIT 1")
    ultimo = cur.fetchone()

    msg = ''

    if tecnicos == 0:
        msg = 'Não existem tecnicos cadastrados'
    if request.method == 'POST' and tecnicos > 0:
        Chamado_data_criacao = datetime.today().strftime('%d-%m-%Y')
        Chamado_data_entrega = '0'
        Chamado_titulo = request.form['Chamado_titulo']
        Chamado_tipo = request.form['Chamado_tipo']
        Chamado_descricao = request.form['Chamado_descricao']
        Chamado_Reposta = ''
        #Chamado_avaliacao = 0
        Chamado_respondido = '0'
        idUsuario = session['idUsuario']

        cur.execute("SELECT idUsuario FROM usuarios WHERE usuario_cargo = 'tecnico' ORDER BY idUsuario LIMIT 1")
        primeiro = cur.fetchone()

        if a is not None:
            if a[0] == ultimo[0]:
                cur.execute("INSERT INTO chamado (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_respondido, idUsuario,idTecnico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_Reposta, Chamado_respondido, idUsuario, primeiro))
                mysql.connection.commit()
                cur.close()
                return redirect("/solicitacoes-p")
            for i in exe:
                if (i[0] == a[0] and len(exe) > exe.index(i) + 1):
                    idtecnico = exe[exe.index(i) + 1][0]
                    cur.execute("INSERT INTO chamado (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_respondido, idUsuario,idTecnico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_Reposta, Chamado_respondido, idUsuario,idtecnico))
                    mysql.connection.commit()
                    cur.close()
                    return redirect("/solicitacoes-p")
        else:
            cur.execute("INSERT INTO chamado (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_respondido, idUsuario,idTecnico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_Reposta, Chamado_respondido, idUsuario, primeiro))
            mysql.connection.commit()
            cur.close()
            return redirect("/solicitacoes-p")
    return render_template('usuario/solicitar.html', msg=msg, tecnicos=tecnicos)
    

@app.route('/solicitacoes-p')
def admpendentes():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    
    cur = mysql.connection.cursor()
    msg = cur.execute("SELECT * FROM chamado WHERE idUsuario = %s AND Chamado_respondido = '0'", [session['idUsuario']])
    Chamados = cur.fetchall()
    return render_template('usuario/solicitacoes-p.html', Chamados=Chamados, msg=msg)



@app.route('/solicitacoes-r')
def respondidas():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    
    cur = mysql.connection.cursor()
    msg = cur.execute("SELECT * FROM chamado WHERE idUsuario = %s AND Chamado_respondido = '1'", [session['idUsuario']])
    Chamados = cur.fetchall()
    return render_template('usuario/solicitacoes-r.html', Chamados=Chamados, msg=msg)


@app.route('/avaliar/<id>', methods=['POST', 'GET'])
def avaliar(id):
    if not session.get('loggedin'):
        return redirect(url_for('login'))
    cur = mysql.connection.cursor()
    cur.execute("SELECT chamado_resposta FROM chamado WHERE idChamado = %s", [id])
    resposta = cur.fetchone()
    if request.method == 'POST':
        cur.execute("UPDATE chamado SET chamado_avaliacao = %s WHERE idChamado = %s", (request.form['nota'], id))
        cur.connection.commit()
        cur.close()
        return redirect('/solicitacoes-r')
    return render_template('usuario/avaliar.html', resposta=resposta[0])


#--------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------tecnico---------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#


@app.route('/index-tecnico')
def indextecnico():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    
    return render_template('tecnico/index-tecnico.html', nome=session['usuario_nome'])


@app.route('/perfil-tecnico', methods=['GET', 'POST'])
def perfiltecnico():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    
    cur = mysql.connection.cursor()
    msg = ''
    if request.method == "POST":
        if str(request.form['senha']) == str(request.form['csenha']) and str(request.form['senha']) != '':
            cur.execute('UPDATE Usuarios SET usuario_nome = %s, usuario_email = %s, usuario_contato = %s, usuario_endereco = %s, usuario_senha = %s WHERE idUsuario = %s', (request.form['nome'], request.form['email'], request.form['contato'], request.form['endereco'], request.form['senha'], session['idUsuario']))
            cur.connection.commit()
            cur.close()
            return redirect('logout')
        if str(request.form['senha']) == '' and str(request.form['csenha']) == '':
            cur.execute('UPDATE Usuarios SET usuario_nome = %s, usuario_email = %s, usuario_contato = %s, usuario_endereco = %s WHERE idUsuario = %s', (request.form['nome'], request.form['email'], request.form['contato'], request.form['endereco'], session['idUsuario']))
            cur.connection.commit()
            cur.close()
            return redirect('logout')
        else:
            msg = 'Senhas não conferem!'
    return render_template('tecnico/perfil-tecnico.html', id=session['idUsuario'],nome=session['usuario_nome'], email=session['usuario_email'], senha=session['usuario_senha'],contato=session['usuario_contato'], endereco=session['usuario_endereco'], msg = msg) 


@app.route('/respondertecnico/<aceitar>/<idChamado>', methods=['POST','GET'])
def responderTecnico(idChamado, aceitar):

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM chamado WHERE idChamado = %s", [idChamado])
    chamado = cur.fetchone()
    if request.method == "POST":
        Chamado_resposta = request.form["resposta"]
        Chamado_respondido = True
        Chamado_data_entrega = datetime.today().strftime('%d-%m-%Y')
        if aceitar == '1':
            Chamado_aceitar = 1
        else:
            Chamado_aceitar = 0

        cur.execute("UPDATE chamado SET Chamado_resposta=%s, Chamado_respondido=%s, Chamado_data_entrega=%s, Chamado_aceitar=%s WHERE idChamado=%s", (Chamado_resposta, Chamado_respondido, Chamado_data_entrega, Chamado_aceitar,idChamado))
        cur.connection.commit()
        cur.close()
        return redirect("/solic-r-tecnico")
    return render_template('tecnico/responder.html', aceitar=aceitar, chamado=chamado)

@app.route('/solic-tecnico', methods=['GET', 'POST'])
def tecnicoSolicitar():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    

    cur = mysql.connection.cursor()
    tecnicos = cur.execute("SELECT * FROM usuarios WHERE usuario_cargo = 'tecnico'")
    exe = cur.fetchall()
    cur.execute("SELECT idTecnico FROM Chamado ORDER BY idChamado DESC LIMIT 1")
    a = cur.fetchone()

    cur.execute("SELECT idUsuario FROM usuarios WHERE usuario_cargo = 'tecnico' ORDER BY idUsuario DESC LIMIT 1")
    ultimo = cur.fetchone()

    msg = ''

    if tecnicos == 0:
        msg = 'Não existem tecnicos cadastrados'
    if request.method == 'POST' and tecnicos > 0:
        Chamado_data_criacao = datetime.today().strftime('%d-%m-%Y')
        Chamado_data_entrega = '0'
        Chamado_titulo = request.form['Chamado_titulo']
        Chamado_tipo = request.form['Chamado_tipo']
        Chamado_descricao = request.form['Chamado_descricao']
        Chamado_Reposta = ''
        #Chamado_avaliacao = 0
        Chamado_respondido = '0'
        idUsuario = session['idUsuario']

        cur.execute("SELECT idUsuario FROM usuarios WHERE usuario_cargo = 'tecnico' ORDER BY idUsuario LIMIT 1")
        primeiro = cur.fetchone()

        if a is not None:
            if a[0] == ultimo[0]:
                cur.execute("INSERT INTO chamado (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_respondido, idUsuario,idTecnico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_Reposta, Chamado_respondido, idUsuario, primeiro))
                mysql.connection.commit()
                cur.close()
                return redirect("/solic-p-tecnico")
            for i in exe:
                if (i[0] == a[0] and len(exe) > exe.index(i) + 1):
                    idtecnico = exe[exe.index(i) + 1][0]
                    cur.execute("INSERT INTO chamado (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_respondido, idUsuario,idTecnico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_Reposta, Chamado_respondido, idUsuario,idtecnico))
                    mysql.connection.commit()
                    cur.close()
                    return redirect("/solic-p-tecnico")
        else:
            cur.execute("INSERT INTO chamado (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_resposta, Chamado_respondido, idUsuario,idTecnico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Chamado_data_criacao, Chamado_data_entrega, Chamado_titulo, Chamado_tipo, Chamado_descricao, Chamado_Reposta, Chamado_respondido, idUsuario, primeiro))
            mysql.connection.commit()
            cur.close()
            return redirect("/solic-p-tecnico")
    return render_template('tecnico/solicitar.html', msg=msg, tecnicos=tecnicos)


@app.route('/solic-p-tecnico')
def tecnicoPendentes():
    if not session.get('loggedin'):
        return redirect(url_for('login'))    
    cur = mysql.connection.cursor()
    msg1 = cur.execute("SELECT * FROM chamado WHERE chamado_respondido = '0' and idtecnico = %s", (session['idUsuario'],))
    Chamados = cur.fetchall()
    msg2 = cur.execute("SELECT * FROM chamado WHERE chamado_respondido = '0' and idUsuario = %s", (session['idUsuario'],))
    Chamados2 = cur.fetchall()
    return render_template('tecnico/solic-p-tecnico.html', Chamados=Chamados, msg1=msg1, Chamados2=Chamados2, msg2=msg2)



@app.route('/solic-r-tecnico')
def tecnicoRespondidas():
    if not session.get('loggedin'):
        return redirect(url_for('login'))
    cur = mysql.connection.cursor()
    msg1 = cur.execute("SELECT * FROM chamado WHERE chamado_respondido = '1' and idtecnico = %s", (session['idUsuario'],))
    Chamados = cur.fetchall()
    msg2 = cur.execute("SELECT * FROM chamado WHERE chamado_respondido = '1' and idUsuario = %s", (session['idUsuario'],))
    Chamados2 = cur.fetchall()
    return render_template('tecnico/solic-r-tecnico.html', Chamados=Chamados, msg1=msg1, Chamados2=Chamados2, msg2=msg2)

@app.route('/avaliartec/<id>', methods=['POST', 'GET'])
def avaliartec(id):
    if not session.get('loggedin'):
        return redirect(url_for('login'))
    cur = mysql.connection.cursor()
    cur.execute("SELECT chamado_resposta FROM chamado WHERE idChamado = %s", [id])
    resposta = cur.fetchone()
    if request.method == 'POST':
        cur.execute("UPDATE chamado SET chamado_avaliacao = %s WHERE idChamado = %s", (request.form['nota'], id))
        cur.connection.commit()
        cur.close()
        return redirect('/solic-r-tecnico')
    return render_template('tecnico/avaliartec.html', resposta=resposta[0])

if __name__ == "__main__":
    app.run(debug=True)