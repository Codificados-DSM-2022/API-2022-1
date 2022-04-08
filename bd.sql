create database api;
use api;

create table chamado(
id int primary key auto_increment,
titulo varchar(100),
assunto varchar(30),
descricao varchar(1000),
resposta varchar (1000),
avaliacao int,
respondido bool
)

select * from 