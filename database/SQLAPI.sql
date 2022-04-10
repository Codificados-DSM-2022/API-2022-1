create database projeto;
use projeto;

CREATE TABLE Usuarios(
    idUser int auto_increment primary key,
    usuario_nome varchar(50) NOT NULL,
	usuario_email varchar(150) NOT NULL,
    usuario_senha varchar(50) NOT NULL,
    );

CREATE TABLE Executores(
	idExecutor int auto_increment primary key,
    executor_nome varchar(50) NOT NULL,
	executor_email varchar(150) NOT NULL,
    executor_senha varchar(50) NOT NULL,
);

CREATE TABLE Chamado(
	idChamado int auto_increment primary key,
    Chamado_data_criacao varchar(15) NOT NULL,
    Chamado_data_entrega varchar(15) NOT NULL,
    Chamado_titulo varchar(50) NOT NULL,
    Chamado_tipo varchar(50) NOT NULL,
	Chamado_descricao varchar(2000) NOT NULL,
    Chamado_resposta varchar(2000) NOT NULL,
    Chamado_avaliacao int NOT NULL,
    Chamado_respondido boolean NOT NULL
    
    -- IdUsuario int,
    -- idExecutor int
);
-- Alter table Chamado ADD constraint fk_user FOREIGN KEY (idUsuario) REFERENCES Usuarios(idUser);
-- Alter table Chamado ADD constraint fk_executor FOREIGN KEY (idExecutor) REFERENCES Usuarios(idUser);

-- delete from Chamado where idChamado = 19;
select * from Chamado;