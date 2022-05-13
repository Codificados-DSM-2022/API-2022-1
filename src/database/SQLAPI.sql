create database API_Codificados;
use API_Codificados;

CREATE TABLE Administrador(
    idAdm INT NOT NULL AUTO_INCREMENT,
    adm_email VARCHAR(100) NOT NULL,
    adm_senha VARCHAR(50) NOT NULL,
    adm_exec_index INT NOT NULL,
    primary key(idAdm)
);

INSERT INTO Administrador(adm_email, adm_senha, adm_exec_index) VALUES('admin', 'admin', 1);

CREATE TABLE Usuarios(
	idUsuario INT NOT NULL AUTO_INCREMENT,
	usuario_email varchar(150) NOT NULL,
	usuario_senha varchar(50) NOT NULL,
    usuario_nome varchar(150) NOT NULL,
    usuario_contato varchar(12) not null,
    usuario_endereco varchar(250) NOT NULL,
    primary key(idUsuario)
    );

CREATE TABLE Executores(
	idExecutor INT NOT NULL AUTO_INCREMENT,
    executor_email varchar(150) NOT NULL,
    executor_senha varchar(50) NOT NULL,
    executor_nome varchar(150) NOT NULL,
	executor_contato varchar(12) not null,
    executor_endereco varchar(250) NOT NULL,
    primary key(idExecutor)
);

CREATE TABLE Chamado(
	idChamado INT NOT NULL AUTO_INCREMENT,
    Chamado_data_criacao varchar(15) NOT NULL,
    Chamado_data_entrega varchar(15) NOT NULL,
    Chamado_titulo varchar(100) NOT NULL,
    Chamado_tipo varchar(50) NOT NULL,
	Chamado_descricao varchar(2000) NOT NULL,
    Chamado_resposta varchar(2000) NOT NULL,
    Chamado_avaliacao int,
    Chamado_respondido bool, 
    Chamado_aceitar varchar(10),
    IdUsuario int,
    idExecutor int,
	primary key(idChamado)
);

Alter table Chamado ADD constraint fk_user FOREIGN KEY (idUsuario) REFERENCES Usuarios(idUsuario);
Alter table Chamado ADD constraint fk_executor FOREIGN KEY (idExecutor) REFERENCES Executores(idExecutor);

