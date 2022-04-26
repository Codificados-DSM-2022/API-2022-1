create database projeto;
use projeto;

CREATE TABLE Usuarios(idUser int auto_increment,
    usuario_nome varchar(150) NOT NULL,
	usuario_email varchar(150) NOT NULL,
    usuario_senha varchar(50) NOT NULL,
    primary key(idUser)
    );

CREATE TABLE Executores(
	idExecutor int auto_increment,
    executor_nome varchar(150) NOT NULL,
	executor_email varchar(150) NOT NULL,
    executor_senha varchar(50) NOT NULL,
    primary key(idExecutor)
);

CREATE TABLE Chamado(
	idChamado int auto_increment,
    Chamado_data_criacao varchar(15) NOT NULL,
    Chamado_data_entrega varchar(15) NOT NULL,
    Chamado_titulo varchar(100) NOT NULL,
    Chamado_tipo varchar(50) NOT NULL,
	Chamado_descricao varchar(2000) NOT NULL,
    Chamado_resposta varchar(2000) NOT NULL,
    Chamado_avaliacao int,
    Chamado_respondido bool, 
    Chamado_aceitar varchar(10),
    primary key(idChamado)
    
    -- IdUsuario int,
    -- idExecutor int
);

-- Alter table Chamado ADD constraint fk_user FOREIGN KEY (idUsuario) REFERENCES Usuarios(idUser);
-- Alter table Chamado ADD constraint fk_executor FOREIGN KEY (idExecutor) REFERENCES Usuarios(idUser);

select * from Chamado;