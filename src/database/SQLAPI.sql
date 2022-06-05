create database API_Codificados;
use API_Codificados;

CREATE TABLE Usuarios(
    idUsuario INT NOT NULL AUTO_INCREMENT,
	usuario_email varchar(150) NOT NULL,
	usuario_senha varchar(50) NOT NULL,
    usuario_nome varchar(150) NOT NULL,
    usuario_contato varchar(12) not null,
    usuario_endereco varchar(250) NOT NULL,
    usuario_cargo varchar(45) check (usuario_cargo = 'administrador' or usuario_cargo = 'tecnico' or usuario_cargo = 'usuario'),
    primary key(idUsuario)
    );

INSERT INTO Usuarios VALUES(0,'admin','admin','Administrador','admin','admin','administrador');


CREATE TABLE Chamado(
	idChamado INT NOT NULL AUTO_INCREMENT,
    Chamado_data_criacao int NOT NULL,
    Chamado_data_entrega int,
    Chamado_titulo varchar(200) NOT NULL,
    Chamado_tipo varchar(30) NOT NULL,
    Chamado_descricao varchar(2000) NOT NULL,
    Chamado_resposta varchar(2000),
    Chamado_avaliacao int,
    Chamado_respondido bool, 
    Chamado_aceitar bool,
    Chamado_arquivo varchar(1000),
    IdUsuario int,
    idTecnico int,
	primary key(idChamado)
);

Alter table Chamado ADD constraint fk_usuario FOREIGN KEY (idUsuario) REFERENCES Usuarios(idUsuario);
Alter table Chamado ADD constraint fk_tecnico FOREIGN KEY (idTecnico) REFERENCES Usuarios(idUsuario);