# Codificados---DSM-2022
<br id="topo">

<p align="center">
      <h2 align="center"> FATEC Profº Jessen Vidal, SJC - 1º Semestre DSM </h2>
<p align="center">

<hr>
<h1 align="center"> Projeto de gestão de serviços de Tecnologia da Informação </h1>
  
<span id="sobre">

## :bookmark_tabs: Sobre o projeto

Tema: Sistema de Gestão de Serviços de Tecnologia da Informação
<h4>O projeto tem como objetivo desenvolver um sistema que controlar a prestação de serviços de TI, tanto sob o ponto de vista do cliente como do executor</h4>

> _Projeto baseado na metodologia ágil SCRUM, desenvolver a Proatividade, Autonomia e Entrega de Resultados envolvidos_ <br><br>
> **Status do Projeto: Desenvolvendo**

## :computer: Executando uma aplicação

Depois de baixar o [python](https://www.pyth.org/download/) e clonar o projeto (ou baixá-lo):

``` powershell
# Acesse a pasta do projeto por meio do terminal
cd API-2022-1

# Instale as dependências
pip install -r requirements.
      
# Habilitar recurso de desenvolvimento
set FLASK_ENV=development

# Executar uma aplicação
flask run

# O site estará disponível através do link: http://localhost:5000/
```

**Executar o banco de dados:** Para executar o banco de dados precisa inserir a sua senha do root do MySQL Workbench no arquivo app.py como mostrado no vídeo abaixo:
<br><br>![](/Readme/senha.gif.gif)
<br><br> Também precisa executar o banco de dados no Workbench, para efetuar essa tarefa tem que abrir o arquivo com o banco de dados no sistema do MySQL Workbench, no qual se encontra com o nome de SQLAPI na pasta database do projeto, como mostrado no vídeo abaixo: 
<br><br>![](/Readme/mysql.mp4)
