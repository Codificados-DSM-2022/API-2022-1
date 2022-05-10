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

> _Projeto baseado na metodologia ágil SCRUM_ <br><br>
> **Status do Projeto: Desenvolvendo**

### Entregas de Sprints
| Sprint | Previsão | Status | 
|:--:|:----------:|:----------------|
| 01 | 14/04/2022 | ✔️ Concluída    | 
| 02 | 15/05/2022 | 🕤 Em andamento | 
| 03 | 05/06/2022 | 🛑 Não iniciada | 

<span id="executar">
 
## :computer: Executando a aplicação

**Executar o banco de dados:** Para executar o banco de dados precisa inserir a sua senha e usuário do root do MySQL Workbench no arquivo app.py como mostrado no vídeo abaixo:
<br><br>![](/Readme/senha.gif.gif)
<br><br> Também precisa executar o script SQL no Workbench, para efetuar essa tarefa basta abrir o script no sistema do MySQL Workbench, no qual se encontra com o nome de SQLAPI.sql no diretório database no src, como mostrado no vídeo abaixo: 
<br><br>![](/Readme/mysql.gif)
      
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

| Código | Descrição | UserStories
| :----: | :----------------------------------- | :------: |
| RFN 01 |  Desenvolver o back end com alinguagem Python 3+ e o microframework Flask; |08|
| RFN 02 | Utilizar o sistema gerenciador de banco de dados MariaDB/MySQL|09|
| RFN 03 | Utilizar HTML 5 para arquitetura da informação da aplicação |10|
| RFN 04 | Utilizar  CSS  3para  especificação  do  layout  e  demais  características  de  renderização  da interface com o usuário.|10|
| RFN 05 | Utilizar o GitHub para controle de versão dos artefatos de projeto.|11|
| RFN 06 |  Interface com navegação intuitiva (e.g. acesso à informação com poucos “cliques”);|11|
| RFN 07 | Sistema responsivo.|11|
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
| RF 03 | Um Executor  de  Serviço (o  sistema  pode  ter  um  ou  vários  executores),  deve  ser  capaz  de atender  a  uma  solicitação  podendo:  a)  atender a  um  serviço  demandado (ao  final  o  chamado  é fechado e o serviço executado é descrito), b) rejeitar um serviço (o chamado é fechado mas uma justificativa para a rejeição deve ser apresentada). | 02 |🕤|
| RF 04 | Um Usuário Comum (o sistema pode ter um ou muitos usuários) deve ser capaz de abrir uma solicitação de  serviço,  visualizar  o  estado  de  todas  as  suas  solicitações,  da  mais  recente  à  mais antiga, e atribuir uma nota (de 0 a 10) à execução de uma de suas solicitações que foi fechada pelo executor. |03|🕤|
| RF 05 | Uma  solicitação  de  serviço,  ao  ser  criada, deve  ser atribuída  automaticamente  a  um  dos executores de serviço cadastrados no sistema. |04|🕤|
| RF 06 | A  atribuição  da  solicitação  deve  seguir  um  esquema  de  distribuição cíclico/  sequencial  de acordo com o número atual de executores (ex. Se há 3 executores cadastrados (A,B,C) e são criadas 7 solicitações, sequencialmente (da 1ª à 7ª ), então os operadores A,B,C receberão as atribuições das solicitações A =[1ª , 4ª , 7ª ] , B= [2ª , 5ª ] , C= [3ª , 6ª ]. |04|🕤|
| RF 07 | Ao  ser  criada, uma  solicitação/chamado deve  ser  atrelada ao  seu  criador  e  atribuída a  um executor. |03|🕤|
| RF 08 | Uma solicitação deve possuir: a)data/hora de criação(obrigatório). b)data/hora de fechamento(obrigatório). c)tipo: Problema de Hardware, Problema de Software ou Esclarecimento/Informação. d)uma descrição de abertura(obrigatório). e)uma imagem/arquivo (opcional). f)uma resposta ou justificativa para o fechamento(obrigatório). g)uma avaliação atribuída pelo usuário que a originou, após o fechamento (opcional). |05|🕤|
| RF 01 | O  sistema  só  deve  ser  acessado  por  pessoas  devidamente  cadastradas,  de  acordo  com  a natureza das operações a serem executadas pelo mesmo.|01|🕤|
| RF 02 | O Administrador do sistema, um único usuário,deve possuir acesso total às funcionalidades do sistema. |01|🕤|
 
#### Sprint 3

| Código | Descrição | UserStories | |
| :----: | :----------------------------------------------------------------------------- | :------: | :-----: |
| RF 09 | O sistema deve prover relatórios que mostrem: a)A quantidade percentual de solicitações abertas e fechadas em um determinado intervalo de  tempo (uma espécie de “instantâneo” considerando um dia, uma semana ou um mês específico). b)A evolução diária da quantidade de solicitações abertas e fechadas, considerando intervalos de tempo especificados (1 semana, 15 dias, etc., utilizando datas de início e término para especificar tal intervalo). c) A avaliação média de cada executor de solicitação. d)A  avaliação  média  global  do  sistema,  tendo  como  base  a  nota  atribuída  a  todos  os chamados. |06 e 07|🛑|
       

## :mag: User Stories
       
       
 | Código | Título | História | Prioridade | Requisitos | 
| :----: | :--------- | :----------------------------------------------------------------------------- | :----------- | :-----------: |
|01| Página Administrador | Como administrador quero ter acesso a todas as funcionalidades do sistema para conseguir ter acesso aos relatórios e aos perfis no qual consigo alterar o cargo deles e que só pessoas devidamentes cadastradas tenham acesso ao sistema. | média | RF01 e RF 02 | O professor ainda não respondeu
|02| Página solicitações do executor | Como um executor quero poder responder a solicitação para que consiga aceitar ou rejeitar uma solicitação e em caso de rejeição é necessário colocar uma resposta  | alta | RF 03 | O professor ainda não respondeu
|03| Página solicitações do usuário| Como usuário comum quero poder abrir uma solicitação para que consiga acompanhar os status das solicitações tanto das mais nova até as mais antigas. | alta | RF 04 e RF 07 | O professor ainda não respondeu
|04| Página solicitações do executor| Como executor quero que uma solicitação de serviço seja atribuída a mim por um esquema de distribuição que seja justo e que não aconteça a atribuição de uma mesma solicitação para outro executor, para que consiga ver a solicitação sem que ocorra uma repetição. | média | RF 05 e RF 06 | O professor ainda não respondeu
|05| Página solicitação| Como executor quero que a solicitação requisita as informações de título, qual é o tipo de problema (Problema de Hardware, Problema de Software ou Esclarecimento/Informação), uma descrição do problema e caso o usuário tenha, uma imagem ou um arquivo que possa ajudar o executor a entender melhor o problema , e também que o sistema mostre a data e hora de criação e de fechamento para que consiga ter todas as informações necessárias para realizar o serviço. | alta | RF 08 | O professor ainda não respondeu
|06| Página relatórios| Como administrador quero que o sistema gere relatórios que mostram a quantidade percentual de solicitações abertas e fechadas em um determinado tempo, a evolução diária da quantidade de solicitações abertas e fechadas, a avaliação média de cada executor e a avaliação média global do sistema para que consiga observar a evolução do sistema. | baixa | RF 09 | O professor ainda não respondeu
|07| Página avaliações| Como executor quero que ao terminar a solicitação, que o usuário responda uma avaliação para ver se o serviço foi bem executado. | baixa | RF 09 | O professor ainda não respondeu
|08| Linguagem de progarmação| Como cliente quero que o back end seja resolvido pela a linguagem Python 3+ e o microframework Flask para o funcionamento da página. | alta | RFN 01 | O professor ainda não respondeu
|09| Banco de Dados | Como cliente quero quer o banco de dados seja desenvolvido no sistema de banco de dados MariaDB/MySQL para armazenamento de dados. | alta | RFN 02 | O professor ainda não respondeu
|10| Customização da página e Interface | Como cliente quero que utilize o html 5, CSS 3 e JavaScript para a customizações do layout, de maneira que o sistema fique de fácil entendimento e com um layout que seja intuitiva que consiga ser visível no computador e no celular | média | RFN 03, RFN 04, RFN 06, RFN 07 e RFN 08  | O professor ainda não respondeu
|11| Compartilhamento | Como cliente quero que utilize o Git para o compartilhamento do projeto | baixa | RFN 05  | O professor ainda não respondeu

       


<span id="prototipo">

## :desktop_computer: Wireframe e protótipo

Antes de realmente desenvolver o projeto, foi idealizado um layout específico, aplicado em um wireframe. Primeiramente o wireframe não foi aprovado, mas com as resposta e a orientação do cliente podemos arrumar e ir direto para o desenvolvimento de um protótipo.

![](/Readme/Wireframe.jpg) 

 Depois, foi desenvolvido o sistema de acordo com as tecnologias pedidas e o planejamento do backlog.
 
De acordo com o planejamento a primeira Sprint apresentará um sistema com a página de solicitação, do executor e a página de visualização do usuário, abaixo consegue observar o resultado dela: 

Área de cliente:

![](/Readme/cliente.gif)

Área de executor:

![](/Readme/executor.gif)

Clique [aqui](https://youtu.be/7HnSxZ8ArkI) para acessar o vídeo técnico, no qual apresenta uma demonstração do sistema e os códigos sendo explicado.

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
| [Código do Visual Studio](https://code.visualstudio.com/) | Codificação |
| [Slack](https://slack.com/) | Comunicação com o cliente |
| [Discord](https://discord.com/)|  Comunicação com a equipe |
| [Trello](https://trello.com/pt-BR) | Ferramenta para organização |
| [GitHub](https://github.com/) | Compatilhamento e documentação |

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
      
 ## :busts_in_silhouette: Organização da Equipe
      
 #### Sprint 1
 #### Sprint 2
 #### Sprint 3

→ [Voltar ao topo](#topo)
