# Codificados---DSM-2022
<br id="topo">

<p align="center">
      <h2 align="center"> FATEC Profº Jessen Vidal, SJC - 1º Semestre DSM </h2>
<p align="center">

<hr>
<h1 align="center"> Projeto de gestão de serviços de Tecnologia da Informação </h1>

<p align="center">
    <a href="#sobre">Sobre</a> |
    <a href="#executar">Executando uma aplicação</a> |
    <a href="#backlogs">Backlogs</a> |
    <a href="#userstories">UserStories</a> |
    <a href="#sprint1">Entrega da Primeira Sprint</a> |
    <a href="#sprint2">Entrega da Segunda Sprint</a> |
    <a href="#sprint3">Entrega da Terceira Sprint</a> |
    <a href="#tecnologias">Tecnologias</a> |
    <a href="#equipe">Equipe</a> |
</p>
  
<span id="sobre">

## :bookmark_tabs: Sobre o projeto

Tema: Sistema de Gestão de Serviços de Tecnologia da Informação
<h4>O projeto tem como objetivo desenvolver um sistema que controlar a prestação de serviços de TI, tanto sob o ponto de vista do cliente como do executor</h4>

> _Projeto baseado na metodologia ágil SCRUM_ <br><br>
> **Status do Projeto: Em andamento**

## Entregas de Sprints
| Sprint | Previsão | Status | tag |
|:--:|:----------:|:----------------| :---------: |
| 01 | 14/04/2022 | ✔️ Concluída    | [Tag v1.0](https://github.com/Codificados-DSM-2022/API-2022-1/releases/tag/v1.0) |
| 02 | 15/05/2022 | ✔️ Concluída | [Tag v1.1](https://github.com/Codificados-DSM-2022/API-2022-1/releases/tag/v1.1) |
| 03 | 05/06/2022 | 🕤 Em andamento | -- |

## 📁 Configuração das pastas

* 📂 `doc`: Pasta com Documentos relacionadas ao projeto, na qual encontra as imagens e os gif do arquivo readme e os modelo conceitual e lógico do banco de dados do sistema.
* 📂 `src`: Pasta com os códigos e o modelo físico do sistema. 

      
<span id="executar">
 
## :computer: Executando a aplicação

**Executar o banco de dados:** Para executar o banco de dados precisa inserir a sua senha e usuário do root do MySQL Workbench no arquivo app.py como mostrado no vídeo abaixo:
<br><br>![](/doc/Readme/vsenha.gif)
<br><br> Também precisa executar o script SQL no Workbench, para efetuar essa tarefa basta abrir o script no sistema do MySQL Workbench, no qual se encontra com o nome de SQLAPI.sql no diretório database no src, como mostrado no vídeo abaixo: 
<br><br>![](/doc/Readme/vmysql.gif)
      
Depois de baixar o [python](https://www.pyth.org/download/) e clonar o projeto (ou baixá-lo):

``` powershell
# Acesse a pasta do projeto por meio do terminal
cd src

# Instale as dependências
pip install -r requirements.txt
      
# Habilitar recurso de desenvolvimento
set FLASK_APP=app.py

# Executar a aplicação
flask run

# O site estará disponível através do link: http://localhost:5000/ ou http://127.0.0.1:5000/
```
 → [Voltar ao topo](#topo)
      
 <span id="backlogs">

## :dart: Backlogs

### Backlog do Produto

#### Requisitos Funcionais

| Código | Descrição |UserStories|
| :----: | :----------------------------------------------------------------------------- | :-------: |
| RF 01 | O  sistema  só  deve  ser  acessado  por  pessoas  devidamente  cadastradas,  de  acordo  com  a natureza das operações a serem executadas pelo mesmo. |01|
| RF 02 | O Administrador do sistema, um único usuário,deve possuir acesso total às funcionalidades do sistema. |01|
| RF 03 | Um Executor  de  Serviço(o  sistema  pode  ter  um  ou  vários  executores),  deve  ser  capaz  de atender  a  uma  solicitação  podendo:  a)  atender a  um  serviço  demandado (ao  final  o  chamado  é fechadoe o serviço executado é descrito), b) rejeitar um serviço(o chamado é fechado mas uma justificativa para a rejeição deve ser apresentada).|02|
| RF 04 | Um Usuário Comum (o sistema pode ter um ou muitos usuários) deve ser capaz de abrir uma solicitaçãode  serviço,  visualizar  o  estado  de  todas  as  suas  solicitações,  da  mais  recente  à  mais antiga,e atribuir uma nota (de 0 a 10) à execução de umade suas solicitaçõesque foi fechadapelo executor. |03|
| RF 05 | Uma  solicitação  de  serviço,  ao  ser  criada, deve  ser atribuída  automaticamente  a  um  dos executores de serviço cadastrados no sistema. |04|
| RF 06 | A  atribuição  da  solicitação  deve  seguir  um  esquema  de  distribuição cíclico/  sequencial  de acordo com o número atual de executores (ex. Se há 3 executores cadastrados (A,B,C) e são criadas 7 solicitações, sequencialmente (da 1ª à 7ª ), então os operadores A,B,C receberão as atribuições das solicitaçõesA = [1ª , 4ª , 7ª ] , B= [2ª , 5ª ] , C= [3ª , 6ª ]. |04|
| RF 07 | Ao  ser  criada, uma  solicitação/chamado deve  ser  atrelada ao  seu  criador  e  atribuídaa  um executor.|03|
| RF 08 | Uma solicitação deve possuir: a)data/hora de criação (obrigatório). b)data/hora de fechamento(obrigatório). c)tipo: Problema de Hardware, Problema de Software ou Esclarecimento/Informação. d)uma descrição de abertura(obrigatório). e)uma imagem/arquivo (opcional). f)uma resposta ou justificativa para o fechamento(obrigatório). g)uma avaliação atribuída pelo usuário que a originou, após o fechamento (opcional).|05|
| RF 09 | O sistema deve prover relatórios que mostrem: a)A quantidade percentual de solicitações abertas e fechadas em um determinado intervalo de  tempo (uma espécie de “instantâneo” considerando um dia, uma semana ou um mês específico). b)A evolução diáriada quantidade de solicitações abertas e fechadas, considerando intervalos de tempo especificados (1 semana, 15 dias, etc., utilizando datas de início e término para especificar tal intervalo). c)A avaliação média de cada executor de solicitação.d)A  avaliação  média  global  do  sistema,  tendo  como  base  a  nota  atribuída  a  todos  os chamados.|06|
    
#### Requisitos Não Funcionais

| Código | Descrição |
| :----: | :----------------------------------- |
| RFN 01 |  Desenvolver o back end com alinguagem Python 3+ e o microframework Flask; |08|
| RFN 02 | Utilizar o sistema gerenciador de banco de dados MariaDB/MySQL|09|
| RFN 03 | Utilizar HTML 5 para arquitetura da informação da aplicação |10|
| RFN 04 | Utilizar  CSS  3para  especificação  do  layout  e  demais  características  de  renderização  da interface com o usuário.|10|
| RFN 05 | Utilizar o GitHub para controle de versão dos artefatos de projeto.|11|
| RFN 06 |  Interface com navegação intuitiva (e.g. acesso à informação com poucos “cliques”);|10|
| RFN 07 | Sistema responsivo.|10|
| RFN 08 | Utilizar JavaScript no front end (obs: pode fazer uso de frameworks)|10|
    
 → [Voltar ao topo](#topo)

### Backlog das Sprints
    
#### Sprint 1

| Código | Descrição | UserStories | |
| :----: | :----------------------------------------------------------------------------- | :------: | :-----: |
| RF 03 | Um Executor  de  Serviço (o  sistema  pode  ter  um  ou  vários  executores),  deve  ser  capaz  de atender  a  uma  solicitação  podendo:  a)  atender a  um  serviço  demandado (ao  final  o  chamado  é fechado e o serviço executado é descrito), b) rejeitar um serviço (o chamado é fechado mas uma justificativa para a rejeição deve ser apresentada). | 02 |❌|
| RF 04 | Um Usuário Comum (o sistema pode ter um ou muitos usuários) deve ser capaz de abrir uma solicitação de  serviço,  visualizar  o  estado  de  todas  as  suas  solicitações,  da  mais  recente  à  mais antiga, e atribuir uma nota (de 0 a 10) à execução de uma de suas solicitações que foi fechada pelo executor. |03|❌|
| RF 05 | Uma  solicitação  de  serviço,  ao  ser  criada, deve  ser atribuída  automaticamente  a  um  dos executores de serviço cadastrados no sistema. |04|❌|
| RF 06 | A  atribuição  da  solicitação  deve  seguir  um  esquema  de  distribuição cíclico/  sequencial  de acordo com o número atual de executores (ex. Se há 3 executores cadastrados (A,B,C) e são criadas 7 solicitações, sequencialmente (da 1ª à 7ª ), então os operadores A,B,C receberão as atribuições das solicitações A =[1ª , 4ª , 7ª ] , B= [2ª , 5ª ] , C= [3ª , 6ª ]. |04|❌|
| RF 07 | Ao  ser  criada, uma  solicitação/chamado deve  ser  atrelada ao  seu  criador  e  atribuída a  um executor. |03|❌|
| RF 08 | Uma solicitação deve possuir: a)data/hora de criação(obrigatório). b)data/hora de fechamento(obrigatório). c)tipo: Problema de Hardware, Problema de Software ou Esclarecimento/Informação. d)uma descrição de abertura(obrigatório). e)uma imagem/arquivo (opcional). f)uma resposta ou justificativa para o fechamento(obrigatório). g)uma avaliação atribuída pelo usuário que a originou, após o fechamento (opcional). |05|❌|
    
 #### Sprint 2

| Código | Descrição | UserStories | |
| :----: | :----------------------------------------------------------------------------- | :------: | :-----: |
| RF 03 | Um Executor  de  Serviço (o  sistema  pode  ter  um  ou  vários  executores),  deve  ser  capaz  de atender  a  uma  solicitação  podendo:  a)  atender a  um  serviço  demandado (ao  final  o  chamado  é fechado e o serviço executado é descrito), b) rejeitar um serviço (o chamado é fechado mas uma justificativa para a rejeição deve ser apresentada). | 02 |✔️|
| RF 04 | Um Usuário Comum (o sistema pode ter um ou muitos usuários) deve ser capaz de abrir uma solicitação de  serviço,  visualizar  o  estado  de  todas  as  suas  solicitações,  da  mais  recente  à  mais antiga, e atribuir uma nota (de 0 a 10) à execução de uma de suas solicitações que foi fechada pelo executor. |03|✔️|
| RF 05 | Uma  solicitação  de  serviço,  ao  ser  criada, deve  ser atribuída  automaticamente  a  um  dos executores de serviço cadastrados no sistema. |04|✔️|
| RF 06 | A  atribuição  da  solicitação  deve  seguir  um  esquema  de  distribuição cíclico/  sequencial  de acordo com o número atual de executores (ex. Se há 3 executores cadastrados (A,B,C) e são criadas 7 solicitações, sequencialmente (da 1ª à 7ª ), então os operadores A,B,C receberão as atribuições das solicitações A =[1ª , 4ª , 7ª ] , B= [2ª , 5ª ] , C= [3ª , 6ª ]. |04|✔️|
| RF 07 | Ao  ser  criada, uma  solicitação/chamado deve  ser  atrelada ao  seu  criador  e  atribuída a  um executor. |03|✔️|
| RF 08 | Uma solicitação deve possuir: a)data/hora de criação(obrigatório). b)data/hora de fechamento(obrigatório). c)tipo: Problema de Hardware, Problema de Software ou Esclarecimento/Informação. d)uma descrição de abertura(obrigatório). e)uma imagem/arquivo (opcional). f)uma resposta ou justificativa para o fechamento(obrigatório). g)uma avaliação atribuída pelo usuário que a originou, após o fechamento (opcional). |05|✔️|
| RF 01 | O  sistema  só  deve  ser  acessado  por  pessoas  devidamente  cadastradas,  de  acordo  com  a natureza das operações a serem executadas pelo mesmo.|01|✔️|
| RF 02 | O Administrador do sistema, um único usuário,deve possuir acesso total às funcionalidades do sistema. |01|✔️|
 
#### Sprint 3

| Código | Descrição | UserStories | |
| :----: | :----------------------------------------------------------------------------- | :------: | :-----: |
| RF 09 | O sistema deve prover relatórios que mostrem: a)A quantidade percentual de solicitações abertas e fechadas em um determinado intervalo de  tempo (uma espécie de “instantâneo” considerando um dia, uma semana ou um mês específico). b)A evolução diária da quantidade de solicitações abertas e fechadas, considerando intervalos de tempo especificados (1 semana, 15 dias, etc., utilizando datas de início e término para especificar tal intervalo). c) A avaliação média de cada executor de solicitação. d)A  avaliação  média  global  do  sistema,  tendo  como  base  a  nota  atribuída  a  todos  os chamados. |06 e 07|🕤|
       
 → [Voltar ao topo](#topo)
 
<span id="userstories">      

## :mag: User Stories
       
 | Código | Título | História | Prioridade | Requisitos | Sprint |
| :----: | :--------- | :----------------------------------------------------------------------------- | :----------- | :-----------: | :------: |
|01| Página Administrador | Como administrador quero ter acesso a todas as funcionalidades do sistema para conseguir ter acesso aos relatórios e aos perfis no qual consigo alterar o cargo deles e que só pessoas devidamentes cadastradas tenham acesso ao sistema. | média | RF01 e RF 02 | 2 |
|02| Página solicitações do técnico | Como um técnico quero poder responder a solicitação para que consiga aceitar ou rejeitar uma solicitação e em caso de rejeição é necessário colocar uma resposta  | alta | RF 03 | 1 e 2 |
|03| Página solicitações do usuário| Como usuário comum quero poder abrir uma solicitação para que consiga acompanhar os status das solicitações tanto das mais nova até as mais antigas. | alta | RF 04 e RF 07 | 1 e 2 |
|04| Página solicitações do técnico| Como técnico quero que uma solicitação de serviço seja atribuída a mim por um esquema de distribuição que não aconteça a atribuição de uma mesma solicitação para outro técnico. | média | RF 05 e RF 06 | 1 e 2 |
|05| Página solicitação| Como técnico quero que a solicitação requisita as informações de título, qual é o tipo de problema (Problema de Hardware, Problema de Software ou Esclarecimento/Informação), uma descrição do problema e caso o usuário tenha, uma imagem ou um arquivo que possa ajudar o técnico a entender melhor o problema , e também que o sistema mostre a data e hora de criação e de fechamento para que consiga ter todas as informações necessárias para realizar o serviço. | alta | RF 08 | 1 e 2 |
|06| Página relatórios| Como administrador quero que o sistema gere relatórios que mostram a quantidade percentual de solicitações abertas e fechadas em um determinado tempo, a evolução diária da quantidade de solicitações abertas e fechadas, a avaliação média de cada técnico e a avaliação média global do sistema para que consiga observar a evolução do sistema. | baixa | RF 09 | 3 |
|07| Página avaliações| Como usuário quero que possa avaliar o serviço do técnico, como técnico quero que ao terminar o serviço o usuário responda uma avaliação e como administrador quero que eu possa ver as avaliações feitas pelos usuários, para ver se o serviço foi bem executado. | baixa | RF 09 | 3 |

 → [Voltar ao topo](#topo)

<span id="sprint1">
      
## ✔️ Entrega Primeira Sprint
        
### :desktop_computer: Wireframe e protótipo

Antes de realmente desenvolver o projeto, foi idealizado um layout específico, aplicado em um wireframe. Primeiramente o wireframe não foi aprovado, mas com as resposta e a orientação do cliente podemos arrumar e ir direto para o desenvolvimento de um protótipo.

![](/doc/Readme/Wireframe.jpg) 

 Depois, foi desenvolvido o sistema de acordo com as tecnologias pedidas e o planejamento do backlog.
 
De acordo com o planejamento a primeira Sprint apresentará um sistema com a página de solicitação, do técnico e a página de visualização do usuário, abaixo consegue observar o resultado dela: 

Área do cliente:

![](/doc/Readme/cliente.gif)

Área do técnico:

![](/doc/Readme/executor.gif)
     
### 🎥 Vídeo de apresentação da Sprint 1

Clique [aqui](https://youtu.be/7HnSxZ8ArkI) para acessar o vídeo técnico, no qual apresenta uma demonstração do sistema e os códigos sendo explicado.
      
 → [Voltar ao topo](#topo)
      
<span id="sprint2">
      
## ✔️ Entrega Segunda Sprint
      
### :desktop_computer: Páginas desenvolvindas nessa sprint
      
De acordo com o planejamento a segunda Sprint apresentará um sistema com a página de login e registro tais como as suas páginas de perfil, e a páginas da área do administrador, abaixo consegue observar o resultado dela: 
      
Área Login/Registro:
      
![](/doc/Readme/login.gif)
      
Atualização da Área do cliente:
      
![](/doc/Readme/usuario.gif)
      
Atualização da Área do técnico:
      
![](/doc/Readme/tenico.gif)
      
Área Administrador:
      
![](/doc/Readme/admin.gif)
      
### 🎥 Vídeo de apresentação da Sprint 2

Clique [aqui](https://youtu.be/JMtoR40EMvQ) para acessar o vídeo técnico, no qual apresenta uma demonstração do sistema e os códigos sendo explicado.
      
 → [Voltar ao topo](#topo)
      
<span id="sprint3">
      
## ✔️ Entrega Terceira Sprint
      
### :desktop_computer: Páginas desenvolvindas nessa sprint
      
De acordo com o planejamento da terceira Sprint apresentará um sistema com a página de relatórios e avaliações completa e também o sistema completo, abaixo consegue observar o resultado dela: 
      
Atualização da Área Login/Registro:
      
![](/doc/Readme/alogin.gif)
      
Atualização da Área do cliente:
      
![](/doc/Readme/acliente.gif)
      
Atualização da Área do técnico:
      
![](/doc/Readme/atecnico.gif)
      
Atualização da Área Administrador:
      
![](/doc/Readme/aadmin.gif)
      
Atualização da Página de relatórios:
      
 ![](/doc/Readme/relatorio.gif)
      
Atualização da Página de avaliação:
    

      
### 🎥 Vídeo de apresentação da Sprint 3

Clique [aqui] para acessar o vídeo técnico do sistema completo, no qual apresenta uma demonstração do sistema e os códigos sendo explicado.
      
 → [Voltar ao topo](#topo)

<span id="tecnologias">

## 🛠️ Tecnologias

| Tecnologia | Funcionalidade |
| :------------: | :------------------------------ |
| [Figma](http://www.figma.com) | Prototipagem |
| [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML) | Front-end: estrutura do site |
| [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS) | Front-end: Estilização do site |
| [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) | Front-end: Interações do site |
| [Python](https://www.python.org/) | Back-end |
| [Flask](https://flask.palletsprojects.com/en/2.0.x/) | Servidor |
| [MySQL](https://www.mysql.com/products/workbench/) | Banco de Dados |
| [Visual Studio Code](https://code.visualstudio.com/) | Codificação |
| [Slack](https://slack.com/) | Comunicação com o cliente |
| [Discord](https://discord.com/)|  Comunicação com a equipe |
| [Trello](https://trello.com/pt-BR) | Organização do backlog |
| [GitHub](https://github.com/) | Compartilhamento e versionamento |
      
 → [Voltar ao topo](#topo)

<span id="equipe">

## :busts_in_silhouette: Equipe

| Função | Nome | GitHub |
| :----------: | :----------------------- | :--------------------------------------------: |
| Scrum Master | Andressa Ginevro de Souza | [GitHub](https://github.com/Andressafatec) |
| Product Owner | Gabriel da Cunha de Macedo | [GitHub](https://github.com/Tuuca) |
| Equipe de desenvolvimento | Állan Victor Silva Campos Pereira | [GitHub](https://github.com/AlnVic) |
| Equipe de desenvolvimento | André Felipe da Costa | [GitHub](https://github.com/fecosta290) |
| Equipe de desenvolvimento | Pedro Antonio Rizzo Toledo | [GitHub](https://github.com/Pedro-Toledo) |
| Equipe de desenvolvimento | Victor dos Santos Salles | [GitHub](https://github.com/VictorSantos18) |
      
 ## 📈 Organização da Equipe
      
Para melhor organização do projeto, foi levantado as habilidades técnicas da equipe, dividindo provisoriamente os integrantes em dois times principais: Frontend e Backend, cada um com responsabilidades de acordo com a área destinada mas sempre em comunicação.
      
 #### Sprint 1
      
 ![](/doc/Readme/tabela-s1.png)
      
 #### Sprint 2
      
 ![](/doc/Readme/tabela-s2.png)
      
 #### Sprint 3
      
 ![](/doc/Readme/tabela-s3.png)   

→ [Voltar ao topo](#topo)
