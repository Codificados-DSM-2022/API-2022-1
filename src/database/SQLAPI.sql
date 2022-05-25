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
    idtecnico int,
	primary key(idChamado)
);

Alter table Chamado ADD constraint fk_user FOREIGN KEY (idUsuario) REFERENCES Usuarios(idUsuario);
Alter table Chamado ADD constraint fk_tecnico FOREIGN KEY (idtecnico) REFERENCES tecnicos(idtecnico);