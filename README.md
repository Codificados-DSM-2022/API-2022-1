# Codificados---DSM-2022
<br id="topo">

<p align="center">
      <h2 align="center"> FATEC Profº Jessen Vidal, SJC - 1º Semestre DSM </h2>
<p align="center">

<hr>
<h1 align="center"> Projeto de gestão de serviços de Tecnologia da Informação </h1>

<p align="center">
    <a href="#sobre">Sobre</a> |
    <a href="#backlogs">Backlogs</a> |
    <a href="#executar">Executando uma aplicação</a> |
    <a href="#prototipo">Protótipo</a> |
    <a href="#tecnologias">Tecnologias</a> |
    <a href="#equipe">Equipe</a> |
</p>
  
<span id="sobre">

## :bookmark_tabs: Sobre o projeto

Tema: Sistema de Gestão de Serviços de Tecnologia da Informação
<h4>O projeto tem como objetivo desenvolver um sistema que controlar a prestação de serviços de TI, tanto sob o ponto de vista do cliente como do executor</h4>

> _Projeto baseado na metodologia ágil SCRUM, desenvolver a Proatividade, Autonomia e Entrega de Resultados envolvidos_ <br><br>
> **Status do Projeto: Desenvolvendo**

<span id="executar">
 
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
<br><br>![](/Readme/mysql.gif)
      
 <span id="backlogs">

## :dart: Backlogs

### Backlog do Produto

#### Requisitos Funcionais

| Código | Artigo |
| :----: | :----------------------------------------------------------------------------- |
| RF 01 | O  sistema  só  deve  ser  acessado  por  pessoas  devidamente  cadastradas,  de  acordo  com  a natureza das operações a serem executadas pelo mesmo.
| RF 02 | O Administrador do sistema, um único usuário,deve possuir acesso total às funcionalidades do sistema. 
| RF 03 | Um Executor  de  Serviço(o  sistema  pode  ter  um  ou  vários  executores),  deve  ser  capaz  de atender  a  uma  solicitação  podendo:  a)  atender a  um  serviço  demandado (ao  final  o  chamado  é fechadoe o serviço executado é descrito), b) rejeitar um serviço(o chamado é fechado mas uma justificativa para a rejeição deve ser apresentada).
| RF 04 | Um Usuário Comum (o sistema pode ter um ou muitos usuários) deve ser capaz de abrir uma solicitaçãode  serviço,  visualizar  o  estado  de  todas  as  suas  solicitações,  da  mais  recente  à  mais antiga,e atribuir uma nota (de 0 a 10) à execução de umade suas solicitaçõesque foi fechadapelo executor. | #06 |
| RF 05 | Uma  solicitação  de  serviço,  ao  ser  criada, deve  ser atribuída  automaticamente  a  um  dos executores de serviço cadastrados no sistema. 
| RF 06 | A  atribuição  da  solicitação  deve  seguir  um  esquema  de  distribuição cíclico/  sequencial  de acordo com o número atual de executores (ex. Se há 3 executores cadastrados (A,B,C) e são criadas7 solicitações, sequencialmente (da1ª à7ª ), então os operadores A,B,C receberão as atribuições das solicitaçõesA =[1ª , 4ª , 7ª ] , B= [2ª , 5ª ] , C= [3ª , 6ª ].
| RF 07 | Ao  ser  criada, uma  solicitação/chamadodeve  ser  atreladaao  seu  criador  e  atribuídaa  um executor.
| RF 08 | Uma solicitação deve possuir:a)data/hora de criação(obrigatório).b)data/hora de fechamento(obrigatório).c)tipo: Problema de Hardware, Problema de Software ou Esclarecimento/Informação.d)uma descrição de abertura(obrigatório).e)uma imagem/arquivo (opcional).f)uma resposta ou justificativa para o fechamento(obrigatório).g)uma avaliação atribuída pelo usuário que a originou, após o fechamento (opcional).
| RF 09 | O sistema deve prover relatórios que mostrem:a)Aquantidadepercentualde solicitaçõesabertas e fechadas em um determinado intervalo de  tempo (uma espécie de “instantâneo” considerando um dia, uma semana ou um mês específico).b)A evolução diáriada quantidade de solicitações abertas e fechadas, considerando intervalos de tempo especificados (1 semana, 15 dias, etc., utilizando datas de início e término para especificar tal intervalo).c)A avaliação média de cada executor de solicitação.d)A  avaliação  média  global  do  sistema,  tendo  como  base  a  nota  atribuída  a  todos  os chamados.
    
#### Requisitos Não Funcionais

| Código | Artigo |
| :----: | :----------------------------------- |
| RFN 01 |  Desenvolver o back end com alinguagem Python 3+ e o microframework Flask;
| RFN 02 | Utilizar o sistema gerenciador de banco de dados MariaDB/MySQL
| RFN 03 | Utilizar HTML 5 para arquitetura da informação da aplicação 
| RFN 04 | Utilizar  CSS  3para  especificação  do  layout  e  demais  características  de  renderização  da interface com o usuário.
| RFN 05 | Utilizar o GitHub para controle de versão dos artefatos de projeto.
| RFN 06 |  Interface com navegação intuitiva (e.g. acesso à informação com poucos “cliques”);
| RFN 07 | Sistema responsivo.
| RFN 08 | Utilizar JavaScript no front end (obs: pode fazer uso de frameworks)
    
 → [Voltar ao topo](#topo)

### Backlog das Sprints
    
#### Sprint 1

| Artigo | Descrição |
| :--: | :------------------------- |
| RF 03 | Um Executor  de  Serviço(o  sistema  pode  ter  um  ou  vários  executores),  deve  ser  capaz  de atender  a  uma  solicitação  podendo:  a)  atender a  um  serviço  demandado (ao  final  o  chamado  é fechadoe o serviço executado é descrito), b) rejeitar um serviço(o chamado é fechado mas uma justificativa para a rejeição deve ser apresentada).
| RF 04 | Um Usuário Comum (o sistema pode ter um ou muitos usuários) deve ser capaz de abrir uma solicitaçãode  serviço,  visualizar  o  estado  de  todas  as  suas  solicitações,  da  mais  recente  à  mais antiga,e atribuir uma nota (de 0 a 10) à execução de umade suas solicitaçõesque foi fechadapelo executor.
| RF 05 | Uma  solicitação  de  serviço,  ao  ser  criada, deve  ser atribuída  automaticamente  a  um  dos executores de serviço cadastrados no sistema. 
| RF 06 | A  atribuição  da  solicitação  deve  seguir  um  esquema  de  distribuição cíclico/  sequencial  de acordo com o número atual de executores (ex. Se há 3 executores cadastrados (A,B,C) e são criadas7 solicitações, sequencialmente (da1ª à7ª ), então os operadores A,B,C receberão as atribuições das solicitaçõesA =[1ª , 4ª , 7ª ] , B= [2ª , 5ª ] , C= [3ª , 6ª ].
| RF 07 | Ao  ser  criada, uma  solicitação/chamado deve  ser  atreladaao  seu  criador  e  atribuídaa  um executor.
| RF 08 | Uma solicitação deve possuir:a)data/hora de criação(obrigatório).b)data/hora de fechamento(obrigatório).c)tipo: Problema de Hardware, Problema de Software ou Esclarecimento/Informação.d)uma descrição de abertura(obrigatório).e)uma imagem/arquivo (opcional).f)uma resposta ou justificativa para o fechamento(obrigatório).g)uma avaliação atribuída pelo usuário que a originou, após o fechamento (opcional).
    
 #### Sprint 2

| Artigo | Descrição |
| :--: | :------------------------- |
| RF 01 | O  sistema  só  deve  ser  acessado  por  pessoas  devidamente  cadastradas,  de  acordo  com  a natureza das operações a serem executadas pelo mesmo.
| RF 02 | O Administrador do sistema, um único usuário,deve possuir acesso total às funcionalidades do sistema. 
 
#### Sprint 2

| Artigo | Descrição |
| :--: | :------------------------- |
| RF 09 | O sistema deve prover relatórios que mostrem:a)Aquantidadepercentualde solicitaçõesabertas e fechadas em um determinado intervalo de  tempo (uma espécie de “instantâneo” considerando um dia, uma semana ou um mês específico).b)A evolução diáriada quantidade de solicitações abertas e fechadas, considerando intervalos de tempo especificados (1 semana, 15 dias, etc., utilizando datas de início e término para especificar tal intervalo).c)A avaliação média de cada executor de solicitação.d)A  avaliação  média  global  do  sistema,  tendo  como  base  a  nota  atribuída  a  todos  os chamados.
